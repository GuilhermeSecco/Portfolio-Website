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

def index_en():
    return render_template('index_en.html')

def projetos():
    return render_template('projetos.html')

bp_simulador = Blueprint("simulador_credito", __name__)

modelo, preproc, cols = carregar_modelo()

# Carrega importâncias das features
importancias = carregar_importancias()
if not importancias:
    importancias = calcular_importancias(modelo, cols)

# Carrega as taxas medianas
taxas_por_grade = load(os.path.join("ml_models", "taxas_por_grade.pkl"))

#Rota do simulador
@bp_simulador.route("/projetos/simulador-credito", methods=["GET", "POST"])
def simulador_credito():
    if request.method == "GET":
        return render_template("projetos/simulador-credito.html", importancias=importancias,
                               nomes_legiveis=NOMES_LEGIVEIS)

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
        "projetos/simulador-credito.html",
        resultado=resultado,
        dados=form_data,
        importancias=importancias,
        explicacao=explicacao,
        nomes_legiveis=NOMES_LEGIVEIS
    )