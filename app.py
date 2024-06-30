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

    # Usar la función send_request de lazyown_bprfuzzer para manejar la solicitud
    response = lazyown_bprfuzzer.send_request(target_url, method='POST', headers=headers, data=body)

    if response:
        return jsonify({
            'status': 'success',
            'message': 'Solicitud interceptada',
            'data': {
                'target_url': target_url,
                'headers': headers,
                'body': body,
                'response_status_code': response.status_code,
                'response_headers': dict(response.headers),
                'response_body': response.text
            }
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Error al interceptar la solicitud'
        }), 500

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    scan_url = data.get('scan_url')

    # Simula un escaneo de vulnerabilidades usando lazyown_bprfuzzer
    # Aquí llamamos a la función lazyfuzz para realizar un escaneo básico
    # Nota: Esto es una simplificación, puedes personalizar la llamada según tus necesidades
    results = lazyown_bprfuzzer.lazyfuzz(scan_url, 'GET', {}, {}, {}, {}, None, 'wordlist.txt', None)
    
    return jsonify({
        'status': 'success',
        'message': 'Escaneo completado',
        'data': results
    })

@app.route('/repeater', methods=['POST'])
def repeater():
    data = request.get_json()
    url = data.get('url')
    method = data.get('method', 'GET')
    headers = data.get('headers', {})
    params = data.get('params', {})
    body = data.get('body', {})
    json_data = data.get('json_data', {})
    proxies = None  # Puedes ajustar esto si necesitas un proxy
    hide_code = data.get('hide_code')

    # Usar la función repeater de lazyown_bprfuzzer
    lazyown_bprfuzzer.repeater(url, method, headers, params, body, json_data, proxies, hide_code)
    
    return jsonify({
        'status': 'success',
        'message': 'Repeater en ejecución'
    })

# Uncomment the following lines if you want to run the app locally without Gunicorn
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
