import streamlit as st
import pandas as pd
import os
from funciones import plot_pie_with_table, plot_equipment_analysis, plot_equipment_med

st.title("Analisis de respuestas -Telemedicina-♟️")
st.subheader("Respuestas de 395 unidades")

# Usar ruta relativa que funcione tanto local como en Streamlit Cloud
file = os.path.join(os.path.dirname(__file__), "data", "especificaciones_clean.xlsx")
df = pd.read_excel(file)
cols_si_no = ["Triage","Consulta","Seguimiento","Interconsulta","Asesoría médica","Monitoreo","Interpretación diagnóstica","Pase de visita","Educación en salud","Coordinación de servicios en salud","Mentoría","Promoción de la salud"]
df_medica = df[cols_si_no]
st.write("Datos cargados exitosamente. 💾")
st.subheader("Análisis de columnas de cosas medicas que no se como englobar 🩺")
columna = st.selectbox("Selecciona la columna para el análisis:", df_medica.columns)
fig = plot_pie_with_table(df_medica, columna)
st.plotly_chart(fig, use_container_width=True)


    # Equipo tecnologico
st.subheader("Análisis de equipamiento tecnológico 🖥️")
cols_equipamiento = ["Computadora de Escritorio","Computadora Portatil (laptop)","Tableta Electrónica","Telefóno Inteligente","Telefóno Convencional","UPS o Nobreak","Cámara WEB","Audifonos con microfóno ","Sistema de Videoconferencia","Plataforma de Videoconferencia (VC)","Licencias de Software de VC","Plataforma de telemedicina"]
df_equipamiento = df[cols_equipamiento]
columna_equip = st.selectbox("Selecciona la columna de equipamiento para el análisis:", df_equipamiento.columns)
fig_equip = plot_equipment_analysis(df_equipamiento, columna_equip)
st.plotly_chart(fig_equip, use_container_width=True)


    #Equipo medico
st.subheader("Análisis de equipamiento médico 🩻")
cols_equipamiento_med = ["Esfigmomanómetro","Oxímetro de Pulso","Termómetro","Estadímetro","Báscula","Glucómetro","Electrocardiógrafo Portatil (1-6 derivaciones)","Estuche Diagnóstico","Estetoscopio","Estación de telemedicina","Estación telerradiología","Estación telemastografía"]
df_equipamiento_med = df[cols_equipamiento_med]
columna_equip_med = st.selectbox("Selecciona la columna de equipamiento médico para el análisis:", df_equipamiento_med.columns)
fig_equip_med = plot_equipment_med(df_equipamiento_med, columna_equip_med)
st.plotly_chart(fig_equip_med, use_container_width=True)