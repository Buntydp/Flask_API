import flask
from flask import Flask, jsonify, request, render_template
import json
import sqlite3
import numpy as np
import pickle
import pandas as pd

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

def caller(request):
    if request.method == "POST":
        requ=json.loads(request.data)
        req=requ['content']
        print('in caller....')
        rat=req['rating']
        print('1st...')
        cs=req['Company_Size']
        to=req['Type_of_ownersip']
        ind=req['Industry']
        sec=req['Sector']
        rev=req['Revenue']
        state=req['state']
        age=req['age']
        ex=req['Excel']
        vs=req['Visualisation']
        ml=req['ML']
        st=req['ST']
        ra=req['RA']
        lead=req['LS']
        ct=req['CT']
        com=req['com']
        aws=req['aws']
        db=req['db']
        ana=req['ana']
        js=req['job_simp']
        sen=req['Seniority']
        df = pd.read_csv(r"op_real4.csv")
        df_model = df[['sal_med','rating','size','com_type','industry','sector','revenue',
             'state','age','excel_yn','visu_yn','ml_yn','st_yn','risk_yn','lead_yn','critical_yn','comu_yn','aws_yn','db_yn','anal_yn','job_simp','seniority']]  
        df_model.loc[len(df_model.index)-1]=[159.43,float(rat),cs,to,ind,sec,rev, ' '+state,int(age),int(ex),int(vs),int(ml),int(st),int(ra),int(lead),int(ct),int(com),int(aws),int(db),int(ana),str(js),str(sen)]     
        dfd=pd.get_dummies(df_model)
        dfd=dfd.drop('sal_med', axis =1)
        newdata = list(dfd.iloc[len(df_model.index)-1,:])
        x_in = np.array(newdata).reshape(1,-1)
        model = load_models()
        prediction = str(round(model.predict(x_in)[0],2))
        return prediction
        

def ranger(sal):
    if int(sal)>=26 and int(sal)<=30:
        return '26-30'
    elif int(sal)>=31 and int(sal)<=35:
        return '31-35'
    elif int(sal)>=36 and int(sal)<=40:
        return '36-40'
    elif int(sal)>=41 and int(sal)<=45:
        return '41-45'
    elif int(sal)>=46 and int(sal)<=50:
        return '46-50'
    elif int(sal)>=51 and int(sal)<=55:
        return '51-55'
    elif int(sal)>=56 and int(sal)<=60:
        return '56-60'
    elif int(sal)>=61 and int(sal)<=65:
        return '61-65'
    elif int(sal)>=66 and int(sal)<=70:
        return '66-70'
    elif int(sal)>=71 and int(sal)<=75:
        return '71-75'
    elif int(sal)>=76 and int(sal)<=80:
        return '76-80'
    elif int(sal)>=81 and int(sal)<=85:
        return '81-85'
    elif int(sal)>=86 and int(sal)<=90:
        return '86-90'
    elif int(sal)>=91 and int(sal)<=95:
        return '91-95'
    elif int(sal)>=96 and int(sal)<=100:
        return '96-100'
    elif int(sal)>=101 and int(sal)<=105:
        return '101-105'
    elif int(sal)>=106 and int(sal)<=110:
        return '106-110'
    elif int(sal)>=111 and int(sal)<=115:
        return '111-115'
    elif int(sal)>=116 and int(sal)<=120:
        return '116-120'
    elif int(sal)>=121 and int(sal)<=125:
        return '121-125'
    elif int(sal)>=126 and int(sal)<=130:
        return '126-130'
    elif int(sal)>=131 and int(sal)<=135:
        return '131-135'
    elif int(sal)>=136 and int(sal)<=140:
        return '136-140'
    elif int(sal)>=141 and int(sal)<=145:
        return '141-145'
    elif int(sal)>=146 and int(sal)<=150:
        return '146-150'
    elif int(sal)>=151 and int(sal)<=155:
        return '151-155'
    elif int(sal)>=156 and int(sal)<=160:
        return '156-160'
    elif int(sal)>=161 and int(sal)<=165:
        return '161-165'
    elif int(sal)>=166 and int(sal)<=170:
        return '166-170'
    elif int(sal)>=171 and int(sal)<=175:
        return '171-175'
    elif int(sal)>=176 and int(sal)<=180:
        return '176-180'
    elif int(sal)>=181 and int(sal)<=185:
        return '181-185'
    elif int(sal)>=186 and int(sal)<=190:
        return '186-190'
    elif int(sal)>=191 and int(sal)<=195:
        return '191-195'
    elif int(sal)>=196 and int(sal)<=200:
        return '196-200'
    elif int(sal)>=201 and int(sal)<=205:
        return '201-205'
    elif int(sal)>=206 and int(sal)<=210:
        return '206-210'
    elif int(sal)>=211 and int(sal)<=215:
        return '211-215'
    elif int(sal)>=216 and int(sal)<=220:
        return '216-220'
    elif int(sal)>=221 and int(sal)<=225:
        return '221-225'
    elif int(sal)>=226 and int(sal)<=230:
        return '226-230'
    elif int(sal)>=231 and int(sal)<=235:
        return '231-235'
    elif int(sal)>=236 and int(sal)<=240:
        return '236-240'
    elif int(sal)>=241 and int(sal)<=245:
        return '241-245'
    elif int(sal)>=246 and int(sal)<=250:
        return '246-250'
    elif int(sal)>=251 and int(sal)<=255:
        return '251-255'
    elif int(sal)>=256 and int(sal)<=260:
        return '256-260'
    elif int(sal)>=261 and int(sal)<=265:
        return '261-265'
    elif int(sal)>=266 and int(sal)<=270:
        return '266-270'
    elif int(sal)>=271 and int(sal)<=275:
        return '271-275'
    elif int(sal)>=276 and int(sal)<=280:
        return '276-280'
    elif int(sal)>=281 and int(sal)<=285:
        return '281-285'
    elif int(sal)>=286 and int(sal)<=290:
        return '286-290'
    elif int(sal)>=291 and int(sal)<=295:
        return '291-295'
    elif int(sal)>=296 and int(sal)<=300:
        return '296-300'   
    else:
        return 'Out Of Range'

