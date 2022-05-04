import flask
from flask import Flask, jsonify, request, render_template
import json
import sqlite3

def Login(request):
    result=False
    print('inside login')
    request=json.loads(request.data)
    request=request['content']
    # fname=request['firstName']
    # lname=request['lastName']
    email=request['email']
    password=request['password']
    print(email)
    print(password)
    conn = sqlite3.connect(r"WareHouse.db")
    conn.row_factory=sqlite3.Row
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM Register WHERE "Email" = "{email}" AND "Password" = "{password}";')
    op=cur.fetchone()
    # print('output of db',op)
    if(op == None):
        return {'decision':False, 'data': {'Email':email, 'Password':password}}
    else:
        return {'decision':True, 'data': ([dict(op)])[0]}


def Register(request):
    # result=False
    print('inside register')
    request=json.loads(request.data)
    request=request['content']
    fname=request['firstName']
    lname=request['lastName']
    email=request['email']
    password=request['password']
    conn = sqlite3.connect(r"WareHouse.db")
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM Register WHERE "Email" = "{email}";')
    op=cur.fetchall()
    if(len(op)==0):
        cur.execute(f"INSERT INTO Register  (FirstName ,LastName, Email, Password, 'Role') VALUES ('{fname}', '{lname}', '{email}', '{password}', 'user' );")
        conn.commit()
        print('success')
        # result=True
        final_output = {'decision':True, 'data': {'FirstName': fname, 'LastName': lname,'Email':email, 'Password':password, 'Role':'user'}}
        print(final_output)
    # cur.execute("INSERT INTO Register  (FirstName ,LastName, Email, Password, 'Role') VALUES ('test', 'test', 'tgmail', 'ssword', 'user' );")
    else:
        # result=False
        print('same email id is already exists...')
        final_output = {'decision':False, 'data': {'FirstName': fname, 'LastName': lname,'Email':email, 'Password':password, 'Role':'user'}}
    cur.execute("SELECT id FROM Register;")
    
    outputs = cur.fetchall()
    print(outputs)
    conn.close()
    return final_output
    

