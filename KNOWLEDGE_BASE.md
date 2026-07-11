# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 3 | **Total Symbols Extracted:** 18 | **Total Imports:** 11

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    lazyown_bprfuzzer_py["lazyown_bprfuzzer.py (py)"]
    class lazyown_bprfuzzer_py mod;
    lazyown_bprfuzzer_py_load_headers_from_file["load_headers_from_file"]
    class lazyown_bprfuzzer_py_load_headers_from_file fn;
    lazyown_bprfuzzer_py --> lazyown_bprfuzzer_py_load_headers_from_file
    lazyown_bprfuzzer_py_load_data_from_file["load_data_from_file"]
    class lazyown_bprfuzzer_py_load_data_from_file fn;
    lazyown_bprfuzzer_py --> lazyown_bprfuzzer_py_load_data_from_file
    lazyown_bprfuzzer_py_signal_handler["signal_handler"]
    class lazyown_bprfuzzer_py_signal_handler fn;
    lazyown_bprfuzzer_py --> lazyown_bprfuzzer_py_signal_handler
    lazyown_bprfuzzer_py_ProxyHandler["ProxyHandler"]
    class lazyown_bprfuzzer_py_ProxyHandler cls;
    lazyown_bprfuzzer_py --> lazyown_bprfuzzer_py_ProxyHandler
    lazyown_bprfuzzer_py_run_proxy["run_proxy"]
    class lazyown_bprfuzzer_py_run_proxy fn;
    lazyown_bprfuzzer_py --> lazyown_bprfuzzer_py_run_proxy
    app_py["app.py (py)"]
    class app_py mod;
    app_py_index["index"]
    class app_py_index fn;
    app_py --> app_py_index
    app_py_intercept["intercept"]
    class app_py_intercept fn;
    app_py --> app_py_intercept
    app_py_scan["scan"]
    class app_py_scan fn;
    app_py --> app_py_scan
    app_py_repeater["repeater"]
    class app_py_repeater fn;
    app_py --> app_py_repeater
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_flask["flask"]
    class ext_flask ext;
    app_py -.->|imports| ext_flask
    ext_lazyown_bprfuzzer["lazyown_bprfuzzer"]
    class ext_lazyown_bprfuzzer ext;
    app_py -.->|imports| ext_lazyown_bprfuzzer
    ext_argparse["argparse"]
    class ext_argparse ext;
    lazyown_bprfuzzer_py -.->|imports| ext_argparse
    ext_json["json"]
    class ext_json ext;
    lazyown_bprfuzzer_py -.->|imports| ext_json
    ext_requests["requests"]
    class ext_requests ext;
    lazyown_bprfuzzer_py -.->|imports| ext_requests
    ext_signal["signal"]
    class ext_signal ext;
    lazyown_bprfuzzer_py -.->|imports| ext_signal
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    lazyown_bprfuzzer_py -.->|imports| ext_subprocess
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    lazyown_bprfuzzer_py -.->|imports| ext_tempfile
    ext_threading["threading"]
    class ext_threading ext;
    lazyown_bprfuzzer_py -.->|imports| ext_threading
    ext_os["os"]
    class ext_os ext;
    lazyown_bprfuzzer_py -.->|imports| ext_os
    ext_http_server["http.server"]
    class ext_http_server ext;
    lazyown_bprfuzzer_py -.->|imports| ext_http_server
```

---

## Architecture Reference

### PY (2 files)

#### `app.py`
**Path:** `app.py`

**Functions:**
- `index` (line 19)
- `intercept` (line 23)
- `scan` (line 52)
- `repeater` (line 68)

#### `lazyown_bprfuzzer.py`
**Path:** `lazyown_bprfuzzer.py`

**Classs:**
- `ProxyHandler` (line 76)

**Functions:**
- `load_headers_from_file` (line 59)
- `load_data_from_file` (line 64)
- `signal_handler` (line 69)
- `run_proxy` (line 99)
- `edit_file_with_nano` (line 105)
- `send_request` (line 114) - *Envía una solicitud HTTP y devuelve la respuesta.*
- `repeater` (line 135) - *Funcionalidad de Repeater que permite enviar solicitudes múltiples veces con posibilidad de modificación.*
- `lazyfuzz` (line 165) - *Funcionalidad de fuzzing que reemplaza LAZYFUZZ con palabras de una wordlist.*
- `parse_arguments` (line 210) - *Parsear los argumentos de la línea de comandos.*
- `main` (line 231)
- `do_GET` (line 77)
- `do_POST` (line 80)
- `_handle_request` (line 83)

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
