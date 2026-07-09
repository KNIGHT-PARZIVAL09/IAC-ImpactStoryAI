"""
Check Gemini API Key and List Available Models
Run this to verify your API key and see which models are available
"""

import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def check_api():
    print("=" * 60)
    print("Gemini API Key Checker")
    print("=" * 60)
    print()
    
    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("❌ ERROR: No API key found in .env file")
        print("\nPlease:")
        print("1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("2. Add it to the .env file")
        return
    
    print(f"✅ API Key found: {api_key[:20]}...")
    print()
    
    try:
        # Configure API
        genai.configure(api_key=api_key)
        print("✅ API configured successfully")
        print()
        
        # List available models
        print("📋 Available Models:")
        print("-" * 60)
        
        models = genai.list_models()
        generation_models = []
        
        for model in models:
            # Check if model supports generateContent
            if 'generateContent' in model.supported_generation_methods:
                generation_models.append(model.name)
                print(f"✅ {model.name}")
                print(f"   Description: {model.description}")
                print(f"   Methods: {', '.join(model.supported_generation_methods)}")
                print()
        
        if generation_models:
            print("=" * 60)
            print(f"\n✅ Found {len(generation_models)} model(s) that support text generation")
            print("\n💡 Recommended model to use in app.py:")
            print(f"   genai.GenerativeModel('{generation_models[0]}')")
        else:
            print("❌ No models found that support generateContent")
            print("\nThis might mean:")
            print("1. Your API key is invalid")
            print("2. Your API key doesn't have the right permissions")
            print("3. There's a quota or billing issue")
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        print("\nPossible issues:")
        print("1. Invalid API key")
        print("2. API key doesn't have access")
        print("3. Network connection issues")
        print("4. Quota exceeded")
        print("\nGet a new API key from: https://makersuite.google.com/app/apikey")

if __name__ == "__main__":
    check_api()
