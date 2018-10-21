# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:09:10 2018

@author: distroter
"""
from flask import Flask,request
from cryptography.fernet import Fernet
import MySQLdb
app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
    ECID = request.form['ECID'] 
    EPW = request.form['EPW']
    key = request.form['key']
    
    key = key.encode('utf-8')
    print(key)
    
    cipher_suite = Fernet(key)
    
    DCID = cipher_suite.decrypt(ECID.encode('utf-8'))
    DPW = cipher_suite.decrypt(EPW.encode('utf-8'))
    conn = MySQLdb.connect(user="root", passwd="rishi26071997", db="rishi")
    cur = conn.cursor()

    cur.execute("insert into iot values ( %s , %s )",(DCID.decode('utf-8'),DPW.decode('utf-8')))
    conn.commit()
    cur.close()
    conn.close()
    return DCID
    
    

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)