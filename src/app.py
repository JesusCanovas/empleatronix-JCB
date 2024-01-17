import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('EMPLEATRONIX - Jesús Cánovas')

st.markdown("Todos los datos sobre los empleados en una aplicación..")

# Cargar datos desde el archivo CSV
file_path = './data/employees.csv'
df = pd.read_csv(file_path)

# Mostrar el DataFrame
st.dataframe(df)

st.divider()

# Widgets para controlar la apariencia del gráfico
col = st.columns(3)
color_s = col[0].color_picker("Elige un color para las barras", value='#3498db')
show_name = col[1].toggle("Mostrar el nombre", value=1)
show_salary = col[2].toggle("Mostrar el salario")

# Contenido del gráfico
full_name = df['full name']
salary = df['salary']

fig, ax = plt.subplots()
bar = ax.barh(full_name, salary, color=color_s)
plt.xticks(rotation=90)
plt.xlim(0, 4500)
# Condiciones sobre que información mostrar según que Widget esté activado
if show_salary:
    ax.bar_label(container=bar, fmt="%d€")

if not show_name:
    plt.yticks([])
    
# Mostrar el gráfico
st.pyplot(fig)

st.divider()
# Firma de la página
st.markdown("© Jesús Cánovas Barqueros - CPIFP Alan Turing")
