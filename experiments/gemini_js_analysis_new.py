import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Lade Variablen aus .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit("❌ Fehler: Setze GEMINI_API_KEY oder GOOGLE_API_KEY in .env")

# Stelle sicher, dass ein Datei-Argument übergeben wurde
if len(sys.argv) < 2:
    raise SystemExit("❌ Bitte gib eine JavaScript-Datei an. Beispiel:\npython experiments/gemini_js_analysis.py experiments/github_quicksort.js")

file_path = sys.argv[1]
if not os.path.exists(file_path):
    raise SystemExit(f"❌ Datei nicht gefunden: {file_path}")

# Code aus Datei laden
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Konfiguriere Gemini API
genai.configure(api_key=api_key)

# Verfügbares Modell 
model_name = "models/gemini-pro-latest"

# Prompt vorbereiten
prompt = f"""Analysiere diesen JavaScript-Code vollständig:

```javascript
{code}
```

Gib bitte:
1. Zyklomatische Komplexität (konkreter Wert für jede Funktion)
2. Halstead-Metriken (Volume, Difficulty, Effort, Bugs)
3. Maintainability Index (mit Interpretation)
4. Mögliche Code Smells
5. Konkrete Verbesserungsvorschläge
"""

try:
    print(f"🚀 Verwende Modell: {model_name}")
    print("🔄 Generiere Code-Analyse...")
    
    # Modell initialisieren
    model = genai.GenerativeModel(model_name)
    
    # Antwort generieren
    response = model.generate_content(prompt)
    
    # Text aus der Antwort extrahieren
    result_text = ""
    
    if hasattr(response, "text"):
        result_text = response.text
    elif hasattr(response, "candidates") and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate, "content") and candidate.content:
                if hasattr(candidate.content, "parts") and candidate.content.parts:
                    for part in candidate.content.parts:
                        if hasattr(part, "text"):
                            result_text += part.text
    
    if not result_text:
        print("⚠️ Keine Antwort erhalten.")
        print(f"Antwortstruktur: {type(response)}")
        print(str(response))
    else:
        print("\n--- ANALYSE VON GEMINI ---\n")
        print(result_text)
        
        # Ergebnis speichern
        os.makedirs("results", exist_ok=True)
        out_file = os.path.join("results", f"gemini_analysis_{os.path.basename(file_path)}.txt")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(result_text)
            
        print(f"\n💾 Gespeichert in: {out_file}")

except Exception as e:
    print("❌ Fehler bei der Analyse:", str(e))