# Loan Approval Prediction using Decision Tree

## Project Overview

Loan Approval Prediction is a Machine Learning-based web application that predicts whether a loan application should be approved or rejected based on applicant information. The system uses a Decision Tree Classifier and a Flask-based web interface for real-time predictions.

Banks and financial institutions receive numerous loan applications daily. Manual evaluation can be time-consuming and may lead to inconsistencies. This project automates the loan approval process using Machine Learning techniques to improve efficiency and decision-making.

---

## Objective

* Predict loan approval status accurately.
* Reduce manual effort in loan evaluation.
* Improve decision-making efficiency.
* Provide an explainable Machine Learning solution.

---

## Why Decision Tree?

* Easy to understand and interpret.
* Works effectively with numerical and categorical data.
* Mimics human decision-making through rule-based logic.
* Suitable for business and financial applications.

---

## Dataset Features

| Feature       | Description                            |
| ------------- | -------------------------------------- |
| Age           | Applicant age                          |
| Income        | Monthly income                         |
| CreditScore   | Creditworthiness score                 |
| ExistingLoans | Number or status of existing loans     |
| LoanStatus    | Approved or Rejected (Target Variable) |

---

## Technology Stack

* Programming Language: Python
* Machine Learning Library: Scikit-learn
* Web Framework: Flask
* Frontend: HTML, CSS
* Model: Decision Tree Classifier

---

## Project Structure

```bash
loan_approval_project/
│
├── app.py
├── train_model.py
├── loan_model.pkl
├── dataset.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Workflow

1. Load the dataset.
2. Perform data preprocessing.
3. Train the Decision Tree model.
4. Save the trained model.
5. Develop the Flask web application.
6. Accept user input through the web interface.
7. Predict loan approval status.
8. Display the prediction result.

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/loan-approval-prediction.git
cd loan-approval-prediction
```

### Install Required Libraries

```bash
pip install flask pandas scikit-learn
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000/
```

---

## Example Prediction

### Input

* Age: 32
* Income: ₹40,000
* Credit Score: 730
* Existing Loans: No

### Output

Loan Approved

---

## Model Details

| Parameter     | Value                    |
| ------------- | ------------------------ |
| Algorithm     | Decision Tree Classifier |
| Learning Type | Supervised Learning      |
| Problem Type  | Classification           |

---

## Interview Explanation

"I developed a Loan Approval Prediction System using a Decision Tree Classifier and Flask. The model evaluates applicant information such as income, credit score, and existing loans to determine whether a loan should be approved or rejected. The application provides a user-friendly web interface for making predictions and demonstrates the practical application of Machine Learning in financial decision-making."

---

## Future Enhancements

* Improve model accuracy using larger datasets.
* Add performance evaluation metrics.
* Deploy the application on cloud platforms.
* Upgrade to advanced models such as Random Forest or XGBoost.
* Integrate a database for storing loan applications.

---

## Author

**Gururaj Gali**

Bachelor of Technology (B.Tech) in Computer Science Engineering

Machine Learning Enthusiast | Python Developer

Email: [galigururaj94@gmail.com](mailto:galigururaj94@gmail.com)

LinkedIn: Add your LinkedIn profile link

GitHub: Add your GitHub profile link
