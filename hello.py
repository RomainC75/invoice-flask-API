from flask import Flask, render_template, jsonify, request
import os

from models.expense import Expense, ExpenseSchema
from models.income import Income, IncomeSchema
from models.transaction_type import TransactionType

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]

@app.route('/')
def home():
    return "coucou"

@app.route('/incomes')
def get_incomes():
    # return jsonify(incomes)
    return {"coucou":"pouet"}

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    print(request.get_json())
    return incomes, 200
    return {"message":"ok"}, 200


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    print(transactions)
    return "", 204




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)