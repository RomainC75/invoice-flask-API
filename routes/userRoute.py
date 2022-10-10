
from flask import Blueprint, request, jsonify
from db import conn
from models.user import UserSchema, User
userRoute = Blueprint('userRoute', __name__)

@userRoute.route("/signup", methods=['POST'])
def signup():
    print(request.get_json())
    newUser = UserSchema().load(request.get_json())
    print('==>',newUser)
    user = User(newUser.email, newUser.password)
    print(user)
    # cur=conn.cursor()
    # print('==>',request.get_json())
    # req=request.get_json()
    # cur.execute("INSERT INTO User (email, password) VALUES(%s ,%s)", (req['email'], req['password']))
    # conn.commit()
    # cur.execute("SELECT * FROM User")
    # dt = cur.fetchall()
    # return jsonify({'data':dt}),200
    return "ok"

@userRoute.route("/dbd", methods=['POST'])
def hello():
    cur=conn.cursor()
    print('==>',request.get_json())
    req=request.get_json()
    cur.execute("INSERT INTO User (email, password) VALUES(%s ,%s)", (req['email'], req['password']))
    conn.commit()
    cur.execute("SELECT * FROM User")
    dt = cur.fetchall()
    return jsonify({'data':dt}),200



# @userRoute.route('/expenses/<int:id>', methods=['POST'])
# def add_expense(id):
#     expense = ExpenseSchema().load(request.get_json())
#     transactions.append(expense)
#     print(transactions, id)
#     return "", 204