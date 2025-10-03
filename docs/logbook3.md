# Logbook – Experiment 3

## Experiment ID: exp03
- **Datum:** 03.10.2025  
- **Datei:** `experiments/complex_example.py`  
- **Beschreibung:** Drei Funktionen –  
  - `process_numbers`: summiert gerade Zahlen, subtrahiert ungerade Zahlen, mit Try/Except.  
  - `factorial`: iterative Fakultät mit Fehlerbehandlung.  
  - `find_max`: findet den Maximalwert in einer Liste.  

---

## Ergebnisse der Tools (Radon)
- **Cyclomatic Complexity:**  
  - `process_numbers`: A (sehr niedrig)  
  - `factorial`: A  
  - `find_max`: A  

- **Halstead-Metriken (gesamt):**  
  - h1 = 8  
  - h2 = 12  
  - N1 = 10  
  - N2 = 19  
  - Vocabulary = 20  
  - Length = 29  
  - Calculated Length ≈ 67.0  
  - Volume ≈ 125.3  
  - Difficulty ≈ 6.33  
  - Effort ≈ 793.8  
  - Time ≈ 44.1  
  - Bugs ≈ 0.042  

- **Maintainability Index:** A (hoch)  

---

## Ergebnisse des LLM (Gemini)
- **Cyclomatic Complexity:**  
  - `process_numbers`: 4  
  - `factorial`: 3  
  - `find_max`: 4  

- **Halstead (geschätzt):**  
  - Volume: ~350–450  
  - Difficulty: ~15–20  
  - Effort: ~5.000–9.000  
  - Bugs: ~0.12–0.15  

- **Maintainability Index:** ~85–95 (exzellent wartbar)  

- **Code Smells:**  
  - Reinventing the wheel (`find_max` statt `max()`)  
  - Broad Exception Handling (`except TypeError` in `process_numbers`)  
  - Inefficient Slicing (`numbers[1:]` erzeugt Kopie)  
  - Fehlende Docstrings in allen Funktionen  

- **Verbesserungsvorschläge:**  
  - Explizite Typprüfung + Generator Expressions in `process_numbers`  
  - Nutzung von `math.factorial()` statt eigener Implementierung  
  - Nutzung von `max()` statt manueller Schleife  
  - Docstrings und Typannotationen hinzufügen  

---

## Vergleich & Analyse
| Metrik                  | Radon (Tool)       | LLM (Gemini)            | Bemerkung |
|--------------------------|--------------------|-------------------------|-----------|
| Cyclomatic Complexity    | Alle A (niedrig)   | 3–4 pro Funktion        | ✅ konsistent (sehr niedrig) |
| Halstead Volume          | ~125               | ~350–450                | ❌ starke Abweichung |
| Difficulty               | ~6.3               | ~15–20                  | ❌ Abweichung |
| Effort                   | ~794               | ~5.000–9.000            | ❌ starke Abweichung |
| Maintainability Index    | A (hoch)           | ~85–95 (hoch)           | ✅ ähnliche Aussage |
| Verbesserungsvorschläge  | –                  | ✅ konkrete Ideen        | Mehrwert vom LLM |

---

## Fazit
- **Radon**: liefert präzise numerische Metriken → bestätigt einfache Struktur und hohe Wartbarkeit.  
- **Gemini**: bestätigt ebenfalls geringe Komplexität & hohe Wartbarkeit, überschätzt aber Halstead-Werte deutlich.  
- **Mehrwert des LLM:** erkennt semantische Probleme (Code Smells) und schlägt konkrete Refactorings vor.  
- **Erkenntnis:** Kombination von Tool + LLM liefert sowohl quantitative Genauigkeit als auch qualitative Verbesserungsvorschläge.  
