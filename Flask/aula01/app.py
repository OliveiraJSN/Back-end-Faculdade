from flask import Flask, render_template

app = Flask(__name__, template_folder='templates',static_folder='static')

@app.route('/inicio')
def homepage():
    mensagem = 'Hello World'
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)


