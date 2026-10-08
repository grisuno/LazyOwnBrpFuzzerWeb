# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `repeater` | files=2 | mentions=4 | `app.py`, `lazyown_bprfuzzer.py`
- `autor` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `com` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `correo` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `creaci` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `descripci` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `dot` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `electr` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `fecha` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `gmail` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `gpl` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `gris` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `grisiscomeback` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `iscomeback` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `licencia` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`
- `nico` | files=2 | mentions=2 | `app.py`, `lazyown_bprfuzzer.py`

## Verb Edges

- `autor` --depends_on--> `com` (strength 1.00)
- `autor` --depends_on--> `correo` (strength 1.00)
- `autor` --depends_on--> `creaci` (strength 1.00)
- `autor` --depends_on--> `descripci` (strength 1.00)
- `autor` --depends_on--> `dot` (strength 1.00)
- `autor` --depends_on--> `electr` (strength 1.00)
- `autor` --depends_on--> `fecha` (strength 1.00)
- `autor` --depends_on--> `gmail` (strength 1.00)
- `autor` --depends_on--> `gpl` (strength 1.00)
- `autor` --depends_on--> `gris` (strength 1.00)
- `autor` --depends_on--> `grisiscomeback` (strength 1.00)
- `autor` --depends_on--> `iscomeback` (strength 1.00)
- `autor` --depends_on--> `licencia` (strength 1.00)
- `autor` --depends_on--> `nico` (strength 1.00)
- `autor` --depends_on--> `repeater` (strength 1.00)
- `com` --depends_on--> `autor` (strength 1.00)
- `com` --depends_on--> `correo` (strength 1.00)
- `com` --depends_on--> `creaci` (strength 1.00)
- `com` --depends_on--> `descripci` (strength 1.00)
- `com` --depends_on--> `dot` (strength 1.00)
- `com` --depends_on--> `electr` (strength 1.00)
- `com` --depends_on--> `fecha` (strength 1.00)
- `com` --depends_on--> `gmail` (strength 1.00)
- `com` --depends_on--> `gpl` (strength 1.00)
- `com` --depends_on--> `gris` (strength 1.00)
- `com` --depends_on--> `grisiscomeback` (strength 1.00)
- `com` --depends_on--> `iscomeback` (strength 1.00)
- `com` --depends_on--> `licencia` (strength 1.00)
- `com` --depends_on--> `nico` (strength 1.00)
- `com` --depends_on--> `repeater` (strength 1.00)
- `correo` --depends_on--> `autor` (strength 1.00)
- `correo` --depends_on--> `com` (strength 1.00)
- `correo` --depends_on--> `creaci` (strength 1.00)
- `correo` --depends_on--> `descripci` (strength 1.00)
- `correo` --depends_on--> `dot` (strength 1.00)
- `correo` --depends_on--> `electr` (strength 1.00)
- `correo` --depends_on--> `fecha` (strength 1.00)
- `correo` --depends_on--> `gmail` (strength 1.00)
- `correo` --depends_on--> `gpl` (strength 1.00)
- `correo` --depends_on--> `gris` (strength 1.00)
- `correo` --depends_on--> `grisiscomeback` (strength 1.00)
- `correo` --depends_on--> `iscomeback` (strength 1.00)
- `correo` --depends_on--> `licencia` (strength 1.00)
- `correo` --depends_on--> `nico` (strength 1.00)
- `correo` --depends_on--> `repeater` (strength 1.00)
- `creaci` --depends_on--> `autor` (strength 1.00)
- `creaci` --depends_on--> `com` (strength 1.00)
- `creaci` --depends_on--> `correo` (strength 1.00)
- `creaci` --depends_on--> `descripci` (strength 1.00)
- `creaci` --depends_on--> `dot` (strength 1.00)

## Dialectic

- Thesis: `autor` centralizes 2 files; Antithesis: `com` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `correo` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `creaci` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `descripci` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `dot` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `electr` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `fecha` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `gmail` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `gpl` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `autor` centralizes 2 files; Antithesis: `gris` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
