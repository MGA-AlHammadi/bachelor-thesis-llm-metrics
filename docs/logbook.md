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
