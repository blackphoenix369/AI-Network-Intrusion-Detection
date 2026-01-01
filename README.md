# 🔐 AI-Based Network Intrusion Detection System (NIDS)

An **AI-powered Network Intrusion Detection System (NIDS)** built using **Python, Machine Learning, C++**, and **Streamlit**. This project is designed for **cybersecurity learning, academic demonstration, and portfolio use**, focusing on ethical intrusion detection.

---

## 📌 Project Overview

Traditional network security systems rely on static rules and signatures, which fail to detect new or unknown attacks. This project implements an **intelligent NIDS** that:

* Simulates network traffic using a **C++ traffic engine**
* Trains a **Machine Learning model (Random Forest)** on traffic data
* Detects **malicious vs normal traffic**
* Provides an interactive **web-based dashboard** using Streamlit

> ⚠️ **Ethical Use Only**: This project is strictly for educational and defensive cybersecurity purposes.

---

## 🧠 Key Features

* ✅ AI-based attack detection (Machine Learning)
* ✅ C++ network traffic simulation engine
* ✅ Python-based model training & inference
* ✅ Real-time detection dashboard (Streamlit UI)
* ✅ Modular and extensible architecture
* ✅ Beginner-friendly & exam-ready project

---

## 🛠️ Technology Stack

| Component               | Technology                   |
| ----------------------- | ---------------------------- |
| Programming Languages   | Python, C++                  |
| Machine Learning        | Scikit-learn (Random Forest) |
| Data Processing         | Pandas, NumPy                |
| Model Serialization     | Joblib                       |
| Dashboard UI            | Streamlit                    |
| Development Environment | VS Code                      |
| OS Support              | Windows / Linux              |

---

## 📁 Project Structure

```text
AI_NIDS_Project/
├── traffic_engine.cpp      # C++ traffic simulation engine
├── model_train.py          # ML model training script
├── detect.py               # CLI-based intrusion detection
├── nids_dashboard.py       # Streamlit web dashboard
├── .gitignore              # Ignored files and folders
├── README.md               # Project documentation
```

> Generated files like `traffic_data.csv`, `nids_model.pkl`, and `venv/` are excluded using `.gitignore`.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/USERNAME/AI-NIDS.git
cd AI-NIDS
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn joblib streamlit
```

---

## 🚀 How to Run the Project

### 🔹 Step 1: Compile & Run Traffic Engine (C++)

```bash
g++ traffic_engine.cpp -o traffic_engine
.\traffic_engine.exe     # Windows
# ./traffic_engine        # Linux
```

✔ Generates `traffic_data.csv`

---

### 🔹 Step 2: Train AI Model

```bash
python model_train.py
```

✔ Generates `nids_model.pkl`

---

### 🔹 Step 3: Run Streamlit Dashboard

```bash
streamlit run nids_dashboard.py
```

✔ Access at: `http://localhost:8501`

---

## 📊 Dashboard Capabilities

* View project overview
* Load trained ML model
* Input simulated network traffic
* Detect intrusion (Normal / Attack)
* Real-time prediction results

---

## 🎓 Academic & Learning Outcomes

* Understanding of **Network Intrusion Detection Systems**
* Practical application of **Machine Learning in Cybersecurity**
* Experience with **C++ & Python integration**
* Hands-on knowledge of **Streamlit dashboards**
* Ethical cybersecurity project implementation

---

## 🛡️ Ethical Disclaimer

This project is developed **only for educational and defensive cybersecurity purposes**. It does **not perform real attacks** and should not be used for malicious activities.

---

## 📚 References

* CIC-IDS Dataset – Canadian Institute for Cybersecurity
* Scikit-learn Documentation
* Streamlit Documentation
* Python Official Docs

---

## 👤 Author

**Rohit Chakraborty**
B.Tech – Computer Science
Aspiring Software Development Engineer (SDE)

---

## ⭐ Future Enhancements

* 🔄 Real packet capture using `libpcap`
* 🤖 Deep Learning (CNN / LSTM) based NIDS
* 🐧 Linux kernel-level traffic monitoring
* ☁️ Cloud-based deployment

---

⭐ *If you find this project useful, consider giving it a star!*
