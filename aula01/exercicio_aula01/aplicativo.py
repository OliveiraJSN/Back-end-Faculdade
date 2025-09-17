from flask import Flask, render_template

app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/times')
def homepage():
    lista_time = ['Palmeiras','Athletico','Coritiba','Parana','Botafogo','Fluminense','Flamengo','Cruzeiro','Fortaleza','Gremio','Inter']
    return render_template('index.html', lista=lista_time)

if __name__ == '__main__':
    app.run(debug=True)
