from flask import Flask, request, render_template
import datetime
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    correo = request.form.get('correo')
    nombre = request.form.get('nombre')
    sector = request.form.get('sector')
    nb = request.form.get('nb')

    ip = request.remote_addr
    navegador = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("registros.txt", "a") as f:
        f.write(f"{timestamp} | IP: {ip} | Navegador: {navegador} | Correo: {correo} | Nombre: {nombre} | Sector: {sector} | NB: {nb}\n")

    return render_template('index.html')

@app.route('/registros')
def ver_registros():
    if os.path.exists("registros.txt"):
        with open("registros.txt", "r") as f:
            contenido = f.read().replace('\n', '<br>')
        return f"<h2>Registros</h2><p>{contenido}</p>"
    else:
        return "No hay registros aún."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
