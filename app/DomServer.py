from flask import Flask,render_template,request
from flask.ext.script import Manager
from flask.ext.restful import Resource, Api, abort, fields, marshal_with,marshal,reqparse 

#déclare le serveur flask
app = Flask(__name__)
#déclare le plug-in flask-script 
manager = Manager( app)
api = Api(app)

#crée la route web de la racine du site 
#et la lie à la fonction index
@app.route("/")
def index():
    return "ceci est la page index"

class Node(Resource) : 
    def get(self,nid) : 
        return "<html><H1>ok pour service</H1></html>"
    
    

api.add_resource(Node, '/node/<int:nid>')

if __name__ == "__main__":
#lance le serveur Flask via le plug-in flask-script
    manager.run()
    
    