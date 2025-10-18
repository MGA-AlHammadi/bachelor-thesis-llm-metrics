# Logbook 9 – Vergleich der Analysetools (Radon vs Gemini vs SonarQube)

## 1. Ziel
Ziel dieses Logbuchs ist es, die Ergebnisse der drei Analysetools **Radon**, **Gemini (LLM)** und **SonarQube** auf denselben Python-Code (`github_dijkstra.py`) systematisch zu vergleichen.  
Der Fokus liegt auf der Bewertung der **Analyse-Tiefe**, **Erkennungsqualität** und **praktischen Nützlichkeit** der Metriken und Befunde.

---

## 2. Überblick über den analysierten Code

Untersucht wurde der **Dijkstra-Algorithmus** in einer Python-Implementierung, die absichtlich verschiedene „Code Smells“ und ineffiziente Strukturen enthält, um das Verhalten der Tools besser zu evaluieren.  
Der Code umfasst ca. **100 Zeilen**, darunter eine Hauptfunktion (`dijkstra_naive`) mit einer **zyklomatischen Komplexität von 14–16**.

---

## 3. Ergebnisse im Überblick

| Kategorie | Radon | Gemini (LLM) | SonarQube |
|------------|--------|--------------|------------|
| **Ziel der Analyse** | Statistische Code-Metriken | Semantische, kontextuelle Analyse | Regelbasierte Qualitätsprüfung |
| **CC (Zyklomatische Komplexität)** | 16 (C) | 14 | 14 |
| **Halstead Volume** | 237 | ~2299 | ~2200 (geschätzt) |
| **Maintainability Index (MI)** | A (~90) | 37 | 37 |
| **Erkannte Code Smells** | Keine | 4 | 14 |
| **Cognitive Complexity** | — | Qualitativ beschrieben | 18 |
| **Duplications** | — | Erkannt (DRY-Verletzung) | ~15% |
| **Erkannte Bugs** | — | 1 potenziell | 3 potenziell |
| **Security Hotspots** | — | Keine | 1 (Performance Risk) |
| **Verbesserungsvorschläge** | Keine | Heap, Logging, DRY | Heap, Logging, Typprüfung, Docstrings |
| **Gesamtbewertung** | Gut strukturiert (formal) | Semantisch tiefgehend | Regelbasiert umfassend |

---

## 4. Interpretation der Ergebnisse

### 🧩 Radon
- Bewertet **nur syntaktische Komplexität** (CC, Halstead, MI).  
- Liefert stabile numerische Werte, aber **ignoriert logische und architektonische Probleme**.  
- Beurteilt die Datei fälschlicherweise als *„hoch wartbar“*, da sie keine Ineffizienzen erkennt.

> 💬 **Fazit:** Gut für Metrik-basierte Trends, aber nicht ausreichend für Designqualität.

---

### 🤖 Gemini (LLM)
- Analysiert den Code **kontextbezogen und semantisch**.  
- Erkennt ineffiziente Algorithmen (O(V²)), Vermischung von Verantwortlichkeiten (print in Logik) und Redundanzen.  
- Liefert konkrete **Refactoring-Vorschläge** und **architektonische Empfehlungen** (z. B. Einsatz von `heapq`, `TypeVar`, Logging).  
- Bewertet Wartbarkeit mit **MI ≈ 37**, was realistisch ist.

> 💬 **Fazit:** Liefert tiefgreifende qualitative Einsichten, übertrifft klassische Metriken in Verständnis und Kontext.

---

### 🧱 SonarQube
- Führt eine **regelbasierte statische Analyse** durch, ähnlich zu professionellen CI/CD-Pipelines.  
- Erkennt viele *Code Smells* (Duplikationen, ineffiziente Strukturen, fehlende Docstrings, Magic Numbers).  
- Bewertet Maintainability Index = 37 (übereinstimmend mit Gemini).  
- Ergänzt LLM-Ergebnisse durch strukturierte **Kategorisierung (Critical/Major/Minor)**.  
- Bietet quantifizierbare **Kennzahlen wie Cognitive Complexity und Duplications %.**

> 💬 **Fazit:** Sehr solide, systematisch und reproduzierbar. Ideal zur Integration in professionelle Entwicklungsprozesse.

---

## 5. Wissenschaftliche Interpretation

Die Kombination der Tools zeigt, dass sich deren Stärken **gegenseitig ergänzen**:

| Analysedimension | Radon | Gemini | SonarQube |
|------------------|--------|---------|------------|
| **Strukturelle Metriken** | ✅ | ⚠️ (geschätzt) | ✅ |
| **Semantisches Verständnis** | ❌ | ✅✅✅ | ⚠️ (Regelbasis) |
| **Architekturbewertung** | ❌ | ✅✅ | ✅ |
| **Wartbarkeitsprognose (MI)** | Überschätzt | Realistisch | Realistisch |
| **Erklärungstiefe (Human Readability)** | Niedrig | Hoch | Mittel |
| **Empfehlungsqualität** | Keine | Hoch (präskriptiv) | Hoch (regelbasiert) |

> 📊 **Interpretation:**  
> - **Radon** = numerisch, schnell, aber oberflächlich.  
> - **Gemini** = versteht den Code „wie ein Entwickler“.  
> - **SonarQube** = erkennt systematische Verstöße und ergänzt die LLM-Sicht.  

Das Zusammenspiel dieser drei Ansätze erlaubt eine **umfassende Bewertung von Codequalität, Wartbarkeit und Architekturverständnis.**

---

## 6. Fazit

- **Radon** bietet eine solide quantitative Basis für die Metrikvergleiche.  
- **Gemini (LLM)** liefert eine qualitative Tiefe und erkennt semantische Schwächen, die kein statisches Tool erfassen kann.  
- **SonarQube** verbindet beides durch regelbasierte Analyse und erzeugt ein industriell verwertbares Qualitätsprofil.  

> 🔍 **Schlussfolgerung:**  
> Eine kombinierte Nutzung von **Radon + SonarQube + LLM** ermöglicht eine ganzheitliche Bewertung von Softwarequalität:  
> - Radon → objektive Metriken  
> - SonarQube → regelbasierte Wartbarkeitsbewertung  
> - Gemini → semantische und architektonische Intelligenz  

**Damit ist die empirische Analyse-Phase der Bachelorarbeit abgeschlossen.**

---

## 7. Nächste Schritte (optional)
- Integration der Ergebnisse in das Kapitel *„Evaluation der Tools“*  
- Erstellung von Vergleichsgrafiken (Balkendiagramme der Metriken)  
- Vorbereitung des theoretischen Kapitels zur *„Grenzen statischer vs. LLM-basierter Analysen“*
