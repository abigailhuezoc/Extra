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
        'id': 103,'titulo': 'Architechture Patterns','autor': 'Erich Gamma','disponible': True}
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
                    ]
                }
            )



if __name__ == '__main__':
    app.run(debug=True)