import os
from flask import Flask, render_template, jsonify, request

from models.expense import Expense, ExpenseSchema
from models.income import Income, IncomeSchema
from models.transaction_type import TransactionType

from routes.userRoute import userRoute

app = Flask(__name__)

@app.route('/')
def home():
    return "coucou"


@app.route('/incomes')
def get_incomes():
    # return jsonify(incomes)
    return {"coucou":"pouet"}

app.register_blueprint(userRoute,url_prefix='/user')




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

