# API

## app.py
Depends on: `lazyown_bprfuzzer.py`
- `index` (function) `app.py:19` `def index()`
- `intercept` (function) `app.py:23` `def intercept()`
- `scan` (function) `app.py:52` `def scan()`
- `repeater` (function) `app.py:68` `def repeater()`

## lazyown_bprfuzzer.py
Imported by: `app.py`
- `load_headers_from_file` (function) `lazyown_bprfuzzer.py:59` `def load_headers_from_file(file_path)`
- `load_data_from_file` (function) `lazyown_bprfuzzer.py:64` `def load_data_from_file(file_path)`
- `signal_handler` (function) `lazyown_bprfuzzer.py:69` `def signal_handler(sig, frame)`
- `ProxyHandler.do_GET` (method) `lazyown_bprfuzzer.py:77` `def do_GET(self)`
- `ProxyHandler.do_POST` (method) `lazyown_bprfuzzer.py:80` `def do_POST(self)`
- `ProxyHandler.run_proxy` (method) `lazyown_bprfuzzer.py:99` `def run_proxy(port)`
- `ProxyHandler.edit_file_with_nano` (method) `lazyown_bprfuzzer.py:105` `def edit_file_with_nano(content)`
- `ProxyHandler.send_request` (method) `lazyown_bprfuzzer.py:114` `def send_request(url, method, headers, params, data, json_data, proxies, hide_code)` -- Envía una solicitud HTTP y devuelve la respuesta.
- `ProxyHandler.repeater` (method) `lazyown_bprfuzzer.py:135` `def repeater(url, method, headers, params, data, json_data, proxies, hide_code)` -- Funcionalidad de Repeater que permite enviar solicitudes múltiples veces con posibilidad de modificación.
- `ProxyHandler.lazyfuzz` (method) `lazyown_bprfuzzer.py:165` `def lazyfuzz(url, method, headers, params, data, json_data, proxies, wordlist_path, hide_code)` -- Funcionalidad de fuzzing que reemplaza LAZYFUZZ con palabras de una wordlist.
- `ProxyHandler.parse_arguments` (method) `lazyown_bprfuzzer.py:210` `def parse_arguments()` -- Parsear los argumentos de la línea de comandos.
- `ProxyHandler.main` (method) `lazyown_bprfuzzer.py:231` `def main()`
