import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_with_table(df, column):
    """
    Genera un gráfico de pastel y una tabla resumen
    para una columna categórica de un DataFrame.
    """
    counts = df[column].value_counts()
    tabla = pd.DataFrame({
        'Respuesta': counts.index,
        'Conteo': counts.values
    })

    fig, ax = plt.subplots(1, 2, figsize=(10,6))

    # Pie chart
    ax[0].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax[0].set_title(f'Valores de {column}')

    # Tabla
    ax[1].axis('off')
    tabla_plot = ax[1].table(cellText=tabla.values,
                             colLabels=tabla.columns,
                             loc='center',
                             cellLoc='center')
    tabla_plot.auto_set_font_size(False)
    tabla_plot.set_fontsize(10)
    tabla_plot.scale(1.2, 1.2)

    return fig



def plot_equipment_analysis(df, column):
    """
    Analiza una columna numérica de equipamiento tecnológico.
    Clasifica en 'SI' si el valor > 0 y 'NO' si el valor == 0.
    Genera un gráfico de pastel y una tabla resumen.
    
    Parámetros:
    df      : DataFrame de pandas
    column  : str, nombre de la columna a analizar
    """
    # Clasificación binaria
    clasificacion = df[column].apply(lambda x: 'SI' if x > 0 else 'NO')
    counts = clasificacion.value_counts()

    # Crear tabla resumen
    tabla = pd.DataFrame({
        'Valor': counts.index,
        'Frecuencia': counts.values
    })

    # Crear figura
    fig, ax = plt.subplots(1, 2, figsize=(10,6))

    # Pie chart
    ax[0].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax[0].set_title(f'Equipamiento: {column}')

    # Tabla
    ax[1].axis('off')
    tabla_plot = ax[1].table(cellText=tabla.values,
                             colLabels=tabla.columns,
                             loc='center',
                             cellLoc='center')
    tabla_plot.auto_set_font_size(False)
    tabla_plot.set_fontsize(10)
    tabla_plot.scale(1.2, 1.2)

    return fig




def plot_equipment_med(df, column):
    """
    Analiza una columna numérica de equipamiento tecnológico.
    Clasifica en 'SI' si el valor > 0 y 'NO' si el valor == 0.
    Genera un gráfico de pastel y una tabla resumen.
    
    Parámetros:
    df      : DataFrame de pandas
    column  : str, nombre de la columna a analizar
    """
    # Clasificación binaria
    clasificacion = df[column].apply(lambda x: 'SI' if x > 0 else 'NO')
    counts = clasificacion.value_counts()

    # Crear tabla resumen
    tabla = pd.DataFrame({
        'Valor': counts.index,
        'Frecuencia': counts.values
    })

    # Crear figura
    fig, ax = plt.subplots(1, 2, figsize=(10,6))

    # Pie chart
    ax[0].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax[0].set_title(f'Equipamiento médico: {column}')

    # Tabla
    ax[1].axis('off')
    tabla_plot = ax[1].table(cellText=tabla.values,
                             colLabels=tabla.columns,
                             loc='center',
                             cellLoc='center')
    tabla_plot.auto_set_font_size(False)
    tabla_plot.set_fontsize(10)
    tabla_plot.scale(1.2, 1.2)

    return fig