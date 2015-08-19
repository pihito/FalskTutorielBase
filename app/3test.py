from flask import Flask,render_template,request
from flask.ext.script import Manager

#déclare le serveur flask
app = Flask(__name__)
#déclare le plug-in flask-script 
manager = Manager( app)


#crée la route web de la racine du site 
#et la lie à la fonction index
@app.route("/")
def index():
    return "ceci est la page index"

#on crée la nouvelle route et on la lie à fonction Hello
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name == None : 
        #Si le nom n'est pas dans l'url, je tente de l'extraire depuis la requête 
        name = request.args.get('name',None)
    return render_template('hello.html', name=name)

if __name__ == "__main__":
#lance le serveur Flask via le plug-in flask-script
    manager.run()
    
    