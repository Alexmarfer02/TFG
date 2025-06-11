import json
import pandas as pd

output_path = "DataSet-FineTuning.jsonl"
df = pd.read_excel("../../../Spain_train_set_2019.xlsx")

user_prompt = (
    "Eres un analizador de sentimientos experto en español. "
    'Tienes que responder si el siguiente texto hace referencia a "POS" (Positivo), '
    '"NEG" (Negativo) o "NEU" (Neutral).'
)

with open(output_path, "w", encoding="utf-8") as outfile:
    for i, row in df.iterrows():
        frase = row["Content"]
        polarity = str(row["Polarity"])
        entry = {
            "messages": [
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": frase},
            {"role": "assistant", "content": polarity}
            ]
        }
        outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")