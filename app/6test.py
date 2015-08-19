from flask import Flask,render_template,request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

#déclare le serveur flask
app = Flask(__name__)
#déclare le plug-in flask-script 
manager = Manager( app)
#déclare le plug-in flask-bootStrap
bootstrap = Bootstrap(app)
#j'instancie le plug-in flask-Nav
nav = Nav()
#je déclare le plug-in dans l'application
nav.init_app(app)

#je déclare une barre de navigation contenant les routes
mynavbar = Navbar(
        'mysite',
        View('Home', 'index'),
        View('1er Exemple', 'hello'),
        View('template Exemple', 'hello2'),
        View('BootStrap Exemple', 'hello3'),
        View('BootStrap et Nav Exemple', 'hello4'),
        
    )


#je donne au plug-in ma barre de navigation
nav.register_element('top', mynavbar)


#crée la route web de la racine du site 
#et la lie à la fonction index
@app.route("/")
def index():
    return render_template('index.html')

#on crée la nouvelle route et on la lie à fonction Hello
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    #if name == None : 
        #Si le nom n'est pas dans l'url, je tente de l'extraire depuis la requête 
    #    name = request.args.get('name',None)
    return render_template('hello.html', name=name)

@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name=None):
    if name == None : 
        #Si le nom n'est pas dans l'url, je tente de l'extraire depuis la requête 
        name = request.args.get('name',None)
    return render_template('hello2.html', name=name)

@app.route('/hello3/')
@app.route('/hello3/<name>')
def hello3(name=None):
    if name == None : 
        #Si le nom n'est pas dans l'url, je tente de l'extraire depuis la requête 
        name = request.args.get('name',None)
    return render_template('hello3.html', name=name)

@app.route('/hello4/')
@app.route('/hello4/<name>')
def hello4(name=None):
    if name == None : 
        #Si le nom n'est pas dans l'url, je tente de l'extraire depuis la requête 
        name = request.args.get('name',None)
    return render_template('hello4.html', name=name)



if __name__ == "__main__":
#lance le serveur Flask via le plug-in flask-script
    manager.run()
    
    