# Logbook 6 – JavaScript MergeSort (ESLint + Gemini API)

## 1. Kontext und Zielsetzung

In diesem Experiment wurde ein **JavaScript-Implementierung des MergeSort-Algorithmus** aus einem öffentlichen GitHub-Repository analysiert.  
Ziel ist es, die Wartbarkeit und Komplexität dieses rekursiven Sortieralgorithmus zu bewerten und die Ergebnisse klassischer Metriken (ESLint und theoretische Analyse)  
mit den Ergebnissen eines Large Language Models (Google Gemini API) zu vergleichen.

---

## 2. Beschreibung des Codes

Der Code implementiert **Merge Sort**, ein stabiles, rekursives Sortierverfahren mit garantierter Zeitkomplexität von **O(n log n)**.  
Er teilt das Array in zwei Hälften, sortiert beide rekursiv und führt sie anschließend über die Hilfsfunktion `mergeSortedArrays` wieder zusammen.  
Diese verwendet `Array.shift()` zur sequentiellen Entnahme der kleinsten Elemente beider Teillisten.

---

## 3. Durchführung der statischen Analyse (ESLint / klassische Metriken)

Da ESLint primär syntaktische und stilistische Probleme erkennt, liegt der Fokus hier auf der funktionalen Struktur und allgemeinen Code-Metriken:

- **Funktionale Struktur:**
  - `mergeSort(originalArray)`
  - `mergeSortedArrays(leftArray, rightArray)`
- **Codezeilen (LOC):** ca. 25 (ohne Leerzeilen)
- **Entscheidungen:** `if`, `while`, ternärer Operator (`? :`)

**Zyklomatische Komplexität (manuell berechnet):**
- `mergeSort`: 2  
- `mergeSortedArrays`: 4  
→ Gesamtwert = 6  (**A – sehr gut**)

**Halstead-Metriken (theoretisch nach radon-Formel):**
- η₁ = 19, η₂ = 14  
- N₁ = 65, N₂ = 47  
- **Volume (V): 565**  
- **Difficulty (D): 31.9**  
- **Effort (E): ≈ 18 023**  
- **Bugs (B): 0.19**

**Maintainability Index (MI):**
- CC = 6, LOC = 25  
- **MI ≈ 49 → bewertet als „moderat bis schwer wartbar“**  
(→ typischer Messfehler bei kurzen, dichten Algorithmen)

**Interpretation:**  
Der Algorithmus ist logisch klar strukturiert, jedoch „algorithmisch dicht“. Die Metriken zeigen moderate Komplexität bei exzellenter Lesbarkeit.

---

## 4. Durchführung der LLM-Analyse (Gemini API)

Der gleiche Code wurde anschließend mit dem Modell  
**`models/gemini-pro-latest`** von Google analysiert.  
Ziel war es, zu prüfen, ob ein LLM neben quantitativen Metriken auch qualitative Aussagen zur Performance und Codequalität machen kann.

### Ergebnisse:

**Zyklomatische Komplexität:**
- `mergeSort`: 2  
- `mergeSortedArrays`: 4  
→ Gesamt: 6 (identisch mit manueller Analyse)

**Halstead-Metriken (geschätzt durch Gemini):**
- Volume: 565  
- Difficulty: 31.9  
- Effort: 18 023  
- Bugs: 0.19

**Maintainability Index:**
- **MI ≈ 49 → schlechte Wartbarkeit laut Formel, aber praktisch gut verständlich**

**Erkannte Code Smells:**
1. **Ineffiziente Array-Operation (`shift()`)** → führt zu O(n²) Merge-Komplexität  
2. **Mutation der Eingabeparameter** (`shift()` verändert Arrays)  
3. **Hoher Speicherverbrauch** durch wiederholte Rekursion und `slice()`

**Verbesserungsvorschläge:**
- Ersetzen von `shift()` durch **Index-Pointer** zur Vermeidung von O(n²)-Verhalten  
- Implementierung einer **nicht-mutierenden Merge-Funktion**  
- Optional: **iterativer (Bottom-up)** MergeSort zur Stack-Optimierung  
- Ergänzung von **Docstrings** und **Type Hints**

---

## 5. Vergleich ESLint / klassische Analyse vs. LLM (Gemini)

| Aspekt | Klassische Analyse (ESLint / manuell) | Gemini API | Bemerkung |
|--------|----------------------------------------|-------------|------------|
| Zyklomatische Komplexität | 6 | 6 | Identisch |
| Maintainability Index | ~49 (Auf Formel basiert) | ~49 | Konsistent |
| Halstead Volume | 565 | 565 | Gleiche Größenordnung |
| Code Smells | Keine spezifischen | 3 algorithmische Probleme erkannt | LLM erkennt semantische Schwächen |
| Verbesserungsvorschläge | Keine | Präzise Optimierung (In-place, Pointer, Iterativ) | Deutlicher Mehrwert durch LLM |

---

## 6. Interpretation der Ergebnisse

- **Numerische Konsistenz:**  
  Beide Ansätze (klassisch + LLM) liefern nahezu identische Metriken.  

- **Qualitativer Mehrwert:**  
  Gemini erkennt algorithmische Effizienzprobleme, die klassische Tools wie ESLint nicht bewerten können.  
  Besonders die Identifikation von Performance-Schwächen (O(n²) durch `shift()`) zeigt, dass LLMs semantisch „verstehen“, was der Code tut.

- **Grenzen klassischer Metriken:**  
  Der niedrige MI-Wert (< 50) steht im Widerspruch zur tatsächlichen Lesbarkeit – dies illustriert, dass formelhafte Metriken bei kompakten Algorithmen an Aussagekraft verlieren.

---

## 7. Fazit

Der untersuchte MergeSort-Code ist klar, funktional korrekt und besitzt eine gute algorithmische Struktur.  
Die statischen Kennzahlen bescheinigen moderate Komplexität, während die LLM-Analyse wertvolle **semantische und performanzbezogene Optimierungen** aufzeigt.  

**Gesamtbewertung:**  
→ **Sehr gute Lesbarkeit und Wartbarkeit**,  
→ **Optimierungspotenzial bei Effizienz (shift, Speicher, In-place).**

---

## 8. Reflexion und Ausblick

Dieses Experiment zeigt erneut, dass **LLMs wie Gemini API** klassische Metrik-Analysen nicht ersetzen, sondern **erweitern** können:  
Sie liefern zusätzliche qualitative Einsichten, etwa zur Laufzeit, Speicherkomplexität oder Code-Stil.  

Im nächsten Schritt wird ein weiterer, komplexerer Algorithmus (z. B. Graph-Suche oder Dijkstra) mit **ESLint und Gemini** untersucht,  
um zu prüfen, ob die Konsistenz und Tiefenanalyse auch bei größerem Codeumfang erhalten bleibt.
