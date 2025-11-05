
#Examen Unidad III
#Autor: Alexander Soto Antunez
#Fecha: 05/11/25

from flask import Flask, request

app = Flask(__name__)

dispositivos = {}

@app.route('/dispositivos_mostrar', methods=['GET'])
def mostrar_dispositivos_html():
    html = """
    <html>
    <head>
        <title>Dispositivos de red</title>
    </head>
    <body>
        <h2>Lista de dispositivos</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Descripción</th>
                    <th>IP</th>
                    <th>MAC</th>
                    <th>Ubicación</th>
                    <th>Tipo</th>
                    <th>Otros</th>
                </tr>
            </thead>
            <tbody>
    """
    for dispositivo_id, dispositivo in dispositivos.items():
        html += f"""
            <tr>
                <td>{dispositivo_id}</td>
                <td>{dispositivo['nombre']}</td>
                <td>{dispositivo['descripcion']}</td>
                <td>{dispositivo['ip']}</td>
                <td>{dispositivo['mac']}</td>
                <td>{dispositivo['ubicacion']}</td>
                <td>{dispositivo['tipo']}</td>
                <td>{dispositivo['otros']}</td>
            </tr>
        """
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(debug=True)