# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `repeater` | 2 | 4 | `app.py`, `lazyown_bprfuzzer.py` |
| `autor` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `com` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `correo` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `creaci` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `descripci` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `dot` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `electr` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `fecha` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `gmail` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `gpl` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `gris` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `grisiscomeback` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `iscomeback` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `licencia` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |
| `nico` | 2 | 2 | `app.py`, `lazyown_bprfuzzer.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `autor` | `depends_on` | `com` | 1.00 |
| `autor` | `depends_on` | `correo` | 1.00 |
| `autor` | `depends_on` | `creaci` | 1.00 |
| `autor` | `depends_on` | `descripci` | 1.00 |
| `autor` | `depends_on` | `dot` | 1.00 |
| `autor` | `depends_on` | `electr` | 1.00 |
| `autor` | `depends_on` | `fecha` | 1.00 |
| `autor` | `depends_on` | `gmail` | 1.00 |
| `autor` | `depends_on` | `gpl` | 1.00 |
| `autor` | `depends_on` | `gris` | 1.00 |
| `autor` | `depends_on` | `grisiscomeback` | 1.00 |
| `autor` | `depends_on` | `iscomeback` | 1.00 |
| `autor` | `depends_on` | `licencia` | 1.00 |
| `autor` | `depends_on` | `nico` | 1.00 |
| `autor` | `depends_on` | `repeater` | 1.00 |
| `com` | `depends_on` | `autor` | 1.00 |
| `com` | `depends_on` | `correo` | 1.00 |
| `com` | `depends_on` | `creaci` | 1.00 |
| `com` | `depends_on` | `descripci` | 1.00 |
| `com` | `depends_on` | `dot` | 1.00 |
| `com` | `depends_on` | `electr` | 1.00 |
| `com` | `depends_on` | `fecha` | 1.00 |
| `com` | `depends_on` | `gmail` | 1.00 |
| `com` | `depends_on` | `gpl` | 1.00 |
| `com` | `depends_on` | `gris` | 1.00 |
| `com` | `depends_on` | `grisiscomeback` | 1.00 |
| `com` | `depends_on` | `iscomeback` | 1.00 |
| `com` | `depends_on` | `licencia` | 1.00 |
| `com` | `depends_on` | `nico` | 1.00 |
| `com` | `depends_on` | `repeater` | 1.00 |
| `correo` | `depends_on` | `autor` | 1.00 |
| `correo` | `depends_on` | `com` | 1.00 |
| `correo` | `depends_on` | `creaci` | 1.00 |
| `correo` | `depends_on` | `descripci` | 1.00 |
| `correo` | `depends_on` | `dot` | 1.00 |
| `correo` | `depends_on` | `electr` | 1.00 |
| `correo` | `depends_on` | `fecha` | 1.00 |
| `correo` | `depends_on` | `gmail` | 1.00 |
| `correo` | `depends_on` | `gpl` | 1.00 |
| `correo` | `depends_on` | `gris` | 1.00 |
| `correo` | `depends_on` | `grisiscomeback` | 1.00 |
| `correo` | `depends_on` | `iscomeback` | 1.00 |
| `correo` | `depends_on` | `licencia` | 1.00 |
| `correo` | `depends_on` | `nico` | 1.00 |
| `correo` | `depends_on` | `repeater` | 1.00 |
| `creaci` | `depends_on` | `autor` | 1.00 |
| `creaci` | `depends_on` | `com` | 1.00 |
| `creaci` | `depends_on` | `correo` | 1.00 |
| `creaci` | `depends_on` | `descripci` | 1.00 |
| `creaci` | `depends_on` | `dot` | 1.00 |

## Dialectic Prompts

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
