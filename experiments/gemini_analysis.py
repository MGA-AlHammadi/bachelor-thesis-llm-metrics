import os
import google.generativeai as genai
from dotenv import load_dotenv

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Der zu analysierende Code
code = """def foo(x):
    if x > 0:
        return x
    else:
        return -x
"""

# API-Schlüssel aus der Umgebungsvariable laden
api_key = os.getenv("GOOGLE_API_KEY")

# Hauptcode
print("Starte Code-Analyse mit Google Gemini...")
print("API-Schlüssel wird konfiguriert...")

try:
    # API-Schlüssel setzen
    genai.configure(api_key=api_key)
    print("API-Schlüssel konfiguriert.")
    
    # Generierungsparameter konfigurieren
    generation_config = {
        "temperature": 0.2,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 1024,
    }
    
    print("Verfügbare Modelle werden abgefragt...")
    # Verfügbare Modelle anzeigen
    for m in genai.list_models():
        print(f"Verfügbares Modell: {m.name}")
    
    print("Modell wird initialisiert...")
    # Das aktuelle Modell auswählen aus den verfügbaren Modellen
    # Wir verwenden ein Flash-Modell, das weniger Ressourcen benötigt
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",
        generation_config=generation_config
    )
    
    print("Anfrage wird gesendet...")
    
    print("\nSende Vollständige Analyse...")
    prompt = f"""Analysiere diesen Python-Code vollständig:

{code}

Gib eine komplette Analyse mit:
1. Zyklomatische Komplexität
2. Halstead Metriken (Volume, Difficulty, Effort, Bugs)
3. Maintainability Index
4. Code Smells
5. Verbesserungsvorschläge

Sei konsistent und genau in der Analyse!"""

    response = model.generate_content(prompt)
    
    print("\nVOLLSTÄNDIGE CODE ANALYSE:")
    print("-" * 60)
    print(response.text)

except Exception as e:
    print(f"Fehler bei der Analyse: {str(e)}")