def info(request, ranger):
    request=json.loads(request.data)
    request=request['content']
    ind=str(request['Industry'])
    sec=str(request['Sector'])
    jsim=str(request['job_simp'])
    state=str(request['state'])
    conn = sqlite3.connect(r"WareHouse.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM First WHERE industry= '{ind}' AND sector= '{sec}' AND state =' {state}' AND job_simp='{jsim}' AND range='{ranger}';")
    outputs = cur.fetchall()
    if not outputs:
        cur.execute(f"SELECT * FROM First WHERE industry= '{ind}' AND sector= '{sec}' AND state =' {state}' AND range='{ranger}';")
        outputs = cur.fetchall()
        if not outputs:
            cur.execute(f"SELECT * FROM First WHERE industry= '{ind}' AND state =' {state}' AND range='{ranger}';")
            outputs = cur.fetchall()
            if not outputs:
                cur.execute(f"SELECT * FROM First WHERE industry= '{ind}' AND sector= '{sec}' AND state =' {state}' AND job_simp='{jsim}';")
                outputs = cur.fetchall()
                if not outputs:
                    cur.execute(f"SELECT * FROM First WHERE industry= '{ind}' AND sector= '{sec}' AND state =' {state}';")
                    outputs = cur.fetchall()
                    if not outputs:
                        cur.execute(f"SELECT * FROM First WHERE industry= '{ind}' AND state =' {state}';")
                        outputs = cur.fetchall()
                        if len(outputs)==1:
                            cur.execute(f"SELECT * FROM First WHERE industry= '{ind}';")
                            out = outputs+(cur.fetchall())
                            outputs=out[:5]
                        if not outputs:
                            cur.execute(f"SELECT * FROM First WHERE industry= '{ind}';")
                            outputs = cur.fetchall()
                        



    # ===================================================

    res = [list(ele) for ele in outputs]
    ids = [list(ele)[0] for ele in res]
    df =pd.read_csv('details.csv')
    similarity = pickle.load(open('similarity2.pkl','rb'))
    job_index=df[df['id'] == res[0][0]].index[0]
    distances = similarity[job_index]
    job_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:21]
    temp = [list(e)[0] for e in job_list]
    for i in range(len(ids)):
       temp.insert(i,ids[i])
    
    fl=[]
    [fl.append(x) for x in temp if x not in fl]

    fl=tuple(fl)
    slist=[]
    conn.row_factory=sqlite3.Row
    cur2 = conn.cursor()
    for i in fl:
        cur2.execute(f'SELECT * FROM First WHERE id="{i}";')
        fuli=cur2.fetchone()
        slist.append(fuli)
    conn.close()
    return json.dumps([dict(x) for x in slist])

def total():
    conn = sqlite3.connect(r"WareHouse.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM Register;")
    outputs = cur.fetchall()
    conn.close()
    return len(outputs)

