# 🌐 Interactive Portfolio — Guilherme Fernandes Secco

High-performance interactive portfolio developed with **Flask**, **Bootstrap 5**, and dynamic **GitHub API** integration. This project centralizes my core deliveries in **Data Science**, **Machine Learning**, and **Software Engineering**.

<img width="1870" height="992" alt="image" src="https://github.com/user-attachments/assets/2dc1a0dc-eb79-4987-9749-8c8ff646f96f" />


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

- 📱 **Responsive and Lightweight Design**  
  Fully adapted for mobile and desktop devices.

---

## 🧠 Project Structure

    project_root/
    ├── app.py # Main Flask file
    ├── views.py # Site blueprints and routes
    ├── static/
    │ ├── bootstrap/ # Local CSS framework
    │ ├── css/ # Styles for each project
    │ ├── img/ # Icons and images
    │ └── script.js # Global scripts
    ├── templates/
    │ ├── base.html # Base template
    │ ├── index.html # Home page
    │ └── projects/
    │ └── simulador-credito.html # Example of project with dedicated page
    └── ml_models/ # Machine Learning models and scripts


---

## 💻 Technologies Used

| Category | Technologies |
|------------|-------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Integration** | GitHub REST API |
| **Animations and Style** | Animate.css, Bootstrap Icons |
| **Machine Learning (specific projects)** | XGBoost, scikit-learn, pandas, NumPy |

---

## 🧩 Featured Projects

### 💳 [Intelligent Credit Simulator](https://github.com/GuilhermeSecco/credit-simulator)
> A credit approval simulator that uses XGBoost to predict default risk and define personalized interest rates.

📊 **Topics:** `python`, `machine-learning`, `flask`, `bootstrap`, `xgboost`

---

### 🧠 Other Projects
In addition to the simulator, the portfolio automatically integrates all projects from my GitHub that have the topic:

    portfolio-project

For projects with active pages (Study cases), simply add:

    portfolio-page

This automatically adds an "Study Case" button to the project card. 🚀

For projects with active demonstrations (e.g., Streamlit, Flask, or published sites), simply add:

    portfolio-demo
    
This automatically adds an "Access Demo" button to the project card. 🚀

## 🔧 Local Setup

To run the portfolio locally:

    1️⃣ Clone the repository
    git clone [https://github.com/GuilhermeSecco/portfolio.git](https://github.com/GuilhermeSecco/portfolio.git)
    cd portfolio

    2️⃣ Create virtual environment
    python -m venv venv
    source venv/bin/activate  # (or venv\Scripts\activate on Windows)

    3️⃣ Install dependencies
    pip install -r requirements.txt

    4️⃣ Run the Flask server
    python app.py

    Access:
    👉 http://localhost:5000

## 🌈 Visual Structure

    🔹 Fixed sidebar with section navigation (Home, About, Skills, Projects)

    🔹 Automatic project cards, powered by GitHub topics

    🔹 Contact buttons with links to LinkedIn, GitHub and Email

    🔹 Predominant dark theme with highlight colors

## 💡 Próximas Melhorias

    🔍 Modo de busca para projetos

    🧾 Página de blog/tutoriais técnicos

    💬 Seção interativa para feedback dos visitantes

    🌙 Tema claro/escuro alternável

## Links

### [💼LinkedIn](https://www.linkedin.com/in/guilherme-f-secco/)
### [💻GitHub](https://github.com/GuilhermeSecco)
