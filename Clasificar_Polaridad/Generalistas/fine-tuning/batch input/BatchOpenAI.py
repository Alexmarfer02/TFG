import json
import pandas as pd

user_prompt = """Eres un analizador de sentimientos experto en español. Tienes que responder si el siguiente texto hace referencia a "POS" (Positivo), "NEG" (Negativo) o "NEU" (Neutral).  
**Limítate a devolver solo la categoría (POS, NEG, NEU), nada más.**"""

output_path = "BatchOpenAI_GPT-4o-mini_2020_Son500.jsonl"
df = pd.read_csv("ES.tsv", sep="\t", names=["ID", "Content"], header=None)
df = df.head(500)

with open(output_path, "w", encoding="utf-8") as outfile:
    for i, row in df.iterrows():
        frase = row["Content"]
        tweet_id = str(row["ID"])
        entry = {
            "custom_id": f"request-{tweet_id}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": user_prompt},
                    {"role": "user", "content": frase}
                ]
            }
        }
        outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")
