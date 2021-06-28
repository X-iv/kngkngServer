from flask import Flask, Response, redirect, url_for, request, session, abort
import hashlib

#in development not finished



app = Flask(__name__)

# config
app.config.update(DEBUG=True, )


def user(name, username, password):

    #combine username and password for generate id

    #create user display id
    id = hashlib.sha256((name + username + password).encode()).hexdigest()

    #create user token
    token = hashlib.sha256((username + password).encode()).hexdigest()

    #create name with id for search.
    #UNCOMPLETED
    #SAVE ID WITH NAME TO LIST
    #saveName(self.id, self.name)

    return token



#define utf8sb
def utf8(s: bytes):
    return str(s, 'utf-8')

#generate private key
def privateKey(token):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    return private_key



#generate private key
def publicKey(token):
    public_key = private_key.public_key()

def encryptMessage(privateKey):
    pass

def decryptMessage(publicKey):


















#generate private key with token
@app.route("/key", methods=["GET", "POST"])
def key():

        #allowing only post and get request
        if request.method == 'POST' or request.method == 'GET':


                #receive token from form
                token = request.form['token']

                #create user with calling function user.
                if token != "":
                        #return private key
                        return privateKey(token)
                else:
                        #wrong request method
                        return "401"







#register user with arguments
@app.route("/register", methods=["GET", "POST"])
def register():

        #allowing only post and get request
        if request.method == 'POST' or request.method == 'GET':


                #data is form value, not json
                username = request.form['username']
                password = request.form['password']
                name = request.form['name']

                #create user with calling function user.
                if name != "" and username != "" and password != "":

                        #return token to client for in next time generate public and private key.
                        return user(name, username, password)
                else:
                        #wrong request method
                        return "401"





#run in 0.0.0.0 or 127.0.0.1
if __name__ == "__main__":
    app.run(debug=1, host="0.0.0.0")






#message lenght limited with 446 characters
