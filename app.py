from flask import Flask, render_template, request, abort, redirect, url_for
import json

app = Flask(__name__)

def cargar_xxxs():
    with open('xxx.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def root():
    # Redirige al /xxxs
    return redirect(url_for('xxxs'))

@app.route('/xxxs')
def xxxs():
    # Página con logo + formulario búsqueda
    return render_template('xxxs.html')

@app.route('/listaxxxs', methods=['POST'])
def listaxxxs():
    nombre_buscar = request.form.get('nombre', '').strip().lower()
    xxxs = cargar_xxxs()

    if nombre_buscar:
        resultados = [x for x in xxxs if x['nombre'].lower().startswith(nombre_buscar)]
    else:
        resultados = xxxs

    return render_template('listaxxxs.html', xxxs=resultados, busqueda=nombre_buscar)

@app.route('/xxx/<int:id>')
def detalle_xxx(id):
    xxxs = cargar_xxxs()
    # Buscar el elemento con el id
    item = next((x for x in xxxs if x['id'] == id), None)
    if not item:
        abort(404)
    return render_template('xxx.html', item=item)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
