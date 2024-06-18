import streamlit as st
import requests

# Définir l'URL de votre API FastAPI
API_URL = "http://127.0.0.1:8000/predict"

# Titre de l'application
st.title("Prédiction de Survie du Titanic")
st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg", caption="RMS Titanic", width=500)

# Entrées de l'utilisateur
stay_class = st.selectbox("Classe de Séjour (1 = Première, 2 = Deuxième, 3 = Troisième)", [1, 2, 3])
sex = st.selectbox("Sexe (0 = Homme, 1 = Femme)", [0, 1])
ticket_price = st.number_input("Prix du Ticket", min_value=0.0, step=0.01)

# Bouton de prédiction
if st.button("Prédire"):
    # Construire le payload pour l'API
    payload = {
        "stay_class": stay_class,
        "sex": sex,
        "ticket_price": ticket_price
    }

    # Envoyer la requête POST à l'API
    response = requests.post(API_URL, json=payload)

    # Vérifier la réponse de l'API
    if response.status_code == 200:
        prediction = response.json().get("Survival Prediction")
        if prediction == 1:
            st.success("Félicitations! La prédiction de survie est : Oui")
            st.balloons()
        else:
            st.error("Malheureusement, la prédiction de survie est : Non")
            st.snow()
    else:
        st.error("Erreur lors de la prédiction. Veuillez réessayer.")
