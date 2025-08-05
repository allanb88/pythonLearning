from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Página de Prueba</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; }
            h1 { color: #333; }
            button { padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <h1>¡Hola desde Flask en WSL!</h1>
        <p>Esta es una página de prueba con algunos elementos HTML básicos.</p>
        <ul>
            <li>Elemento 1</li>
            <li>Elemento 2</li>
            <li>Elemento 3</li>
        </ul>
        <button onclick="alert('¡Hola mundo!')">Haz clic aquí</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

