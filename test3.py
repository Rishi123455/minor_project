# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:09:10 2018

@author: distroter
"""

from flask import Flask
import requests
from cryptography.fernet import Fernet
CID=input()
PW=input()
key = Fernet.generate_key()
cipher_suite = Fernet(key)
# encoding the password and CustomerID 
encoded_CID = cipher_suite.encrypt(CID.encode('utf-8'))
encoded_PW = cipher_suite.encrypt(PW.encode('utf-8'))
# sending get request
r = requests.post("http://localhost:5000", data={'ECID': encoded_CID,'EPW':encoded_PW,'key':key})
print(r.text)