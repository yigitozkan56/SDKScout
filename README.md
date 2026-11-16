# 📦 SDKScout

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB.svg?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg?logo=fastapi&logoColor=white)
![Legal Data Flow](https://img.shields.io/badge/Data%20Flow-Official%20Registries%20%26%20Public%20Manifests-success)

**SDKScout** is an open-source package and dependency intelligence tool that analyzes technology stack trends across `npm`, `PyPI`, `pub.dev`, and public GitHub manifest files (`package.json`, `requirements.txt`, `pubspec.yaml`).

---

## ⚖️ Legal Data Architecture & Compliance (Legal Pivot)

- **Zero Binary Decompilation:** SDKScout **never** decompiles, disassembles, or reverse-engineers proprietary mobile binaries (`.apk` / `.ipa`).
- **100% Open Registry & Manifest Intelligence:** Uses only official public package manager APIs (`registry.npmjs.org`, `pypi.org/pypi/<pkg>/json`, `pub.dev/api/packages`) and public open-source manifest files.
- **Local SQLite Cache:** Stores package metadata and adoption scores locally in `sdkscout_cache.db`.

---

## 📊 Sample Output

```text
Package                    | Registry | Category                   | Version  | Score
--------------------------------------------------------------------------------------
pydantic                   | PyPI     | Data Validation            | 2.9.2    | 98.0/100
fastapi                    | PyPI     | Web API Framework          | 0.115.0  | 96.5/100
@supabase/supabase-js      | npm      | BaaS / Auth & DB           | 2.45.0   | 92.0/100
flutter_riverpod           | pub.dev  | Flutter State Management   | 2.6.1    | 89.4/100
```

| Package | Registry | Category | Latest Version | License | Adoption Score |
| :--- | :---: | :--- | :---: | :---: | :---: |
| `pydantic` | `PyPI` | Data Validation | `2.9.2` | `MIT` | **98.0 / 100** |
| `fastapi` | `PyPI` | Web API Framework | `0.115.0` | `MIT` | **96.5 / 100** |
| `@supabase/supabase-js` | `npm` | BaaS / Auth & DB | `2.45.0` | `MIT` | **92.0 / 100** |
| `flutter_riverpod` | `pub.dev` | Flutter State Management | `2.6.1` | `MIT` | **89.4 / 100** |

---

## 🚀 Step-by-Step Installation

```bash
git clone https://github.com/yigitozkan56/SDKScout.git
cd SDKScout
cp .env.example .env
pip install -r requirements.txt
```

---

## 💻 Usage Examples

### CLI Mode
```bash
# View top SDK adoption trends across npm, PyPI, and pub.dev
python app.py trends

# Inspect a local manifest file (requirements.txt, package.json, or pubspec.yaml)
python app.py inspect-manifest requirements.txt
```

### Web Dashboard & REST API Mode
```bash
python app.py serve --port 8009
```
Visit `http://127.0.0.1:8009` or `POST http://127.0.0.1:8009/api/parse-manifest`.

### Running Unit Tests
```bash
pytest tests/
```

---

## 🗺️ Roadmap

- [x] Multi-ecosystem manifest parser (`package.json`, `requirements.txt`, `pubspec.yaml`)
- [x] SDK category classification & SQLite registry cache
- [x] FastAPI Web UI & CLI inspector
- [ ] Cargo (`Cargo.toml`) and Go (`go.mod`) manifest support
- [ ] SPDX license compatibility matrix for dependency trees
