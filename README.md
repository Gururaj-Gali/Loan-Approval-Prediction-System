<!DOCTYPE html>
<html lang="en">
<head>
    
</head>
<body>

<div class="container">

<h1>🏦 Loan Approval Prediction using Decision Tree</h1>

<p>
A <strong>Machine Learning–based web application</strong> that predicts whether a loan should be
<strong>Approved or Rejected</strong> based on applicant details.
The project uses a <strong>Decision Tree Classifier</strong> and a <strong>Flask web interface</strong>.
</p>

<h2>📌 Project Overview</h2>
<p>
Banks and financial institutions receive many loan applications every day.
Manual evaluation is time-consuming and error-prone.
</p>
<p>
This project automates the process using <strong>Decision Tree Machine Learning</strong>,
which mimics human decision-making through simple rules.
</p>

<h2>🎯 Objective</h2>
<ul>
    <li>Predict loan approval status</li>
    <li>Reduce manual effort</li>
    <li>Improve decision accuracy</li>
    <li>Provide an explainable ML solution</li>
</ul>

<h2>🧠 Why Decision Tree?</h2>
<ul>
    <li>Easy to understand and explain</li>
    <li>Works well with numerical and categorical data</li>
    <li>Human-like decision rules</li>
    <li>Business-friendly model</li>
</ul>

<h2>📊 Dataset Features</h2>
<table>
    <tr>
        <th>Feature</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Age</td>
        <td>Applicant age</td>
    </tr>
    <tr>
        <td>Income</td>
        <td>Monthly income</td>
    </tr>
    <tr>
        <td>CreditScore</td>
        <td>Creditworthiness score</td>
    </tr>
    <tr>
        <td>ExistingLoans</td>
        <td>Active loan status</td>
    </tr>
    <tr>
        <td>LoanStatus</td>
        <td>Approved / Rejected (Target)</td>
    </tr>
</table>

<h2>⚙️ Technology Stack</h2>
<ul>
    <li><strong>Programming Language:</strong> Python</li>
    <li><strong>Machine Learning:</strong> Scikit-learn</li>
    <li><strong>Web Framework:</strong> Flask</li>
    <li><strong>Frontend:</strong> HTML, CSS</li>
    <li><strong>Model:</strong> Decision Tree Classifier</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
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
</pre>

<h2>🔄 Workflow</h2>
<ol>
    <li>Load dataset</li>
    <li>Preprocess data</li>
    <li>Train Decision Tree model</li>
    <li>Save trained model</li>
    <li>Build Flask web app</li>
    <li>Predict loan status using user input</li>
</ol>

<h2>▶️ How to Run the Project</h2>

<h3>Install Required Libraries</h3>
<pre><code>pip install flask pandas scikit-learn</code></pre>

<h3>Train the Model</h3>
<pre><code>python train_model.py</code></pre>

<h3>Run Flask Application</h3>
<pre><code>python app.py</code></pre>

<h3>Open Browser</h3>
<pre><code>http://127.0.0.1:5000/</code></pre>

<h2>🧪 Example Prediction</h2>
<p><strong>Input:</strong></p>
<ul>
    <li>Age: 32</li>
    <li>Income: ₹40,000</li>
    <li>Credit Score: 730</li>
    <li>Existing Loans: No</li>
</ul>

<p><strong>Output:</strong> Loan Approved ✅</p>

<h2>📈 Model Details</h2>
<ul>
    <li>Algorithm: Decision Tree Classifier</li>
    <li>Learning Type: Supervised Learning</li>
    <li>Problem Type: Classification</li>
</ul>

<h2>🎤 Interview Explanation</h2>
<p>
“I built a Decision Tree–based Loan Approval Prediction system with a Flask web interface.
The model evaluates applicant data such as income, credit score, and existing loans to automate loan approval decisions.”
</p>

<h2>🚀 Future Enhancements</h2>
<ul>
    <li>Improve accuracy with more data</li>
    <li>Add model evaluation metrics</li>
    <li>Deploy on cloud platforms</li>
    <li>Upgrade to Random Forest</li>
</ul>

<h2>👨‍💻 Author</h2>
<p>
<strong>Gururaj Gali</strong><br>
Machine Learning Enthusiast | Python Developer
</p>

</div>

</body>
</html>
