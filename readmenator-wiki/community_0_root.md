# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `ProxyHandler`, `_handle_request`, `do_GET`, `do_POST`, `edit_file_with_nano`, `index`, `intercept`, `lazyfuzz`. Core file: `lazyown_bprfuzzer.py` (14 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | presentation | 4 | yes |
| `lazyown_bprfuzzer.py` | py | utility | 14 | yes |

## Key Symbols

- `index` (function, `app.py:19`) `def index()`
- `intercept` (function, `app.py:23`) `def intercept()`
- `scan` (function, `app.py:52`) `def scan()`
- `repeater` (function, `app.py:68`) `def repeater()`
- `load_headers_from_file` (function, `lazyown_bprfuzzer.py:59`) `def load_headers_from_file(file_path)`
- `load_data_from_file` (function, `lazyown_bprfuzzer.py:64`) `def load_data_from_file(file_path)`
- `signal_handler` (function, `lazyown_bprfuzzer.py:69`) `def signal_handler(sig, frame)`
- `ProxyHandler` (class, `lazyown_bprfuzzer.py:76`) `class ProxyHandler(BaseHTTPRequestHandler)`
- `do_GET` (method, `lazyown_bprfuzzer.py:77`) `def do_GET(self)`
- `do_POST` (method, `lazyown_bprfuzzer.py:80`) `def do_POST(self)`
- `_handle_request` (method, `lazyown_bprfuzzer.py:83`) `def _handle_request(self, method)`
- `run_proxy` (method, `lazyown_bprfuzzer.py:99`) `def run_proxy(port)`
- `edit_file_with_nano` (method, `lazyown_bprfuzzer.py:105`) `def edit_file_with_nano(content)`
- `send_request` (method, `lazyown_bprfuzzer.py:114`) `def send_request(url, method, headers, params, data, json_data, proxies, hide_co` - Envía una solicitud HTTP y devuelve la respuesta.
- `repeater` (method, `lazyown_bprfuzzer.py:135`) `def repeater(url, method, headers, params, data, json_data, proxies, hide_code)` - Funcionalidad de Repeater que permite enviar solicitudes múltiples veces con posibilidad de modifica
- `lazyfuzz` (method, `lazyown_bprfuzzer.py:165`) `def lazyfuzz(url, method, headers, params, data, json_data, proxies, wordlist_pa` - Funcionalidad de fuzzing que reemplaza LAZYFUZZ con palabras de una wordlist.
- `parse_arguments` (method, `lazyown_bprfuzzer.py:210`) `def parse_arguments()` - Parsear los argumentos de la línea de comandos.
- `main` (method, `lazyown_bprfuzzer.py:231`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 1
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (layer utility) with no import path between community 0 (root) and community 1 (orphans).

## Risks

- [taint medium] `lazyown_bprfuzzer.py` -> `lazyown_bprfuzzer.py` via `requests` (0 hops)
- [taint high] `lazyown_bprfuzzer.py` -> `lazyown_bprfuzzer.py` via `subprocess` (0 hops)

## Open Questions

- Is the dangerous import `requests` in `lazyown_bprfuzzer.py` still required, or can it be isolated?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `lazyown_bprfuzzer.py`
