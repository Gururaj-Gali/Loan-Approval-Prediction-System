from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("loan_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        age = int(request.form["age"])
        income = int(request.form["income"])
        credit = int(request.form["credit"])
        loans = int(request.form["loans"])

        result = model.predict([[age, income, credit, loans]])

        prediction = "✅ Loan Approved" if result[0] == 1 else "❌ Loan Rejected"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
