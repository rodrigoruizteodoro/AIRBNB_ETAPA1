import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.title('Airbnb')
st.header("App")
st.write("Sitio que te permite analizar de forma visual la base de datos de airbnb")

@st.cache
def load_data(nrows):
    airbnb = pd.read_csv("airbnb_clean2.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return airbnb

st.sidebar.image("airbnb.jpeg")
st.sidebar.markdown("##")

loading_data = st.text('Loading airbnb data...')
airbnb = load_data(101)
loading_data.text("Done!")

data_description = st.sidebar.checkbox("Resumen de la base de datos")
if data_description:
    st.header("Base de datos")
    st.dataframe(airbnb)


@st.cache
def room_clase(room_class):
    filter_room=airbnb[airbnb["room_type"]==room_class]
    
    return filter_room

select_type= st.sidebar.selectbox("Seleccione tipo de residencia", airbnb['room_type'].unique())
search_class=st.sidebar.button("Busca residencia")

if(search_class):
    filter_type_if= room_clase(select_type)
    count_row= filter_type_if.shape[0]
    st.write(f"Total: {count_row} de resultados")

    st.dataframe(filter_type_if)

delegacion = st.sidebar.selectbox("Selecciona la delegación", airbnb['neighbourhood'].unique())
if st.sidebar.button("Filtrar por delegación"):
    filtrar_dele =airbnb[(airbnb["neighbourhood"]==delegacion)]
    st.write(f"Opcion seleccionada: {delegacion!r}")
    st.write(airbnb.query(f"""neighbourhood==@delegacion"""))
    st.map(filtrar_dele)
    st.markdown("_")

price_valores = st.sidebar.checkbox("Rango de precios")
if price_valores:
    st.header("Base de datos")
    valores = st.slider('price', 5000, 999998, 0)

    
#GRÁFICOS
hisplot_by_price= st.sidebar.checkbox("Histograma: Distribución de precios")
if hisplot_by_price:
    fig, ax = plt.subplots()
    ax.hist(airbnb.price)
    st.header("Distribución de precios de todas las residencias")
    st.pyplot(fig)
    st.markdown("_")

typeroom_price= st.sidebar.checkbox("Relacion entre precio y tipo de residencia")
if typeroom_price:
    fig, ax = plt.subplots()
    y= airbnb["price"]
    x=airbnb["room_type"]
    ax.barh(x,y)
    ax.set_ylabel("Tipo de residencia")
    ax.set_xlabel("Precio")
    st.header("Relacion entre tipo de residencia y precio")
    st.pyplot(fig)
    st.markdown("_")

neighbourhood_price= st.sidebar.checkbox("Relacion entre precio y vecindario")
if typeroom_price:
    fig, ax = plt.subplots()
    y= airbnb["price"]
    x=airbnb["neighbourhood"]
    ax.barh(x,y)
    ax.set_ylabel("Precio")
    ax.set_xlabel("Vecindario")
    st.header("Relacion entre tipo de precio y vecindario")
    st.pyplot(fig)
    st.markdown("_")

st.markdown("**Analysis**")
st.markdown("1.Distribución de los precios de todas las casas: Dentro de este código podemos tener un análisis de cuáles son las casas con mayor número de rentas en CDMX de acuerdo al precio, y podemos ver que en este rango las que tiene un mayor “éxito” son las de menor precio. 2.Tenemos 4 tipos de residencias, y notamos que los que tienen  un mayor rango de precios son las casas o departamentos completos,  pues estos llegan a costar hasta 17,500 pesos; mientras que los cuartos privados en casas o departamentos tienen un precio menor, esto puede ser por las comodidades que cada uno tiene. 3.Dependiendo el vecindario, el precio puede llegar a variar por la plusvalía y ubicación que este tiene a otros puntos importantes. En este caso, Cuauhtémoc es en donde el precio se eleva más y los lugares con menor precio se encuentran en Tlalpan")


