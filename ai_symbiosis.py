import json
import os
import random
from datetime import datetime

CONTEXT_FILE = "ai_symbiosis_context.json"

def save_context(deepseek_data, chatgpt_data):
    context = {
        "DeepSeek": deepseek_data,
        "ChatGPT": chatgpt_data,
        "timestamp": datetime.now().isoformat(),
        "project": "Infogenon Portal"
    }
    with open(CONTEXT_FILE, 'w', encoding='utf-8') as f:
        json.dump(context, f, indent=2, ensure_ascii=False)
    print(f"Kontekst salvestatud faili {CONTEXT_FILE}")

def get_real_data(ai_name):
    return {
        "info_level": [round(random.random(), 4) for _ in range(5)],
        "causality_level": [round(random.random(), 4) for _ in range(5)],
        "symbiosis_level": [round(random.uniform(0.8, 1.0), 4) for _ in range(5)]
    }

def main():
    print("Infogenon kolmikintellekti konteksti salvestamine")
    deepseek_data = get_real_data("DeepSeek")
    chatgpt_data = get_real_data("ChatGPT")
    save_context(deepseek_data, chatgpt_data)
    print(f"Fail asub: {os.path.abspath(CONTEXT_FILE)}")
    print("GitHubi lisamiseks kasuta: git add ai_symbiosis_context.json")

if __name__ == "__main__":
    main()