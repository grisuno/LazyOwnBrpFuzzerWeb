# Subsystem: root

## app.py
- Layer: presentation
- Doc: app.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licenci
- Language: py
- Symbols:
  - `index` (function, line 19) `def index()`
  - `intercept` (function, line 23) `def intercept()`
  - `scan` (function, line 52) `def scan()`
  - `repeater` (function, line 68) `def repeater()`
- Depends on: `lazyown_bprfuzzer.py`

## install.sh
- Layer: utility
- Language: sh

## lazyown_bprfuzzer.py
- Layer: utility
- Doc: main.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: 09/06/2024 Licenc
- Language: py
- Symbols:
  - `load_headers_from_file` (function, line 59) `def load_headers_from_file(file_path)`
  - `load_data_from_file` (function, line 64) `def load_data_from_file(file_path)`
  - `signal_handler` (function, line 69) `def signal_handler(sig, frame)`
  - `ProxyHandler` (class, line 76) `class ProxyHandler(BaseHTTPRequestHandler)`
  - `run_proxy` (method, line 99) `def run_proxy(port)`
  - `edit_file_with_nano` (method, line 105) `def edit_file_with_nano(content)`
  - `send_request` (method, line 114) `def send_request(url, method, headers, params, data, json_data, proxies, hide_code)`
  - `repeater` (method, line 135) `def repeater(url, method, headers, params, data, json_data, proxies, hide_code)`
  - `lazyfuzz` (method, line 165) `def lazyfuzz(url, method, headers, params, data, json_data, proxies, wordlist_path, hide_code)`
  - `parse_arguments` (method, line 210) `def parse_arguments()`
  - `main` (method, line 231) `def main()`
  - `do_GET` (method, line 77) `def do_GET(self)`
  - `do_POST` (method, line 80) `def do_POST(self)`
  - `_handle_request` (method, line 83) `def _handle_request(self, method)`
- Imported by: `app.py`
