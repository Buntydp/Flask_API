import flask
from flask import Flask, jsonify, request, render_template, session
from call import caller, ranger, info, total
from auth import Register, Login
import json
from flask_cors import CORS

app = Flask(__name__)

pred_config = {
    "origins": "*",
    "methods": ["OPTIONS", "GET", "POST"],
}

CORS(app)

app.secret_key = "vrudit"  
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test', methods=['GET','POST'])
def test():
    return {'201':'ok done'}

@app.route('/predict', methods=['GET','POST'])
def predict():
    prediction =caller(request)
    session['salary']=prediction
    print(session)
    rang=ranger(float(prediction))
    data=info(request,rang)
    return data

@app.route('/salary', methods=['GET'])
def predicts():
    if 'salary' in session:  
        s = session['salary']
        session.clear()  
        print('output:',s)
        return str(s) 
    else:
        print('failed for salary')
        return '0000'

@app.route('/pre', methods=['GET','POST'])
def pres():
    prediction =caller(request)
    return prediction

@app.route('/register', methods=['GET','POST'])
def register():
    des = Register(request)
    print(des)
    return {'decision':des}

@app.route('/login', methods=['GET','POST'])
def login():
    des = Login(request)
    print(type(des), des)
    return des

@app.route('/jobs', methods=['GET','POST'])
def jobs():
    Total = total()
    return str(Total)
        