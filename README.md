# 🌐 Interactive Portfolio — Guilherme Fernandes Secco

High-performance interactive portfolio developed with **Flask**, **Bootstrap 5**, and dynamic **GitHub API** integration. This project centralizes my core deliveries in **Data Science**, **Machine Learning**, and **Software Engineering**.

<img width="1850" height="1002" alt="image" src="https://github.com/user-attachments/assets/c2524524-a395-41b7-966f-de992f545ccf" />

---

## 🚀 Technical Highlights

This website was developed to gather, organize, and dynamically present my **data science projects**.  
Each project has a dedicated card featuring:
- 💻 Project Name;
- 🧩 Technologies Badges;
- 💬 Project Description;
- 🔗 Direct links to GitHub and, when available, project pages.

The portfolio is fully **responsive and dynamic**, automatically powered via the **GitHub API** — no need to manually update each project.

---

## ⚙️ Main Features

- 🔄 **Automatic GitHub Integration**  
  Displays all repositories containing the topic `portfolio-project`.

- 🧩 **Display of Technologies and Languages Used**  
  Each project displays colored badges based on its tags (e.g., `python`, `machine-learning`, `flask`, etc).

- 💻 **Individual Pages for Selected Projects**  
  Special projects have a dedicated route within the site, with a customized layout.

- 🌈 **Dynamic Themes and Smooth Animations**  
  Modern interface built with **Bootstrap 5** and **Animate.css**.

- 📱 **Design responsivo e leve**  
  Totalmente adaptado para dispositivos móveis e desktop.

---

## 🧠 Estrutura do Projeto

    project_root/
    ├── app.py # Arquivo principal Flask
    ├── views.py # Blueprints e rotas do site
    ├── static/
    │ ├── bootstrap/ # Framework CSS local
    │ ├── css/ # Estilos de cada projeto
    │ ├── img/ # Ícones e imagens
    │ └── script.js # Scripts globais
    ├── templates/
    │ ├── base.html # Template principal
    │ ├── index.html # Página inicial
    │ ├── projetos.html # Página com listagem de repositórios
    │ └── projetos/
    │ └── simulador-credito.html # Exemplo de projeto com página dedicada
    └── ml_models/ # Modelos e scripts de Machine Learning


---

## 💻 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|-------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Integração** | GitHub REST API |
| **Animações e Estilo** | Animate.css, Bootstrap Icons |
| **Machine Learning (em projetos específicos)** | XGBoost, scikit-learn, pandas, NumPy |

---

## 🧩 Projetos em Destaque

### 💳 [Simulador de Crédito Inteligente](https://github.com/GuilhermeSecco/Simulador-Credito)
> Um simulador de aprovação de crédito que usa **XGBoost** para prever risco de inadimplência e definir taxa de juros personalizada.

📊 **Tópicos:** `python`, `machine-learning`, `flask`, `bootstrap`, `xgboost`

---

### 🧠 Outros Projetos
Além do simulador, o portfólio integra automaticamente todos os projetos do meu GitHub que possuem o tópico:

    portfolio-project

Para projetos com demonstrações ativas (por exemplo, Streamlit, Flask ou sites publicados), basta adicionar também:

    portfolio-demo

Isso adiciona automaticamente um botão “Acessar Demonstração” ao card do projeto. 🚀

## 🔧 Configuração Local

Para executar o portfólio localmente:

    1️⃣ Clonar o repositório
    git clone https://github.com/GuilhermeSecco/portfolio.git
    cd portfolio
    
    2️⃣ Criar ambiente virtual
    python -m venv venv
    source venv/bin/activate  # (ou venv\Scripts\activate no Windows)
    
    3️⃣ Instalar dependências
    pip install -r requirements.txt
    
    4️⃣ Executar o servidor Flask
    python app.py
    
    Acesse:
    👉 http://localhost:5000

## 🌈 Estrutura Visual

    🔹 Sidebar fixa com navegação por seções (Início, Sobre, Habilidades, Projetos, Contato)

    🔹 Cards de projetos automáticos, alimentados por tópicos do GitHub

    🔹 Seção de contato com links para LinkedIn e GitHub

    🔹 Tema escuro predominante, com realces em cores de destaque

## 💡 Próximas Melhorias

    🔍 Modo de busca para projetos

    🧾 Página de blog/tutoriais técnicos

    💬 Seção interativa para feedback dos visitantes

    🌙 Tema claro/escuro alternável

## Links

### [💼LinkedIn](https://www.linkedin.com/in/guilherme-f-secco/)
### [💻GitHub](https://github.com/GuilhermeSecco)
