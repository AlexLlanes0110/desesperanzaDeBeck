import os
import pandas as pd

ruta = os.path.join(os.path.dirname(__file__), 'estudio.xlsx')
df = pd.read_excel(ruta)

# Ítems que valen 1 si la respuesta es 'Verdadero'
items_verdadero = [2, 4, 7, 9, 11, 12, 14, 16, 17, 18, 20]
# Ítems que valen 1 si la respuesta es 'Falso'
items_falso = [1, 3, 5, 6, 8, 10, 13, 15, 19]

# Factores
factor_afectivo_items = [1, 6, 13, 15, 19]
factor_motivacional_items = [2, 3, 9, 11, 12, 16, 17, 20]
factor_cognitivo_items = [4, 7, 8, 14, 18]

def calcular_puntaje(respuestas):
    puntaje_total = 0
    puntajes = {}

    for i in range(1, 21):
        item_col = f'Item{i}'  
        respuesta = respuestas.get(item_col, '')
        respuesta = str(respuesta).strip().upper()

        # Manejo de valores nulos o vacíos
        if respuesta in ('', 'NAN', 'NONE'):
            puntaje = 0
        elif i in items_verdadero and respuesta.startswith('V'):
            puntaje = 1
        elif i in items_falso and respuesta.startswith('F'):
            puntaje = 1
        else:
            puntaje = 0

        puntajes[item_col] = puntaje
        puntaje_total += puntaje

    # Cálculo de factores
    factor_afectivo = sum(puntajes[f'Item{i}'] for i in factor_afectivo_items)
    factor_motivacional = sum(puntajes[f'Item{i}'] for i in factor_motivacional_items)
    factor_cognitivo = sum(puntajes[f'Item{i}'] for i in factor_cognitivo_items)

    # Clasificación de riesgo 
    if puntaje_total <= 3:
        riesgo = "Ningún o mínimo riesgo"
    elif puntaje_total <= 8:
        riesgo = "Riesgo bajo"
    elif puntaje_total <= 14:
        riesgo = "Riesgo moderado"
    else:
        riesgo = "Riesgo alto"

    return puntaje_total, factor_afectivo, factor_motivacional, factor_cognitivo, riesgo

# Procesar todos los sujetos 
resultados = []
for idx, row in df.iterrows():
    sujeto = row.iloc[0]
    respuestas = row.to_dict()  # Usar to_dict() para evitar problemas con índices
    total, afectivo, motivacional, cognitivo, riesgo = calcular_puntaje(respuestas)
    resultados.append([sujeto, total, afectivo, motivacional, cognitivo, riesgo])

# Crear DataFrame de resultados
df_resultados = pd.DataFrame(resultados, columns=[
    'Sujeto', 'Puntaje Total', 'Factor Afectivo',
    'Factor Motivacional', 'Factor Cognitivo', 'Clasificación de Riesgo'
])

# Guardar resultados (igual que antes)
df_resultados.to_excel('resultados_desesperanza.xlsx', index=False)
print("Resultados guardados en 'resultados_desesperanza.xlsx'")

