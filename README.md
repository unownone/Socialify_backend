# Socialify Backend

Socialify provides a nearly no code deployable backend solution for a social media esk application. Built on top of python and mongodb it is very flexible and provides functions like user authentication , user data retrieval , user data update and is easily deployable on Heroku with just your own environment variables and as the project is open source , you can just fork it and modify the code as you like it. It is well documented and commented and hence you don't need to worry much!

A sample of the project has been deployed at : https://socialifybackend.herokuapp.com/ 
---
## SETTING UP:
#### To set up the server all you have to do is , clone and create your own repository , go to heroku, create heroku app with pipeline as github and deploy with environment variables: 

'master_key' : Your master key for encryption , keep it hidden and safe as it handles encyrption
'MONGO_URI' : pass your mongo uri with dbname and password . Make sure you pass the password and name too !

#### Modules Used:
- flask
- flask_pymongo
- bcrypt
- dotenv
- virtualenv
- datetime
- secrets

---
### Socialify has predefined methods and the main.py is the flask app class. The api includes:

#### /signup/ ------> POST
Accepts : email,password,username . 
Returns : response: UREGSUCS - If user is registered successfully along with api_key: which gives the api key for that user
          response: UEXISTS - if username/email already exists.

#### /login/ ------> POST
Accepts : email/username,password.
Returns : response: INVALPASS - If the password entered is invalid.
          response: UNOEXIST - If username/email is invalid.
          response: UVAL - User validated along with api_key - which gives the api key for that user.
          

#### /user/modify/ ------> POST
Accepts : api key for a particular account along with old password and new password. Currently only supports password update.
Returns : response: PUPSUCS - Password Update successful.
          response: PNOMAT - old password is incorrect.
          response: PNEWUNV - New password not provided.
          
#### /user/"user_name"/ 
Accepts : Username uri example ```www.api.com/user/kawaiibeans```
Returns : response: **UFOUND** - User found along with **data** - returns user details like profile picture, posts , groups he has joined.
          response: **UNOFOUND** - User doesn't exist.
          
---         
         

