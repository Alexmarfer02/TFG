# Diseño de Sistemas de Evaluación de las Capacidades de Clasificación de los Grandes Modelos de Lenguaje y Comparacion con otros modelos de Procesamiento de Lenguaje Natural

**Autor**: Álex Márquez Fernández de la Vega  
**Grado**: Ingeniería de Tecnologías y Servicios de Telecomunicación  
**Universidad**: UPM - ETSI de Telecomunicación  
**Fecha**: Junio 2025

---

## Descripción

Este repositorio contiene el código, scripts y recursos utilizados en el Trabajo de Fin de Grado enfocado en el análisis y evaluación de la capacidad de los Grandes Modelos del Lenguaje (LLMs) para realizar tareas de clasificación de sentimiento en español. Se comparan modelos generalistas (GPT-4o, LLaMA, Gemma) con un modelo especializado (RoBERTuito), utilizando técnicas como prompting (zero-shot, few-shot y Chain-of-Thought) y fine-tuning supervisado.

---

## Objetivos del Proyecto

- Comparar modelos generalistas y especializados en análisis de sentimiento en español.
- Evaluar estrategias de prompting y su impacto en la clasificación.
- Realizar fine-tuning sobre GPT-4o-mini y analizar su rendimiento.
- Estudiar la coherencia interna de los razonamientos generados (CoT).
- Utilizar métricas estándar (accuracy, precision, recall, F1-score) y análisis semántico (PCA, clustering).

---

## Estructura del Repositorio

- `Clasificar_Polaridad/`: scripts y notebooks para ejecutar los modelos y clasificar los datasets.
  - `Generalistas/`: notebooks para GPT-4o, LLaMA, Gemma.
    - `fine-tuning/`: scripts, datos y resultados del fine-tuning sobre GPT-4o-mini.
  - `GPT-4o-mini/`: notebooks y prompts para evaluar con distintos esquemas de prompting.
  - `Robertuito/`: notebook de evaluación con el modelo especializado RoBERTuito.
- `DataSets/`: datasets originales InterTASS 2019 y 2020 y scripts de procesamiento.
- `Resultados/`: notebooks de análisis y visualización.
  - `analisis fine-tuning/`: métricas y comparativas tras fine-tuning.
  - `analisis prompts/`: análisis de prompting y razonamiento CoT.

---

## Tecnologías y Herramientas

- **Lenguaje:** Python
- **Librerías:** pandas, scikit-learn, matplotlib, seaborn, spaCy, transformers, openai, pysentimiento
- **APIs**: [OpenAI](https://platform.openai.com/), [Groq](https://console.groq.com/)
- **Modelos evaluados:**
  - Generalistas: GPT-4o (OpenAI), LLaMA (Groq), Gemma (Groq)
  - Especializado: RoBERTuito (Hugging Face)
- **Entornos**: Jupyter Notebook
- **Técnicas:** prompting (zero-shot, few-shot, CoT), fine-tuning supervisado, BoW, TF-IDF, PCA, clustering

---
Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

bash
Copiar
Editar
# 1. Clona el repositorio
git clone https://github.com/Alexmarfer02/TFG.git
cd TFG

# 2. Instala las dependencias (Python 3.10+ recomendado)
pip install -r requirements.txt
▶️ Cómo ejecutar los experimentos
A continuación se indican los notebooks principales para cada fase del proyecto:

🔍 Clasificación de polaridad
GPT-4o (OpenAI):
Clasificar_Polaridad/GPT-4o-mini/Extraer_GPT-4o-mini.ipynb

Modelos generalistas (Groq):

Clasificar_Polaridad/Generalistas/Clasificar_gemma2-9b-it.ipynb

Clasificar_Polaridad/Generalistas/Clasificar_llama-3.1-8b-instant.ipynb

Clasificar_Polaridad/Generalistas/Clasificar_llama-3.3-70b-versatile.ipynb

Modelo especializado (RoBERTuito):
Clasificar_Polaridad/Robertuito/Clasificar_Robertuito.ipynb

🛠️ Fine-tuning de GPT-4o-mini
Scripts y datasets:

Clasificar_Polaridad/Generalistas/fine-tuning/entrenamiento/Fine-Tuning_Dataset2019.py

Clasificar_Polaridad/Generalistas/fine-tuning/entrenamiento/Fine-Tuning_Dataset2019&2020.py

Evaluación de modelos fine-tuned:

Clasificar_Polaridad/Generalistas/fine-tuning/Extraer_GPT-4o-mini&FineTuning.ipynb

📊 Análisis y visualización de resultados
Comparativas de rendimiento:

Resultados/analisis fine-tuning/graficas-comparativas.ipynb

Análisis de prompting:

Resultados/analisis prompts/analisis_prompts.ipynb

Resultados/analisis prompts/graficas-prompts.ipynb

Análisis de razonamiento (CoT):

Resultados/analisis prompts/Análisis de razonamiento/Razonamientos_GPT-4o-mini.ipynb

Resultados/analisis prompts/Análisis de razonamiento/Razonamientos_llama-3.3-70b-versatile.ipynb

⚠️ Requisitos externos
Cuenta en OpenAI con clave API para usar GPT-4o-mini.

Cuenta en Groq Cloud para ejecutar LLaMA y Gemma.

Claves API deben configurarse en los notebooks o scripts correspondientes.





