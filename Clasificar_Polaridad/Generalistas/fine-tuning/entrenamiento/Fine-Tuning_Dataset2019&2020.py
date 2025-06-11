import json
import pandas as pd

output_path = "DataSet-FineTuning2.jsonl"
df_2019 = pd.read_excel("../../../Spain_train_set_2019.xlsx")
df_2020 = pd.read_csv("Train_set_2020.tsv", sep="\t", header=None, names=["ID", "Content", "Polarity"])

df_2019 = df_2019[["ID", "Content", "Polarity"]]
df_2020 = df_2020[["ID", "Content", "Polarity"]]

df = pd.concat([df_2019, df_2020], ignore_index=True)

user_prompt = (
    "Eres un analizador de sentimientos experto en español. "
    'Tienes que responder si el siguiente texto hace referencia a "POS" (Positivo), '
    '"NEG" (Negativo) o "NEU" (Neutral).'
)

with open(output_path, "w", encoding="utf-8") as outfile:
    for _, row in df.iterrows():
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