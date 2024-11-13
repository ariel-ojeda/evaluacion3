from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        # Procesamiento de datos del formulario
        notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
        asistencia = float(request.form['asistencia'])
        promedio = sum(notas) / len(notas)
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre = None
    longitud = None
    if request.method == 'POST':
        # Procesamiento de datos del formulario
        nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
        nombre = max(nombres, key=len)
        longitud = len(nombre)
    return render_template('ejercicio2.html', nombre=nombre, longitud=longitud)

if __name__ == '__main__':
    app.run(debug=True)

