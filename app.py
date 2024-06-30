#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
app.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: xx/xx/xxxx
Licencia: GPL v3

Descripción:  
"""
from flask import Flask, render_template, request, jsonify
import lazyown_bprfuzzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('burp.html')

@app.route('/intercept', methods=['POST'])
def intercept():
    data = request.get_json()
    target_url = data.get('target_url')
    headers = data.get('headers')
    body = data.get('body')

    # Aquí puedes usar funciones de lazyown_bprfuzzer para manejar la solicitud
    # response = lazyown_bprfuzzer.some_function(target_url, headers, body)

    return jsonify({
        'status': 'success',
        'message': 'Solicitud interceptada',
        'data': {
            'target_url': target_url,
            'headers': headers,
            'body': body
        }
    })

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    scan_url = data.get('scan_url')

    # Simula un escaneo de vulnerabilidades usando lazyown_bprfuzzer
    # results = lazyown_bprfuzzer.scan_function(scan_url)
    
    results = {
        'vulnerabilities': [
            'XSS Reflejado en el parámetro \'q\' de la página de búsqueda',
            'Posible inyección SQL en el formulario de inicio de sesión',
            'Versión desactualizada de OpenSSL (CVE-2023-0286)'
        ]
    }

    return jsonify({
        'status': 'success',
        'message': 'Escaneo completado',
        'data': results
    })

if __name__ == '__main__':
    app.run(debug=True)
