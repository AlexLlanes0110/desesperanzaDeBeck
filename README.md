# Evaluador de Escala de Desesperanza de Beck (BHS)

Este script en Python automatiza el procesamiento de respuestas a la **Escala de Desesperanza de Beck**, utilizada para evaluar actitudes negativas sobre el futuro. La herramienta toma respuestas desde un archivo Excel (`estudio.xlsx`), calcula puntajes individuales, desglosa factores y clasifica el riesgo de desesperanza de cada sujeto evaluado.

## 📋 ¿Qué hace este script?

- Lee respuestas desde un archivo Excel con estructura tipo cuestionario.
- Evalúa los ítems según las reglas de la Escala de Beck.
- Calcula los puntajes totales por sujeto.
- Calcula los puntajes por factores: **afectivo**, **motivacional**, y **cognitivo**.
- Clasifica el nivel de riesgo de desesperanza.
- Genera un archivo Excel (`resultados_desesperanza.xlsx`) con los resultados procesados.

## 🧠 Fundamento teórico

La Escala de Desesperanza de Beck consta de 20 ítems tipo verdadero/falso. Cada ítem suma 1 punto si coincide con una respuesta indicativa de desesperanza. La suma total clasifica el riesgo del individuo:

| Puntaje Total | Nivel de Riesgo            |
|---------------|-----------------------------|
| 0 – 3         | Ningún o mínimo riesgo      |
| 4 – 8         | Riesgo bajo                 |
| 9 – 14        | Riesgo moderado             |
| 15 – 20       | Riesgo alto                 |

### 🔍 Clasificación por factores:

- **Afectivo**: ítems 1, 6, 13, 15, 19  
- **Motivacional**: ítems 2, 3, 9, 11, 12, 16, 17, 20  
- **Cognitivo**: ítems 4, 7, 8, 14, 18  

## 🛠️ Requisitos

- Python 3.7+
- pandas
- openpyxl (para exportar Excel)

Instalación:
```bash
pip install pandas openpyxl


📂 Estructura esperada del archivo Excel
Primera columna: nombre o identificador del sujeto (ej. sujeto1, sujeto2…)

Columnas siguientes: respuestas a los ítems como Item1, Item2, ..., Item20.

Las respuestas deben ser "VERDADERO" o "FALSO" (el script maneja variaciones comunes como minúsculas y espacios).

Ejemplo:


Sujeto	Item1	Item2	...	Item20
sujeto1	FALSO	VERDADERO	...	FALSO
sujeto2	FALSO	FALSO	...	VERDADERO
📤 Salida
El script genera un archivo llamado resultados_desesperanza.xlsx con columnas:

Sujeto

Puntaje Total

Factor Afectivo

Factor Motivacional

Factor Cognitivo

Clasificación de Riesgo

✨ Autor
Desarrollado por Aguilar Llanes ALejandro Antonio.
Inspirado en la necesidad de automatizar evaluaciones psicológicas para facilitar el análisis en entornos académicos o clínicos.
