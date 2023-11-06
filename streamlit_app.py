# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection


st.set_page_config(
   page_title="Teacher",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

# url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

url = "https://docs.google.com/spreadsheets/d/1eCnGwVsKOZMtv6JAM-Ul0OeW5hNTiTzUrNYVsI4fnT0/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Se pued colocar el nombre de la hoja pero solo funciona si es privada si es publica se coloca 
# el numero que aparece en la url del libro de Google Sheet al final 

# data = conn.read(spreadsheet=url, usecols=list(range(2)),worksheet="1452764456")


st.subheader("Courses Taught 💻👨‍💻")

data = conn.read(spreadsheet=url,usecols=list(range(13)), worksheet="1452764456")
st.dataframe(data,hide_index=True)

#  #e1183a   #18e16d

st.bar_chart(data, x="Herramienta",y="No Alumno",color="#CD5C5C",width=3, height=500, use_container_width=True)

total_students = data['No Alumno'].sum()
total_hours = data['Horas'].sum()

summary_tools = data.groupby('Herramienta')['No Alumno','Horas'].sum().sort_values(by='Horas',ascending = True)
summary_institut = data.groupby('Institución')['No Alumno','Horas'].sum().sort_values(by='Horas',ascending = True)

st.write(f"Total Students : {total_students}")
st.write(f"Total Hours :{total_hours}")
st.dataframe(summary_tools)
st.dataframe(summary_institut)


code = ''' 
      st.subheader("Courses Taught 💻👨‍💻")

      data = conn.read(spreadsheet=url,usecols=list(range(13)), worksheet="1452764456")
      st.dataframe(data,hide_index=True)



      st.bar_chart(data, x="Herramienta",y="No Alumno",color="#CD5C5C",width=3, height=500, use_container_width=True)

      total_students = data['No Alumno'].sum()
      total_hours = data['Horas'].sum()

      summary_tools = data.groupby('Herramienta')['No Alumno','Horas'].sum().sort_values(by='Horas',ascending = True)
      summary_institut = data.groupby('Institución')['No Alumno','Horas'].sum().sort_values(by='Horas',ascending = True)

      st.write(f"Total Students : {total_students}")
      st.write(f"Total Hours :{total_hours}")
      st.dataframe(summary_tools)
      st.dataframe(summary_institut)

      '''

st.code(code, language='python')