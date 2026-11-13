# ===== 1. Préparer l'environnement AVANT d'importer l'application =====
import os

# app.py lit MODEL_URI au moment de l'import : on lui indique le dossier « model »
os.environ["MODEL_URI"] = "model"

from fastapi.testclient import TestClient  # faux client HTTP, sans serveur ni port
from app import app

client = TestClient(app)

# Un client type, réutilisé par plusieurs tests
CLIENT = {
    "age": 35,
    "salaire": 2500,
    "abonnement": "Standard",
    "anciennete": 1,
    "consommation": 10
}

# ===== 2. Les tests : chaque fonction test_... est exécutée par pytest =====
# assert : si la condition est fausse, le test échoue et le pipeline devient rouge

def test_health():
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.json() == {"status": "ok"}


def test_client_a_risque_part():
    # faible consommation et faible ancienneté : le modèle doit prédire un départ
    reponse = client.post("/predict", json=CLIENT)
    assert reponse.status_code == 200
    assert reponse.json()["churn"] == 1


def test_client_fidele_reste():
    fidele = dict(
        CLIENT,
        age=50,
        salaire=4000,
        abonnement="Premium",
        anciennete=10,
        consommation=80
    )
    reponse = client.post("/predict", json=fidele)
    assert reponse.status_code == 200
    assert reponse.json()["churn"] == 0


def test_donnee_invalide_refusee():
    mauvais = dict(CLIENT, age="abc")
    reponse = client.post("/predict", json=mauvais)
    assert reponse.status_code == 422  # 422 : données invalides