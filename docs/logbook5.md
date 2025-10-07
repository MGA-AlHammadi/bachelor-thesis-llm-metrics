# Logbuch 5 – Analyse eines JavaScript-Algorithmus mit ESLint und Gemini API

## 1. Ziel des Experiments

Ziel dieses Abschnitts war es, den Einsatz von **LLMs (Large Language Models)** bei der Analyse von JavaScript-Code zu evaluieren und die Ergebnisse mit klassischen statischen Analysewerkzeugen – insbesondere **ESLint** – zu vergleichen.  
Dazu wurde ein bekannter Algorithmus (QuickSort) aus einem Open-Source-Projekt (TheAlgorithms) verwendet.

📎 **Quelle des Codes:**  
[https://github.com/TheAlgorithms/Javascript/blob/master/Sorts/quickSort.js](https://github.com/TheAlgorithms/Javascript/blob/master/Sorts/quickSort.js)

---

## 2. Vorbereitung

Der QuickSort-Code wurde in die Datei  
`experiments/github_quicksort.js` kopiert und als Grundlage für die Analyse genutzt.

Der Code implementiert den QuickSort-Algorithmus in funktionaler Form unter Verwendung von JavaScript-Array-Methoden (`filter`, `map`, `concat`) und einer rekursiven Struktur.

---

## 3. Durchführung der ESLint-Analyse

Zunächst wurde der Code mithilfe von **ESLint** überprüft:

```bash
npx eslint experiments/js_examples/github_quicksort.js -f json > results/eslint_quicksort.json

 Ergebnis:

Keine Syntaxfehler oder Laufzeitprobleme erkannt

Allgemeine Hinweise auf Verbesserungen:

Empfehlung zur Verwendung von const statt let

Vorschlag zur Dokumentation mittels JSDoc-Kommentaren

Kein erkennbarer Verstoß gegen Code-Stilregeln

Interpretation:
ESLint identifiziert keine strukturellen oder syntaktischen Probleme.
Die Analyse bleibt auf formaler Ebene und konzentriert sich auf Syntax, Stil und potenzielle Best Practices.

4. Durchführung der LLM-Analyse (Gemini API)

Die gleiche Datei wurde anschließend mit dem Modell
models/gemini-pro-latest der Google Gemini API analysiert.
Ziel war es, zu untersuchen, ob das LLM über die statischen Regeln hinaus qualitative Aussagen über Codequalität und algorithmische Effizienz treffen kann.

Prompt (vereinfacht):

Analysiere diesen JavaScript-Code vollständig
– Zyklomatische Komplexität
– Halstead-Metriken
– Maintainability Index
– Code Smells
– Verbesserungsvorschläge

5. Ergebnisse der Gemini-Analyse
🔹 Zyklomatische Komplexität
Funktion	Wert	   Interpretation
----------------------------------------------
quickSort()	 2	 Sehr einfache Kontrollstruktur
-----------------------------------------------
main()	     1	 Sequenziell, keine Verzweigungen


🔹 Halstead-Metriken (geschätzt)
Metrik	Wert	Bedeutung
Volume	~290	Geringe Codegröße
Difficulty	~25	Moderate kognitive Komplexität
Effort	~7.250	Mittlerer Implementierungsaufwand
Bugs	~0.1	Sehr geringe Fehleranfälligkeit

🔹 Maintainability Index

Berechneter Wert: ~109
→ Exzellente Wartbarkeit (Skala: >85 = sehr gut)

🔹 Erkannte Code Smells

Ineffiziente Partitionierung:
Drei separate filter()-Durchläufe pro Rekursion erhöhen die Laufzeitkomplexität.

Hoher Speicherverbrauch:
Jede Rekursion erzeugt neue Arrays (left, middle, right), was den Speicherbedarf drastisch erhöht.

Naive Pivot-Wahl:
Verwendung des mittleren Elements kann bei vorsortierten Arrays zum Worst Case (O(n²)) führen.

🔹 Verbesserungsvorschläge des LLM

In-Place-Partitionierung (Lomuto-/Hoare-Schema):
Reduziert die Speicherkomplexität von O(n) auf O(log n).

Optimierte Pivot-Wahl (Median-of-Three):
Minimiert das Risiko eines unausgewogenen Teilens des Arrays.

Hybrid-Ansatz für kleine Arrays:
Verwendung von Insertion Sort für kleine Teilarrays zur Performance-Steigerung.

Type-Hints und JSDoc-Kommentare:
Verbesserung der Wartbarkeit und Dokumentation.

6. Vergleich ESLint vs. Gemini
Aspekt	               ESLint	             Gemini	                Bemerkung
Syntax- und Stilfehler	Keine	             Keine	                Konsistent
Tiefe der Analyse	Formale Regeln	Strukturelle + algorithmische Analyse	LLM tiefergehend
Komplexitätsmetriken	Nicht verfügbar	Detaillierte Werte (Halstead, MI)	Nur LLM
Code Smells	Keine erkannt	3 erkannt (Effizienz, Speicher, Pivot)	LLM erkennt semantische Schwächen
Verbesserungsvorschläge	Stil-Ebene (const, JSDoc)	Algorithmisch & semantisch	LLM bietet Mehrwert

7. Interpretation der Ergebnisse

Die Ergebnisse zeigen, dass klassische Metriken und LLM-Analysen sich ergänzen:

ESLint bewertet Syntax und Stil (formale Korrektheit).

Gemini liefert semantische Einsichten in Effizienz, Wartbarkeit und algorithmische Qualität.

Gemini war in der Lage, algorithmische Schwächen zu erkennen und konkrete Verbesserungen vorzuschlagen, die weit über statische Analysen hinausgehen.

8. Fazit

Der QuickSort-Code weist aus Sicht klassischer Metriken eine hohe Qualität und exzellente Wartbarkeit auf.
Das LLM konnte jedoch zusätzliche Optimierungspotenziale identifizieren, insbesondere bei Speicher- und Laufzeiteffizienz.

 Gesamtbewertung:

Wartbarkeit: A (sehr gut)

Algorithmische Effizienz: optimierbar

LLM bietet qualitativen Mehrwert gegenüber rein statischen Tools.

9. Reflexion und Ausblick

Dieses Experiment bestätigt, dass LLM-basierte Code-Analysen eine sinnvolle Ergänzung zu klassischen Tools wie ESLint oder SonarQube darstellen.

Im nächsten Schritt soll untersucht werden, ob sich dieses Verhalten auch bei komplexeren JavaScript-Projekten (z. B. React-Komponenten oder asynchroner Logik) reproduzieren lässt.
Parallel dazu wird eine Integration mit SonarQube durchgeführt, um die Ergebnisse der verschiedenen Analysearten quantitativ zu vergleichen.
