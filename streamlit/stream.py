#TO RUN : streamlit run stream.py [-- script args]
import streamlit as st
import json
import requests

BACKEND_URL = "https://immo-eliza-deployment-max.onrender.com"

st.title("My API Title")

st.write("A paragraph...")

inputs = {}
inputs["property_type"] = st.selectbox("Is it a house or apart?", ("house", "apartment"))

inputs["livable_surface"] = st.slider("Livable surface: ", 0, 1000, 10)

inputs["total_surface"] = st.slider("Total surface: ", 0, 1000, 10)

states = ['Normal', 'To renovate', 'Excellent', 'New', 'Fully renovated', 
           'To demolish', 'Under construction', 'To restore']
inputs["property_state"] = st.pills("Property state", states, selection_mode="single")
st.markdown(f"Your selected options: {inputs["property_state"]}.")
inputs["build_year"] = st.slider("Build year :", 1500, 2030, 1)

inputs["latitude"] = st.number_input("Latitude", min_value=49.3, max_value=51.3)
inputs["longitude"] = st.number_input("Longitude", min_value=2.32, max_value=6.24)

provinces = ['antwerp', 'limburg', 'east-flanders', 'vlaams-brabant', 
             'west-flanders', 'brussels', 'hainaut', 'liege', 'luxembourg',
             'namur', 'brabant-wallon']

inputs["province"] = st.selectbox("Province :", provinces)
inputs["bedroom_count"] = st.slider("Number of bedrooms :", 0, 20, 1)
inputs["swimming_pool"] = st.toggle("Swimming pool")
inputs["terrace"] = st.toggle("Terrace")
inputs["garage"] = st.toggle("Garage")
inputs["energy_consumption_kWh"] = st.number_input("energy_consumption_kWh :", value=150)

inputs["preschool_distance_m"] = st.slider("preschool_distance_m :", 0, 10000, 50)
inputs["train_station_distance_m"] = st.slider("train_station_distance_m :", 0, 10000, 50)
inputs["supermarket_distance_m"] = st.slider("supermarket_distance_m :", 0, 10000, 50)
inputs["nearest_city_distance_km"] = st.number_input("nearest_city_distance_km :", value=0.5)

if st.button("Predict"):
    res = requests.post(url=f"{BACKEND_URL}/predict", json=inputs)

    st.subheader(f"Response from api: {res}")
    if res.status_code == 200:
        st.write(res.json())
    else:
        st.error(f"Backend Error {res.status_code}: Look at your Render Logs!")
        st.text(res.text)