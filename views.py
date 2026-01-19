from flask import Blueprint, render_template, request
from ml_models.model_predict_simulador import (
    carregar_modelo, preprocessar_dados, prever_risco_credito,
    carregar_importancias, calcular_importancias, explicar_previsao,
    NOMES_LEGIVEIS
)
from joblib import load
import os
import numpy as np

#Rotas principais do site
def index():
    return render_template('index.html')

bp_simulador = Blueprint("credit_simulator", __name__)

modelo, preproc, cols = carregar_modelo()

# Carrega importâncias das features
importancias = carregar_importancias()
if not importancias:
    importancias = calcular_importancias(modelo, cols)

# Carrega as taxas medianas
taxas_por_grade = load(os.path.join("ml_models", "taxas_por_grade.pkl"))

#Rota do simulador
@bp_simulador.route("/projects/credit-simulator", methods=["GET", "POST"])
def credit_simulator():
    if request.method == "GET":
        # 1. Definimos os dados iniciais (Renda Mensal de 3000 -> Anual 39000)
        default_data = {
            "person_age": 26.0,
            "credit_score": 1000.0,
            "person_income": 39000.0, 
            "loan_amnt": 20000.0,
            "loan_intent": "EDUCATION",
            "person_home_ownership": "OWN",
            "cb_person_default_on_file": "N"
        }

        # 2. Precisamos replicar a lógica de Grade e Ratio que você tem no POST
        score = default_data["credit_score"]
        if score >= 900: default_data["loan_grade"] = "A"
        elif score >= 800: default_data["loan_grade"] = "B"
        elif score >= 700: default_data["loan_grade"] = "C"
        elif score >= 600: default_data["loan_grade"] = "D"
        elif score >= 500: default_data["loan_grade"] = "E"
        elif score >= 400: default_data["loan_grade"] = "F"
        else: default_data["loan_grade"] = "G"

        default_data["loan_int_rate"] = taxas_por_grade.get(default_data["loan_grade"], 12.0)
        default_data["loan_to_income_ratio"] = default_data["loan_amnt"] / default_data["person_income"]

        # 3. Processamento via ML (Certifique-se que 'preproc', 'modelo' e 'cols' estão acessíveis)
        try:
            X_ready = preprocessar_dados(default_data, preproc, cols)
            resultado_inicial = prever_risco_credito(modelo, X_ready)
            
            # Formatação para o HTML
            resultado_inicial.update({
                "renda_anual": default_data["person_income"],
                "score": int(score),
                "grade": default_data["loan_grade"],
                "taxa_aplicada": default_data["loan_int_rate"]
            })

            explicacao_inicial = explicar_previsao(X_ready, importancias)
        except Exception as e:
            # Caso dê erro no modelo, carrega a página limpa para não travar o site
            print(f"Erro na predição inicial: {e}")
            return render_template("projects/credit_simulator.html", 
                                   importancias=importancias, 
                                   nomes_legiveis=NOMES_LEGIVEIS)

        return render_template(
            "projects/credit_simulator.html",
            resultado=resultado_inicial,
            dados=default_data,
            explicacao=explicacao_inicial,
            importancias=importancias,
            nomes_legiveis=NOMES_LEGIVEIS
        )
    
    form_data = request.form.to_dict()

    # Conversão de renda mensal -> anual
    form_data["person_income"] = float(form_data["person_income"]) * 13

    # Conversão de numéricos
    for key in ["person_age", "person_income", "loan_amnt"]:
        form_data[key] = float(form_data[key])

    # Conversão de score → grade
    score = float(form_data["credit_score"])
    if score >= 900:
        form_data["loan_grade"] = "A"
    elif score >= 800:
        form_data["loan_grade"] = "B"
    elif score >= 700:
        form_data["loan_grade"] = "C"
    elif score >= 600:
        form_data["loan_grade"] = "D"
    elif score >= 500:
        form_data["loan_grade"] = "E"
    elif score >= 400:
        form_data["loan_grade"] = "F"
    else:
        form_data["loan_grade"] = "G"

    # Taxa automática conforme grade
    form_data["loan_int_rate"] = taxas_por_grade.get(form_data["loan_grade"], 12.0)

    # Cria nova feature
    form_data["loan_to_income_ratio"] = form_data["loan_amnt"] / max(form_data["person_income"], 1)

    # Preprocessa e prediz
    X_ready = preprocessar_dados(form_data, preproc, cols)
    resultado = prever_risco_credito(modelo, X_ready)

    resultado["renda_anual"] = form_data["person_income"]
    resultado["score"] = int(score)
    resultado["grade"] = form_data["loan_grade"]
    resultado["taxa_aplicada"] = form_data["loan_int_rate"]

    # Explicação da previsão atual
    explicacao = explicar_previsao(X_ready, importancias)

    return render_template(
        "projects/credit_simulator.html",
        resultado=resultado,
        dados=form_data,
        importancias=importancias,
        explicacao=explicacao,
        nomes_legiveis=NOMES_LEGIVEIS
    )

#Rota da página Olist
@bp_simulador.route("/projects/olist-data-analysis")
def olist_data_analysis_page():
    return render_template("projects/olist_data_analysis.html")