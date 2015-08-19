from flask import Flask
from flask.ext.script import Manager

#déclare le serveur flask
app = Flask(__name__)
#déclare le plug-in flask-script 
manager = Manager( app)


#crée la route web de la racine du site 
#et la lie à la fonction hello
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
#lance le serveur Flask via le plug-in flask-script
    manager.run()