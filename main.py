from flask import Flask
app = Flask('app')

@app.route('/')
def unifran():
  return '<h1>Minha Primeira Rota!</h1>'
     
@app.route('/unifran')
def unifran2():
       return '<h2> Universidade de Franca </h2>'
        
app.run(host='0.0.0.0', port=8080)