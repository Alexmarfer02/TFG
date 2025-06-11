import json
import pandas as pd
user_prompt = [
    
    """Eres un analizador de sentimientos experto en español. Tienes que responder si el siguiente texto hace referencia a "POS" (Positivo), "NEG" (Negativo) o "NEU" (Neutral).  
        **Limítate a devolver solo la categoría (POS, NEG, NEU), nada más.**""",
    
    
    """Eres un analizador de sentimientos experto en español. Tu tarea es leer el siguiente tweet y clasificarlo en una de estas categorías:  
    POS → Expresa felicidad, satisfacción o una emoción positiva.  
        NEG → Contiene quejas, frustración o emociones negativas.  
        NEU → No tiene emoción clara o es informativo, o relamente no dice nada. 
    
        Ejemplo:
        Texto: "Hoy es un día maravilloso" Respuesta: POS
        Texto: "No me gusta el frío" Respuesta: NEG
        Texto: "El coche es azul" Respuesta: NEU   
        **Limítate a devolver solo la categoría, nada más.**""",
    
    
    """Eres un analizador de sentimientos experto en español. Clasifica la siguiente bateria de tweets en una de las siguientes categorías:  
        POS → Si expresa alegría, emoción positiva o satisfacción.  
        NEG → Si muestra quejas, descontento o emociones negativas.  
        NEU → Si es un comentario informativo sin carga emocional, o relamente no dice nada.
        Hazlo Paso a paso siguiendo el siguiente formato:
    
        1. Identificación de palabras clave: [Enumera palabras o frases clave en el texto] 
        2. Interpretación del tono general: [Explica si el tono es positivo, negativo o neutro basado en el contexto]  
        3. Detección de matices: [Considera si hay ironía, emoción oculta o lenguaje ambiguo]
        4. Polaridad final (Positivo, Negativo, neutral): [POS / NEG / NEU]
    
        No queiro que añadas más de lo descrito, limitate a responder lo que se te pide y como se te pide.
    
        Ejemplo:
        Texto: "No está mal, pero esperaba algo mucho mejor."
        1. Identificación de palabras clave: "No está mal", "esperaba algo mucho mejor"
        2. Interpretación del tono general: El texto no es completamente negativo, pero expresa una decepción.
        3. Detección de matices: Aunque "No está mal" podría parecer positivo, la segunda parte del texto implica insatisfacción.
        4. Polaridad final: NEG"""
    ]

output_path_gpt4o = "BatchOpenAI_GPT4o.jsonl"
df = pd.read_csv("../../../Spain_train_set_2019.csv")

for numero in range(len(user_prompt)):
    output_path = f"BatchOpenAI_GPT4o_{numero}.jsonl"
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
                        {"role": "system", "content": user_prompt[numero]},
                        {"role": "user", "content": frase}
                    ]
                }
            }
            outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")

    output_path_gpt4o