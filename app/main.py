#MODULE IMPORTS

from flask import Flask,jsonify,request,render_template
from flask_pymongo import PyMongo
import secrets
from .config import Config
from .password import get_pass,check_pass
from datetime import datetime
from .helpers import objidconv


app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app)

user_db=mongo.db.user.user_data
media_db=mongo.db.media

########################################
########################################
#############BASIC######################
########################################
@app.route('/')
def base():
    return render_template("index.html")
########################################
#############USER MANAGEMENT############
########################################

####USER SIGN UP #########
@app.route('/signup/',methods=['POST'])
def signup():
    data=request.json
    user_exists = user_db.find_one({"$or":[{"email":data['email']},{"username":data['username']}]})

    if user_exists is None:
        key = secrets.token_urlsafe(10) #generates api key
        while user_db.find_one({'api_key':'key'}) is not None:
            key = secrets.token_urlsafe(10)
        #checks if unique
        
        #if not check_pass(data['password']): return jsonify(response='INVALPASS')
        if not user_db.find_one({'uname':data['username']}) is None:
            return jsonify(response='UEXISTS')
        #checks if password is strong enough , else returns false
        password,salt=get_pass(data['password'])
        #gets the salt , and hashed password
        user_db.insert_one({"email":data['email'],"uname":data['username'],"profile_pic":None,"password":password,"api_key":key,"posts":[],"groups":[],"salt":salt,"last_login":datetime.now()})
        #inserts the data into user array , ie user has been registered
        return jsonify(response='UREGSUCS',api_key=key)        
    else: 
        return jsonify(response='UEXISTS')


######USER LOG IN:
@app.route('/login/',methods=['POST'])
def login():
    data=request.json
    pass_check=data['pass']
    if data['username'] is None: data['username']=''
    if data['email'] is None:data['email']=''
    user_check=user_db.find_one({"$or": [{'uname':data['username']},{'email':data['email']}]})
    if user_check is not None:
        pass_check,salt=get_pass(pass_check,user_check['salt'])
        if pass_check==user_check['password']:
            user_db.find_one_and_update({"uname":data['username']},{"last_login":datetime.now()})
            return jsonify(response='UVAL',api_key=user_check['api_key'])
        else: return jsonify(response='INVALPASS')
    else: return jsonify(response='UNOEXIST')
#####################################
########USER AUTH BLOCK FINISHED####
####################################

###################################
########USER UPDATE BLOCK##########
##################################

@app.route('/user/modify/',methods=['POST'])
def update():
    data=request.json
    db=user_db.find_one({'api_key':data['api_key']})
    if data['api_key'] is not None:
        if data['new_pass'] is not None:
            if get_pass(data['old_pass'],db['salt'])[0]==db['password']:
                user_db.update_one({'api_key':data['api_key']},{'password':data['new_pass']})
                return jsonify(response='PUPSUCS')
            else: return jsonify(response='PNOMAT')
        else: return jsonify(response='PNEWUNV')
    else: return jsonify(response='NOAPIKEY')

#################################
##########USER FETCHING API######
#################################

@app.route('/user/<uname>/')
def fetch_user(uname):
    user_val = user_db.find_one({"uname":uname})
    if user_val is not None:
        return jsonify(response='UFOUND',data=objidconv(user_val))
    else: return jsonify(response='UNOFOUND')
#################################
##########END OF USER BLOCK######
#################################

