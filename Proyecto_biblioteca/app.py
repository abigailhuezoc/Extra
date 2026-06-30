from flask import Flask, jsonify, request

app = Flask(__name__)

#Repositorio temporal de datos
#no representa persistencia de datos


libros = {
    101: {
        'id': 101,'titulo': 'Clean Code','autor': 'Robert C. Martin','disponible': True
    },
    102: {
        'id': 102,'titulo': 'Python Crash Course','autor': 'Eric Matthes','disponible': True
    },
    103: {
        'id': 103,'titulo': 'Architechture Patterns','autor': 'GoF','disponible': False}
}
 
@app.get('/')
def inicio():
    return jsonify({'mensaje': 'API REST de Biblioteca Universitaria',
                    'version': '1.0',
                    'endpoints': [
                        'GET/libros', #Muestra todos los libros
                        'GET/libros/<id>', #Muestra un libro específico
                        'POST/libros', #Agrega un libro
                        'PUT/libros/<id>', #Actualiza o modifica un libro
                        'DELETE/libros/<id>' #Borra un libro
                    ],
                    'mensaje': 'API REST de Biblioteca Universitaria',
                    'version': '1.0',
                }
            )

@app.get('/libros')
def obtener_libros():
    return jsonify(list(libros.values()))

@app.get('/libros/<int:id>')
def obtener_libro(id):
    libro = libros.get(id)

    if libro:
        return jsonify(libro)
    
    return jsonify({'error': 'Libro no encontrado'}), 404

@app.post('/libros')
def agregar_libro():
    datos = request.get_json()
    if not datos:
        return jsonify({'error': 'Debe enviar informacion'}), 400
    if 'titulo' not in datos or 'autor' not in datos or 'disponible' not in datos:
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    nuevo_id = max(libros.keys()) + 1

    libro[nuevo_id] = {
        'id': nuevo_id,
        'titulo': datos['titulo'],
        'autor': datos['autor'],
        'disponible': datos['disponible']
    }
    return jsonify(libros[nuevo_id]), 201

if __name__ == '__main__':
    app.run(debug=True)