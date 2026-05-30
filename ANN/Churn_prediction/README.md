# 💰 Customer Salary Prediction using ANN

## 📌 Project Overview
This project predicts the **Estimated Salary** of a bank customer using an Artificial Neural Network (ANN). It uses customer data such as credit score, age, balance, geography, and other features to make salary predictions.

---

## 🚀 Features
- Data preprocessing
- Handling categorical variables (Label Encoding & One-Hot Encoding)
- Feature scaling
- Train-test split
- ANN model using TensorFlow/Keras
- Actual vs Predicted Salary comparison

---

## 📂 Project Structure

```text
📁 Salary_prediction/
│
├── 📁 Data/
│   └── 📄 Churn_Modelling.csv
│
├── 📁 Notebooks/
│   └── 📓 salary.ipynb
│
├── ⚙️ requirements.txt
└── 📘 README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run
```bash
jupyter notebook
```
Open:
```
Notebooks/salary.ipynb
```

---

## 📊 Dataset

- File: `Churn_Modelling.csv`
- Features used:
  - Credit Score
  - Geography
  - Gender
  - Age
  - Tenure
  - Balance
  - Number of Products
  - Has Credit Card
  - Is Active Member
  - Exited
- Target Column: **EstimatedSalary**

---

## 🧠 Model Details

- Model: Artificial Neural Network (ANN)
- Hidden Layer 1: 64 neurons, ReLU activation
- Hidden Layer 2: 32 neurons, ReLU activation
- Output Layer: 1 neuron, Linear activation (regression)
- Loss Function: Mean Squared Error (MSE)
- Optimizer: Adam (learning rate = 0.01)
- Callbacks: EarlyStopping, TensorBoard

---

## 📈 Output

The model outputs a **continuous salary value** (regression).
A comparison table is generated showing:

| Column | Description |
|---|---|
| Actual_EstimatedSalary | Real salary from the dataset |
| Predicted_Value | ANN model's predicted salary |
| Error | Difference between predicted and actual |

---

## ⚠️ Note

> The `EstimatedSalary` column in this dataset is randomly assigned and has **no strong correlation** with other features. As a result, model accuracy may be limited. This project is intended for **learning purposes** to understand ANN regression workflows.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib

---

## 👨‍💻 Author

Vashu Khanpara
