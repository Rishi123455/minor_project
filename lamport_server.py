# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:45:48 2018

@author: distrote
"""

from flask import Flask,request,session
point = -1
M=-1
private_key = -1
f=int(455)
ntp = int(455)
d=int(2222)
app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
    c1 = request.form['C1']
    c2 = request.form['C2']
    temp = request.form['temp']
    count = request.form['count']
    point = request.form['point']
    public_key = request.form['public_key']
    print(int(c1))
    print(int (c2))
    print(float(temp))
    print(int(count))
    print(int(point))
    print(int(public_key))  
    print(f)
    global ntp
    print(ntp)
    
    M = int(c2) - int(d) * int(c1)
   
    var = float(temp) - int(d)*int(c1)
   
    ans="-1"
    if int(count) == 1:
        ntp = float(var)
        ans="1"
    else:
        inverse = float((2*float(var)-3-f)/3)
        print("inverse is : {}".format(inverse))
        #print("otp is : {}".format(ntp))
        if inverse == ntp:
                ntp = var
                ans="1"
        else:
            ans="0"
    return  ans

     

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5001)