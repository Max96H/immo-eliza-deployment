#TO RUN : streamlit run streamlit/stream.py
import streamlit as st
import requests

BACKEND_URL = "https://immo-eliza-deployment-max.onrender.com"

st.title("Immo Eliza Prediction")

st.write("Fill in this form to get an evaluating price on your property :")

inputs = {}
inputs["property_type"] = st.selectbox("Is it a house or apartment?", ("house", "apartment"))

inputs["livable_surface"] = st.slider("Livable surface : ", 0, 1000, 100, 10)

inputs["total_surface"] = st.slider("Total surface : ", 0, 1000, 100, 10)

states = ['Normal', 'To renovate', 'Excellent', 'New', 'Fully renovated', 
           'To demolish', 'Under construction', 'To restore']
inputs["property_state"] = st.pills("Property state :", states, selection_mode="single")
st.markdown(f"Your selected option : {inputs["property_state"]}.")

inputs["build_year"] = st.slider("Build year :", min_value=1500, max_value=2030, value=1985)

inputs["postcode"] = st.text_input("Zipcode :", value="", placeholder="1000", max_chars=4)

provinces = ['antwerp', 'limburg', 'east-flanders', 'vlaams-brabant', 
             'west-flanders', 'brussels', 'hainaut', 'liege', 'luxembourg',
             'namur', 'brabant-wallon']

inputs["province"] = st.selectbox("Province :", provinces)
inputs["bedroom_count"] = st.slider("Number of bedrooms :", 0, 20, 1)
inputs["swimming_pool"] = st.toggle("Swimming pool")
inputs["terrace"] = st.toggle("Terrace")
inputs["garage"] = st.toggle("Garage")
inputs["energy_consumption_kWh"] = st.number_input("Energy consumption (kWh/m2/year) :", value=150, step=None)

inputs["preschool_distance_m"] = st.slider("Preschool distance (m) :", 0, 10000, 350, 50)
inputs["train_station_distance_m"] = st.slider("Train station distance (m) :", 0, 10000, 500, 50)
inputs["supermarket_distance_m"] = st.slider("Supermarket distance (m) :", 0, 10000, 200, 50)
inputs["nearest_city_distance_km"] = st.number_input("Nearest city distance (km) :", value=0.5, step=0.5)

if st.button("Predict"):
    if not (inputs["postcode"]):
        st.warning("Please fill in a zipcode !")
    else:
        with st.spinner("Calculating...", show_time=True):
            res = requests.post(url=f"{BACKEND_URL}/predict", json=inputs)

        if res.status_code == 200:
            number = res.json()["prediction"]
            result = f"{number:,.2f} €".replace(",", " ").replace(".", ",")
            st.subheader(f"Evaluation : {result}")
        elif res.status_code == 400:
            error_msg = res.json().get('detail', 'An error occurred')
            st.error(f"Error: {error_msg}")
        else:
            st.error("Something went wrong... Try again later!")
            st.error(f"Server returned status {res.status_code}")
        