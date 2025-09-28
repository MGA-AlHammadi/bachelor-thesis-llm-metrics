# Logbook – Bachelorarbeit LLM & Softwaremetriken

Dieses Logbuch dokumentiert die praktischen Experimente im Rahmen der Bachelorarbeit.  
Struktur: Jede Analyse enthält Informationen zum Code, den Ergebnissen der Tools (z. B. Radon, ESLint, SonarQube) und zum Vergleich mit LLM-Ausgaben (z. B. Gemini, GPT).

---

## Experiment ID: exp01
- **Datum:** 21.09.2025  
- **Datei:** `experiments/example.py`  
- **Beschreibung:** Einfache Funktion `foo(x)` mit if-else zur Berechnung des Absolutwertes.

### Ergebnisse der Tools (Radon)
- **Cyclomatic Complexity:** 2  
- **Halstead:**  
  - h1 = 2  
  - h2 = 2  
  - N1 = 2  
  - N2 = 3  
  - Vocabulary = 4  
  - Length = 5  
  - Volume = 10.0  
  - Difficulty = 1.5  
  - Effort = 15.0  
  - Bugs = 0.0033  
- **Maintainability Index:** A (hoch)

### Ergebnisse des LLM (Gemini)
- **Cyclomatic Complexity (Schätzung):** 2  
- **Halstead (ungefähr):** Volume = 6, Difficulty = 1.5, Effort = 9  
- **Maintainability Index:** ≈ 100 (hoch)  
- **Code Smells:** Keine  
- **Verbesserungsvorschläge:**  
  - Nutzung von `abs(x)` anstelle der if-else-Struktur  
  - Bessere Funktionsnamen vorschlagen  
  - Docstring hinzufügen

### Vergleich & Analyse
| Metrik                  | Radon (Tool) | LLM (Gemini) | Bemerkung |
|--------------------------|--------------|--------------|-----------|
| Cyclomatic Complexity    | 2            | 2            | ✅ identisch |
| Halstead Volume          | 10.0         | 6            | ❌ Abweichung |
| Difficulty               | 1.5          | 1.5          | ✅ identisch |
| Effort                   | 15.0         | 9            | ❌ Abweichung |
| Maintainability Index    | A (hoch)     | ≈ 100 (hoch) | ✅ ähnliche Aussage |
| Verbesserungsvorschläge  | –            | ✅ abs(), Docstring, Name | Mehrwert vom LLM |

### Fazit
Das LLM konnte die **Cyclomatic Complexity korrekt** einschätzen und zusätzlich **konkrete Verbesserungen** vorschlagen.  
Bei den Halstead-Metriken zeigten sich Abweichungen, was auf Grenzen der LLM-Analyse hinweist.  
**Mehrwert:** qualitative Vorschläge und bessere Verständlichkeit für Entwickler:innen.

---

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
