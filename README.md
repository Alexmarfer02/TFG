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

# Instalación

```bash
# Clonar repositorio
git clone https://github.com/Alexmarfer02/TFG.git
cd TFG

#Instalar dependencias
pip install -r requirements.txt
```

---

# Uso

1. Clasificación vía APIs (OpenAI / Groq)
    - Ejecuta notebooks en Clasificar_Polaridad/Generalistas/ o GPT-4o-mini/.
2. Evaluación con RoBERTuito (modelo especializado)
    - Notebook disponible en: Clasificar_Polaridad/Robertuito/Clasificar_Robertuito.ipynb
3. Extraer resultados y preparar métricas
    - Usa los notebooks Extraer_*.ipynb para convertir salidas JSONL en Excel analizables.
4. Fine-tuning
    - Utiliza los scripts de fine-tuning/entrenamiento/ y datasets .jsonl preparados con Fine-Tuning_Dataset*.py.
5. Análisis y visualización
    - Todos los notebooks de evaluación están en Resultados/analisis*.









