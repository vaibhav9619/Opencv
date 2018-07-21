from flask import Flask,request
from pymessenger.bot import Bot
from utils import wit_res
bot=Bot("EAADLsi0eHJwBAOszvgxpgmkVeWD4lkzy0LrvgZAjF2nKq0KM0ptZChcbw7P3hDGqipmuJWbZANk8QbeV1oeJ12jC25yqFdQm9KN6a2bQwQA6qQ978eMgop5wjrdep7jkLlo5SZCY8fkZBs0FGeLFoZCa98PLSHYDtg8Oq27ZBLLggZDZD")
newapp=Flask(__name__)
@newapp.route("/",methods=["GET"])
def veri():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else:
        return "Please Run bro Otherwise i wll hit u(VERIFIED)"
@newapp.route("/",methods=["POST"])
def msg1():
    data=request.get_json()
    print(data)
    for en in data["entry"]:
        for messaging in en["messaging"]:
            text=(messaging["message"]["text"])
            user=(messaging["sender"]["id"])

            response=None
            entity,value=wit_res(text)
            if entity == 'newstype':
                response="Ok i ll send  you {} news ".format(str(value))
            elif entity == 'location':
                response="Ok , So u live in {0}. I will send u headlines from {0}".format(str(value))

            elif entity=='message_body':
                response="sadana.vaibhav@gmail.com".format(str(value))

            if response == None:
                response="Sorry i didn't Understand"
            bot.send_text_message(user,response)

    return "Message revieved"
@newapp.after_request# for clearing previous cache
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
# newapp.run(debug=True)



