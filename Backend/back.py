# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:45:04 2023

@author: USER
"""

from flask import Flask, jsonify

app = Flask(__name__)

# Ruta de ejemplo para obtener datos
@app.route('/api/hola', methods=['GET'])
def obtener_hola():
    mensaje = {'mensaje': '¡Hola, esta es mi API en Python!'}
    return jsonify(mensaje)

if __name__ == '__main__':
    app.run(debug=True)