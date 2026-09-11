# API

## app.py

### index (function) `def index()`
- Defined: `app.py:19`
- Depends on: `lazyown_bprfuzzer.py`

### intercept (function) `def intercept()`
- Defined: `app.py:23`
- Depends on: `lazyown_bprfuzzer.py`

### scan (function) `def scan()`
- Defined: `app.py:52`
- Depends on: `lazyown_bprfuzzer.py`

### repeater (function) `def repeater()`
- Defined: `app.py:68`
- Depends on: `lazyown_bprfuzzer.py`

## lazyown_bprfuzzer.py

### load_headers_from_file (function) `def load_headers_from_file(file_path)`
- Defined: `lazyown_bprfuzzer.py:59`
- Imported by: `app.py`

### load_data_from_file (function) `def load_data_from_file(file_path)`
- Defined: `lazyown_bprfuzzer.py:64`
- Imported by: `app.py`

### signal_handler (function) `def signal_handler(sig, frame)`
- Defined: `lazyown_bprfuzzer.py:69`
- Imported by: `app.py`

### run_proxy (method) `def run_proxy(port)`
- Defined: `lazyown_bprfuzzer.py:99`
- Imported by: `app.py`

### edit_file_with_nano (method) `def edit_file_with_nano(content)`
- Defined: `lazyown_bprfuzzer.py:105`
- Imported by: `app.py`

### send_request (method) `def send_request(url, method, headers, params, data, json_data, proxies, hide_code)`
- Defined: `lazyown_bprfuzzer.py:114`
- Doc: Envía una solicitud HTTP y devuelve la respuesta.
- Imported by: `app.py`

### repeater (method) `def repeater(url, method, headers, params, data, json_data, proxies, hide_code)`
- Defined: `lazyown_bprfuzzer.py:135`
- Doc: Funcionalidad de Repeater que permite enviar solicitudes múltiples veces con posibilidad de modificación.
- Imported by: `app.py`

### lazyfuzz (method) `def lazyfuzz(url, method, headers, params, data, json_data, proxies, wordlist_path, hide_code)`
- Defined: `lazyown_bprfuzzer.py:165`
- Doc: Funcionalidad de fuzzing que reemplaza LAZYFUZZ con palabras de una wordlist.
- Imported by: `app.py`

### parse_arguments (method) `def parse_arguments()`
- Defined: `lazyown_bprfuzzer.py:210`
- Doc: Parsear los argumentos de la línea de comandos.
- Imported by: `app.py`

### main (method) `def main()`
- Defined: `lazyown_bprfuzzer.py:231`
- Imported by: `app.py`

### do_GET (method) `def do_GET(self)`
- Defined: `lazyown_bprfuzzer.py:77`
- Imported by: `app.py`

### do_POST (method) `def do_POST(self)`
- Defined: `lazyown_bprfuzzer.py:80`
- Imported by: `app.py`

### _handle_request (method) `def _handle_request(self, method)`
- Defined: `lazyown_bprfuzzer.py:83`
- Imported by: `app.py`
