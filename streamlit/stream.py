#TO RUN : streamlit run streamlit/stream.py
import streamlit as st
import requests

BACKEND_URL = "https://immo-eliza-deployment-max.onrender.com"

LANGUAGES = {
    "English": {
        "title": "Immo Eliza Prediction",
        "instruction": "Fill in this form to get an evaluating price on your property :",
        "type_question": "Is it a house or an apartment ?",
        "livable_surface": "Livable surface :",
        "total_surface": "Total surface :",
        "property_state": "Property state :",
        "selected_option": "Your selected option :",
        "build_year": "Build year :",
        "zipcode": "Enter Belgian Zipcode:",
        "bedrooms": "Amount of bedrooms :",
        "simming_pool": "Swimming pool :",
        "garage": "Garage :",
        "terrace": "Terrace :",
        "en_cons": "Energy consumption (kWh/m2/year) :",
        "preschool": "Preschool distance (m) :",
        "train_station": "Train station distance (m) :",
        "supermarket": "Supermarket distance (m) :",
        "nearest_city": "Nearest city distance (km) :",
        "button": "Predict",
        "spinner": "Calculating...",
        "warning": "Warning: please fill in a zipcode.",
        "error": "Something went wrong... Please try again later."
    },
    "Français": {
        "title": "Immo Eliza Prédiction",
        "instruction": "Remplissez ce formulaire pour obtenir une estimation de prix de vente de votre propriété :",
        "type_question": "Est-ce une maison ou un appartement ?",
        "livable_surface": "Surface habitable :",
        "total_surface": "Surface totale :",
        "property_state": "Etat de la propriété :",
        "selected_option": "Votre option sélectionnée :",
        "build_year": "Année de construction :",
        "zipcode": "Code postal :",
        "bedrooms": "Nombre de chambres :",
        "swimming_pool": "Piscine :",
        "garage": "Garage :",
        "terrace": "Terrace :",
        "en_cons": "Consommation d'énergie (kWh/m2/year) :",
        "preschool": "Distance de la plus proche école maternelle (m) :",
        "train_station": "Distance de la gare (m) :",
        "supermarket": "Distance d'un supermarché (m) :",
        "nearest_city": "Distance de la ville la plue proche (km) :",
        "button": "Estimer",
        "spinner": "En cours...",
        "warning": "Attention: veuillez remplir le code postal.",
        "error": "Quelque chose s'est mal passé... Veuillez réessayer plus tard."
    }
}


selected_language = st.sidebar.selectbox("Language / Langue", options=["English", "Français"])

text = LANGUAGES[selected_language]

st.title(text["title"])

st.write(text["instruction"])

inputs = {}
inputs["property_type"] = st.selectbox(text["type_question"], ("house", "apartment"))

inputs["livable_surface"] = st.slider(text["livable_surface"], 0, 1000, 100, 10)

inputs["total_surface"] = st.slider(text["total_surface"], 0, 1000, 100, 10)

states = ['Normal', 'To renovate', 'Excellent', 'New', 'Fully renovated', 
           'To demolish', 'Under construction', 'To restore']
inputs["property_state"] = st.pills(text["property_state"], states, selection_mode="single")
st.markdown(f"{text["selected_option"]} {inputs["property_state"]}.")

inputs["build_year"] = st.slider(text["build_year"], min_value=1500, max_value=2030, value=1985)

inputs["postcode"] = st.text_input(text["zipcode"], value="", placeholder="1000", max_chars=4)

provinces = ['antwerp', 'limburg', 'east-flanders', 'vlaams-brabant', 
             'west-flanders', 'brussels', 'hainaut', 'liege', 'luxembourg',
             'namur', 'brabant-wallon']

inputs["province"] = st.selectbox("Province :", provinces)
inputs["bedroom_count"] = st.slider(text["bedrooms"], 0, 20, 1)
inputs["swimming_pool"] = st.toggle(text["swimming_pool"])
inputs["terrace"] = st.toggle(text["terrace"])
inputs["garage"] = st.toggle(text["garage"])
inputs["energy_consumption_kWh"] = st.number_input(text["en_cons"], value=150, step=None)

inputs["preschool_distance_m"] = st.slider(text["preschool"], 0, 10000, 350, 50)
inputs["train_station_distance_m"] = st.slider(text["train_station"], 0, 10000, 500, 50)
inputs["supermarket_distance_m"] = st.slider(text["supermarket"], 0, 10000, 200, 50)
inputs["nearest_city_distance_km"] = st.number_input(text["nearest_city"], value=0.5, step=0.5)

if st.button(text["button"]):
    if not (inputs["postcode"]):
        st.warning(text["warning"])
    else:
        with st.spinner(text["spinner"], show_time=True):
            res = requests.post(url=f"{BACKEND_URL}/predict", json=inputs)

        if res.status_code == 200:
            number = res.json()["prediction"]
            result = f"{number:,.2f} €".replace(",", " ").replace(".", ",")
            st.subheader(f"Evaluation : {result}")
        elif res.status_code == 400:
            error_msg = res.json().get('detail', 'An error occurred')
            st.error(f"Error: {error_msg}")
        else:
            st.error(text["error"])
            st.error(f"Server returned status {res.status_code}")
        