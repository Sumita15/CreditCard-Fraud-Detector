# Credit Card Fraud Detection

A Streamlit web app that predicts whether a credit card transaction is **fraudulent or legitimate** using a trained **Logistic Regression** model. The model was built on a balanced dataset derived from the original highly imbalanced credit card transaction data.

---

## Features

- Input all 30 transaction features (Time, V1–V28, Amount)
- Scales inputs using StandardScaler for accurate prediction
- Returns instant prediction: Legitimate or ⚠️ Fraudulent
- Lightweight and fast — perfect for quick demonstrations

---

## Model Info

- **Algorithm**: Logistic Regression
- **Preprocessing**: Feature scaling with `StandardScaler`
- **Training**: Performed on a balanced dataset (492 fraud + 492 legit)

---

## Project Structure

```

credit-card-fraud-detection/
├── app.py                # Streamlit app
├── logistic\_model.pkl    # Trained logistic regression model
├── scaler.pkl            # Fitted StandardScaler
├── requirements.txt      # Dependencies
└── README.md             # Project overview

```

---

## Setup Instructions

### Local Setup

1. Clone the repository:

   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection

2. Install dependencies:
   
   pip install -r requirements.txt

4. Run the Streamlit app:

   streamlit run app.py

---

## Live Demo

[[Click here to try the app]](https://creditcard-fraud-detector.streamlit.app)

---

## Dataset Info

* [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
* 284,807 transactions
* Highly imbalanced (only 0.17% frauds)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Sumita Lakhlan**

