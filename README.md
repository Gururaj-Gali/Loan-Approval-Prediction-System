<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Loan Approval Prediction using Decision Tree</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            margin: 30px;
            background-color: #f8f9fa;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background: #eee;
            padding: 4px 6px;
            border-radius: 4px;
        }
        pre {
            background: #eee;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        table, th, td {
            border: 1px solid #aaa;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background: #e3e3e3;
        }
        .container {
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
        }
    </style>
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
    <li><
