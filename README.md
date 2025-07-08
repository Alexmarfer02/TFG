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

TFG/
├── Clasificar_Polaridad/
│ ├── Spain_test_2020.xlsx
│ ├── Spain_train_set_2019.xlsx
│ ├── Generalistas/
│ │ ├── Clasificar_gemma2-9b-it.ipynb
│ │ ├── Clasificar_llama-3.1-8b-instant.ipynb
│ │ ├── Clasificar_llama-3.3-70b-versatile.ipynb
│ │ └── fine-tuning/
│ │ ├── Clasificación_GPT-4o-mini_Fine-tuning.xlsx
│ │ ├── Extraer_GPT-4o-mini&FineTuning.ipynb
│ │ ├── entrenamiento/ (datasets .jsonl y scripts de preparación)
│ │ ├── batch input/ (prompts .jsonl)
│ │ └── batch output/ (resultados de OpenAI API)
│ ├── GPT-4o-mini/
│ │ ├── Extraer_GPT-4o-mini.ipynb
│ │ ├── batch input/
│ │ └── batch output/
│ └── Robertuito/
│ └── Clasificar_Robertuito.ipynb
│
├── DataSets/
│ ├── 2019/ (XML original y scripts de parsing)
│ └── 2020/ (TSV + procesamiento)
│
├── Resultados/
│ ├── analisis fine-tuning/
│ │ ├── graficas-comparativas.ipynb
│ │ └── datos/
│ └── analisis prompts/
│ ├── notebooks de análisis
│ ├── Análisis de razonamiento/
│ └── datos/

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




