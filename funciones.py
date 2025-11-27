import pandas as pd
import plotly.graph_objects as go

def plot_pie_with_table(df, column):
    """
    Genera un gráfico de pastel interactivo y un DataFrame
    para una columna categórica de un DataFrame usando Plotly.
    
    Retorna:
    fig : figura de Plotly con el gráfico de pastel
    data_df : DataFrame con los datos tabulados
    """
    counts = df[column].value_counts()
    percentages = (counts / counts.sum() * 100).round(1)
    
    # Crear DataFrame para mostrar
    data_df = pd.DataFrame({
        'Respuesta': counts.index,
        'Conteo': counts.values,
        'Porcentaje': [f"{p}%" for p in percentages.values]
    })
    
    # Crear figura solo con pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=counts.index,
                values=counts.values,
                textinfo='label+percent',
                hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<extra></extra>',
                marker=dict(line=dict(color='white', width=2))
            )
        ]
    )
    
    fig.update_layout(
        height=450,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        title_text=f"Análisis de {column}",
        title_x=0.5,
        title_font_size=18,
        margin=dict(t=80, b=80, l=20, r=20)
    )
    
    return fig, data_df


def plot_equipment_analysis(df, column):
    """
    Analiza una columna numérica de equipamiento tecnológico.
    Clasifica en 'SI' si el valor > 0 y 'NO' si el valor == 0.
    Genera un gráfico de pastel interactivo y un DataFrame.
    
    Parámetros:
    df      : DataFrame de pandas
    column  : str, nombre de la columna a analizar
    
    Retorna:
    fig : figura de Plotly con el gráfico de pastel
    data_df : DataFrame con los datos tabulados
    """
    # Clasificación binaria
    clasificacion = df[column].apply(lambda x: 'SI' if x > 0 else 'NO')
    counts = clasificacion.value_counts()
    percentages = (counts / counts.sum() * 100).round(1)
    
    # Crear DataFrame para mostrar
    data_df = pd.DataFrame({
        'Estado': counts.index,
        'Frecuencia': counts.values,
        'Porcentaje': [f"{p}%" for p in percentages.values]
    })
    
    # Colores personalizados
    colors = {'SI': '#2ecc71', 'NO': '#e74c3c'}
    pie_colors = [colors.get(label, '#95a5a6') for label in counts.index]
    
    # Crear figura solo con pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=counts.index,
                values=counts.values,
                textinfo='label+percent',
                hovertemplate='<b>%{label}</b><br>Unidades: %{value}<br>Porcentaje: %{percent}<extra></extra>',
                marker=dict(colors=pie_colors, line=dict(color='white', width=2))
            )
        ]
    )
    
    fig.update_layout(
        height=450,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        title_text=f"Equipamiento Tecnológico: {column}",
        title_x=0.5,
        title_font_size=18,
        margin=dict(t=80, b=80, l=20, r=20)
    )
    
    return fig, data_df


def plot_equipment_med(df, column):
    """
    Analiza una columna numérica de equipamiento médico.
    Clasifica en 'SI' si el valor > 0 y 'NO' si el valor == 0.
    Genera un gráfico de pastel interactivo y un DataFrame.
    
    Parámetros:
    df      : DataFrame de pandas
    column  : str, nombre de la columna a analizar
    
    Retorna:
    fig : figura de Plotly con el gráfico de pastel
    data_df : DataFrame con los datos tabulados
    """
    # Clasificación binaria
    clasificacion = df[column].apply(lambda x: 'SI' if x > 0 else 'NO')
    counts = clasificacion.value_counts()
    percentages = (counts / counts.sum() * 100).round(1)
    
    # Crear DataFrame para mostrar
    data_df = pd.DataFrame({
        'Estado': counts.index,
        'Frecuencia': counts.values,
        'Porcentaje': [f"{p}%" for p in percentages.values]
    })
    
    # Colores personalizados
    colors = {'SI': '#3498db', 'NO': '#95a5a6'}
    pie_colors = [colors.get(label, '#bdc3c7') for label in counts.index]
    
    # Crear figura solo con pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=counts.index,
                values=counts.values,
                textinfo='label+percent',
                hovertemplate='<b>%{label}</b><br>Unidades: %{value}<br>Porcentaje: %{percent}<extra></extra>',
                marker=dict(colors=pie_colors, line=dict(color='white', width=2))
            )
        ]
    )
    
    fig.update_layout(
        height=450,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        title_text=f"Equipamiento Médico: {column}",
        title_x=0.5,
        title_font_size=18,
        margin=dict(t=80, b=80, l=20, r=20)
    )
    
    return fig, data_df