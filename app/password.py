#THIS Python file helps you hash the passwords safely and store it on MongoDB db for better protection.
#
#please change the master_secret_key to your desired key and do not share it with anybody

from dotenv import load_dotenv
import os
#dotenv is used to pass environment variables 
import bcrypt
#bcrypt provides powerful encryption
import re
#re provides regex
#get_pass returns a hashed password and a salt for that password. 
#for password matching to handle log in , we pass a salt , 
# that comes with the password when it was first hashed and stored. 
# The salt needs to be stored too.
#If a salt is provided the method returns the old salt 
# while if it is not returned it returns a new one
from flask import current_app as app
def get_pass(raw_password,salt=None):
    raw_password=bytes(raw_password,'utf8')
    master_secret_key = bytes(app.config["MASTER_KEY"],'utf8')
    if salt is None:salt = bcrypt.gensalt()
    else: salt=bytes(salt,'utf8')
    combo_password = raw_password + salt + master_secret_key
    hashed_password = bcrypt.hashpw(combo_password, salt)
    return str(hashed_password)[2:62],str(salt)[2:31]

#This is a basic function and returns a empty or non empty string to check the password strength
def check_pass(raw_password):
    return re.search('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})',raw_password)

#The password needs to contain atleast 8 characters , both lowercase and upercase letters and numbers
#if there is no match it returns none 
#else returns a match object