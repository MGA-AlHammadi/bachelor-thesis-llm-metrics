import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Lade Umgebungsvariablen
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit("❌ Fehler: Setze GEMINI_API_KEY oder GOOGLE_API_KEY in .env")

# API-Schlüssel konfigurieren
genai.configure(api_key=api_key)

print("🤖 Verfügbare Modelle:")
try:
    models = list(genai.list_models())
    for model in models:
        print(f"- {model.name}")
except Exception as e:
    print(f"❌ Fehler beim Auflisten der Modelle: {str(e)}")