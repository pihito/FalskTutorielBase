from flask import Flask
#déclare le serveur flask
app = Flask(__name__)

#crée la route web de la racine du site 
#et la lie à la fonction hello
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
#lance le serveur Flask
    app.run(host="0.0.0.0",debug=True)