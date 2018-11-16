# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:37:20 2018

@author: distroter
"""
import pyotp,time
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
totp.at(time.time(),1)
totp.now()
str=totp.now()
time.sleep(16)
totp.verify(str)
