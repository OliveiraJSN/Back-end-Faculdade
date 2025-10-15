from flask import Flask
from flask import render_template 
from flask import request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET','POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        op = request.form['op']

        if op == 'soma':
            resultado = round(n1 + n2)
        elif op == 'subtracao':
            resultado = round(n1 - n2)
        elif op == 'mult':
            resultado = round(n1 * n2)
        elif op == 'divisao':
            resultado = {
                round(n1 / n2)
                if n2 != 0
                else "Erro: divisão por 0 não é possivel!"
            }

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
