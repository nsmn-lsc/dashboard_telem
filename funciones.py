import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_pie_with_table(df, column):
    """
    Genera un gráfico de pastel interactivo con tabla de datos
    para una columna categórica de un DataFrame usando Plotly.
    """
    counts = df[column].value_counts()
    percentages = (counts / counts.sum() * 100).round(1)
    
    # Crear subplots: pie chart y tabla
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "pie"}, {"type": "table"}]],
        column_widths=[0.6, 0.4],
        subplot_titles=(f'Distribución de {column}', 'Resumen de datos')
    )
    
    # Agregar pie chart
    fig.add_trace(
        go.Pie(
            labels=counts.index,
            values=counts.values,
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<extra></extra>',
            marker=dict(line=dict(color='white', width=2))
        ),
        row=1, col=1
    )
    
    # Agregar tabla
    fig.add_trace(
        go.Table(
            header=dict(
                values=['<b>Respuesta</b>', '<b>Conteo</b>', '<b>%</b>'],
                fill_color='paleturquoise',
                align='center',
                font=dict(size=12, color='black')
            ),
            cells=dict(
                values=[counts.index, counts.values, [f"{p}%" for p in percentages.values]],
                fill_color='lavender',
                align='center',
                font=dict(size=11, color='black')
            )
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        title_text=f"Análisis de {column}",
        title_x=0.5
    )
    
    return fig


def plot_equipment_analysis(df, column):
    """
    Analiza una columna numérica de equipamiento tecnológico.
    Clasifica en 'SI' si el valor > 0 y 'NO' si el valor == 0.
    Genera un gráfico de pastel interactivo con tabla usando Plotly.
    
    Parámetros:
    df      : DataFrame de pandas
    column  : str, nombre de la columna a analizar
    """
    # Clasificación binaria
    clasificacion = df[column].apply(lambda x: 'SI' if x > 0 else 'NO')
    counts = clasificacion.value_counts()
    percentages = (counts / counts.sum() * 100).round(1)
    
    # Crear subplots: pie chart y tabla
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "pie"}, {"type": "table"}]],
        column_widths=[0.6, 0.4],
        subplot_titles=(f'Equipamiento: {column}', 'Estadísticas')
    )
    
    # Colores personalizados
    colors = {'SI': '#2ecc71', 'NO': '#e74c3c'}
    pie_colors = [colors.get(label, '#95a5a6') for label in counts.index]
    
    # Agregar pie chart
    fig.add_trace(
        go.Pie(
            labels=counts.index,
            values=counts.values,
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Unidades: %{value}<br>Porcentaje: %{percent}<extra></extra>',
            marker=dict(colors=pie_colors, line=dict(color='white', width=2))
        ),
        row=1, col=1
    )
    
    # Agregar tabla
    fig.add_trace(
        go.Table(
            header=dict(
                values=['<b>Estado</b>', '<b>Frecuencia</b>', '<b>%</b>'],
                fill_color='paleturquoise',
                align='center',
                font=dict(size=12, color='black')
            ),
            cells=dict(
                values=[counts.index, counts.values, [f"{p}%" for p in percentages.values]],
                fill_color='lavender',
                align='center',
                font=dict(size=11, color='black')
            )
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        title_text=f"Análisis de Equipamiento Tecnológico: {column}",
        title_x=0.5
    )
    
    return fig


def plot_equipment_med(df, column):
    """
    Analiza una columna numérica de equipamiento médico.
    Clasifica en 'SI' si el valor > 0 y 'NO' si el valor == 0.
    Genera un gráfico de pastel interactivo con tabla usando Plotly.
    
    Parámetros:
    df      : DataFrame de pandas
    column  : str, nombre de la columna a analizar
    """
    # Clasificación binaria
    clasificacion = df[column].apply(lambda x: 'SI' if x > 0 else 'NO')
    counts = clasificacion.value_counts()
    percentages = (counts / counts.sum() * 100).round(1)
    
    # Crear subplots: pie chart y tabla
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "pie"}, {"type": "table"}]],
        column_widths=[0.6, 0.4],
        subplot_titles=(f'Equipamiento Médico: {column}', 'Estadísticas')
    )
    
    # Colores personalizados
    colors = {'SI': '#3498db', 'NO': '#95a5a6'}
    pie_colors = [colors.get(label, '#bdc3c7') for label in counts.index]
    
    # Agregar pie chart
    fig.add_trace(
        go.Pie(
            labels=counts.index,
            values=counts.values,
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Unidades: %{value}<br>Porcentaje: %{percent}<extra></extra>',
            marker=dict(colors=pie_colors, line=dict(color='white', width=2))
        ),
        row=1, col=1
    )
    
    # Agregar tabla
    fig.add_trace(
        go.Table(
            header=dict(
                values=['<b>Estado</b>', '<b>Frecuencia</b>', '<b>%</b>'],
                fill_color='lightblue',
                align='center',
                font=dict(size=12, color='black')
            ),
            cells=dict(
                values=[counts.index, counts.values, [f"{p}%" for p in percentages.values]],
                fill_color='aliceblue',
                align='center',
                font=dict(size=11, color='black')
            )
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        title_text=f"Análisis de Equipamiento Médico: {column}",
        title_x=0.5
    )
    
    return fig