# Logbook 4 – Analyse eines Open-Source-Beispiels (QuickSort)

**Datum:** 05.10.2025  
**Projekt:** Bachelorarbeit – LLM & Softwaremetriken  
**Datei:** `experiments/github_quicksort.py`  
**Quelle:** [https://github.com/calebmadrigal/algorithms-in-python/blob/master/quicksort.py](https://github.com/calebmadrigal/algorithms-in-python/blob/master/quicksort.py)

---

## 1. Ziel des Experiments
Das Ziel dieses Experiments war die Analyse einer realen Open-Source-Implementierung des QuickSort-Algorithmus mithilfe zweier Ansätze:
1. **Klassische statische Softwaremetriken** (Radon)  
2. **Semantische Analyse mit einem LLM** (Google Gemini API)

Untersucht werden sollten Unterschiede in Objektivität, Tiefe und Interpretierbarkeit der Ergebnisse.

---

## 2. Beschreibung des Codes
Der untersuchte Code implementiert den **QuickSort-Algorithmus** in Python.  
Die Funktion `quicksort()` arbeitet rekursiv:
- Auswahl des mittleren Elements als Pivot  
- Aufteilung der Eingabeliste in drei Teillisten  
  *(kleiner als Pivot – gleich Pivot – größer Pivot)*  
- Rekursive Sortierung und anschließendes Zusammenführen  

Die Funktion `main()` dient als einfacher Testlauf mit Beispielwerten.

---

## 3. Durchführung der Radon-Analyse
Zur statischen Analyse wurde **Radon** verwendet.  
Die folgenden Kommandos wurden ausgeführt:

```bash
radon cc experiments/github_quicksort.py
radon hal experiments/github_quicksort.py
radon mi experiments/github_quicksort.py

Interpretation

Die zyklomatische Komplexität liegt bei 5 – der Code ist klar strukturiert und einfach nachzuvollziehen.

Das Halstead-Volumen (125,3) weist auf eine geringe kognitive Belastung hin.

Der Maintainability Index (A) bestätigt eine sehr gute Wartbarkeit des Codes.

4. Durchführung der LLM-Analyse (Gemini API)

Die gleiche Datei wurde anschließend mit dem Modell models/gemini-pro-latest der Google Gemini API analysiert.
Ziel war es, die Fähigkeit eines LLM zu testen, nicht nur Metriken zu erkennen, sondern auch qualitative Aussagen zur Codequalität und zu möglichen Verbesserungen zu treffen.

Ergebnisse

Zyklomatische Komplexität

quicksort: 5

main: 1

Halstead-Metriken (geschätzt)

Volume: 255.4

Difficulty: 24

Effort: 6130

Bugs: 0.085

Maintainability Index

≈ 100 → Exzellente Wartbarkeit

Erkannte Code Smells

Ineffiziente Speicherverwendung (drei neue Listen pro Rekursionsschritt)

Naive Pivot-Wahl → möglicher Worst-Case O(n²)

Potenzieller RecursionError bei großen Eingabelisten

Verbesserungsvorschläge

Nutzung einer in-place Partitionierung (Lomuto-Schema) zur Reduktion des Speicherverbrauchs

Implementierung einer besseren Pivot-Strategie (z. B. zufällig oder Median-of-Three)

Hinzufügen von Type Hints und Docstrings für mehr Lesbarkeit und Wartbarkeit


5. Vergleich Radon vs. LLM (Gemini)

Aspekt	                  Radon	              Gemini	                 Bemerkung
--------------------------------------------------------------------------------------------------
Zyklomatische Komplexität	5	                5	                 Gleiche Bewertung
--------------------------------------------------------------------------------------
Maintainability Index	    A (~95 – 100)	    100	                      Konsistent
--------------------------------------------------------------------------------------
Halstead Volume	            125.3	            255.4	           LLM schätzt komplexer
----------------------------------------------------------------------------------------
Code Smells	        Keine erkannt	    3 konkrete Probleme  LLM erkennt algorithmische Schwächen
-----------------------------------------------------------------------------------------
Verbesserungsvorschläge	   Keine	    In-Depth Vorschläge 	LLM liefert semantischen Mehrwert

6. Interpretation der Ergebnisse

Die Ergebnisse zeigen, dass beide Analyseansätze – statische Metriken und LLM-Analyse – konsistente, aber unterschiedlich tiefe Einblicke bieten.

Radon liefert eine objektive und quantitative Bewertung der Code-Komplexität.

Gemini erkennt zusätzlich semantische Aspekte, algorithmische Schwächen und Performance-Risiken.

Besonders bei rekursiven Algorithmen liefert die LLM-Analyse wertvolle Vorschläge, die über die klassischen Metriken hinausgehen.

7. Fazit
Softwaremetriken.
Die LLM-Analyse hat zusätzlich wertvolle Optimierungsmöglichkeiten aufgezeigt – insbesondere in Bezug auf Effizienz und Speicherverbrauch.
Somit ergänzen sich beide Analyseformen idealerweise.

Gesamtbewertung:

QuickSort (Python, rekursiv, funktional korrekt)
→ Sehr gute Wartbarkeit, geringe Komplexität, algorithmisch optimierbar.


8. Reflexion und Ausblick

Das Experiment zeigt, dass LLM-Modelle wie Gemini nicht nur Metriken reproduzieren, sondern auch qualitative Verbesserungsvorschläge bieten können.
Im nächsten Schritt wird ein komplexerer Algorithmus (z. B. BFS / Graph-Suche) analysiert, um zu überprüfen, ob die Konsistenz der Ergebnisse auch bei höherer Codekomplexität erhalten bleibt.