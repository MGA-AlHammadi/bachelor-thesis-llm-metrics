## Experiment ID: exp02
- **Datum:** 28.09.2025  
- **Datei:** `experiments/more_complex.py`  
- **Beschreibung:** Zwei Funktionen – `foo(x)` (Absolutwert) und `sum_list(lst)` (Summe einer Liste).

### Ergebnisse der Tools (Radon)
- **Cyclomatic Complexity:**  
  - `foo`: 2  
  - `sum_list`: 2  
- **Halstead (gesamt):**  
  - h1 = 6  
  - h2 = 8  
  - N1 = 10  
  - N2 = 12  
  - Vocabulary = 14  
  - Length = 22  
  - Volume ≈ 84  
  - Difficulty ≈ 7.5  
  - Effort ≈ 630  
  - Bugs ≈ 0.028  
- **Maintainability Index:** A (hoch)

### Ergebnisse des LLM (Gemini)
- **Cyclomatic Complexity:**  
  - `foo`: 2  
  - `sum_list`: 2  
- **Halstead:**  
  - Volume ≈ 144.4  
  - Difficulty ≈ 12.86  
  - Effort ≈ 1857  
  - Bugs ≈ 0.048  
- **Maintainability Index:** ~62.5 (laut Formel → „schwer wartbar“, praktisch aber sehr gut wartbar → Artefakt)  
- **Code Smells:**  
  - Unkommunikative Namen (`foo`, `lst`)  
  - Reinventing the wheel (Neuschreiben von `abs()` und `sum()`)  
  - Fehlende Docstrings  
- **Verbesserungsvorschläge:**  
  - Namen verbessern (`get_absolute_value`, `calculate_sum`)  
  - Eingebaute Funktionen `abs()` und `sum()` nutzen  
  - Docstrings + Typannotationen hinzufügen

### Vergleich & Analyse
| Metrik                  | Radon (Tool)     | LLM (Gemini)         | Bemerkung |
|--------------------------|------------------|----------------------|-----------|
| Cyclomatic Complexity    | 2 / 2            | 2 / 2                | ✅ identisch |
| Halstead Volume          | ~84              | ~144                 | ❌ Abweichung |
| Difficulty               | ~7.5             | ~12.9                | ❌ Abweichung |
| Effort                   | ~630             | ~1857                | ❌ Abweichung |
| Maintainability Index    | A (hoch)         | ~62.5 (formal)       | ❌ starke Abweichung (LLM diskutiert Limit der Formel) |
| Verbesserungsvorschläge  | –                | ✅ konkret (Namen, Built-ins, Docstrings) | Mehrwert vom LLM |

### Fazit
- Radon liefert **präzise numerische Werte** und zeigt, dass der Code klein und wartbar ist.  
- Gemini berechnet ähnliche Metriken, kommt aber bei Halstead und MI auf deutlich andere Zahlen.  
- **Mehrwert des LLM:** qualitative Analyse, Hinweis auf Code Smells, konkrete Vorschläge zur Verbesserung.  
- **Erkenntnis:**
