import streamlit as st
import requests

# Définir l'URL de votre API FastAPI
API_URL = "http://127.0.0.1:8000/predict"

# Titre de l'application
st.title("Prédiction de Temps de Livraison")

# Saisie des données utilisateur
distance = st.number_input("Distance à parcourir", min_value=0.0, format="%f")

# Bouton de prédiction
if st.button("Prédire"):
    # Créer un payload JSON avec les données d'entrée
    payload = {
        "distance": distance,
    }

    # Envoyer une requête POST à l'API
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Temps estimé de livraison : {result['Time from Pickup to Arrival']} secondes")
    else:
        st.error("Erreur dans la prédiction")
