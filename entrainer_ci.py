# ===== 1. Importer les bibliothèques =====
import shutil  # supprimer un dossier existant
import mlflow.sklearn  # enregistrer le modèle dans un dossier
import pandas as pd  # lire et préparer les données
from sklearn.ensemble import RandomForestClassifier

# ===== 2. Lire et préparer les données =====
df = pd.read_csv("churn_data.csv")

# get_dummies : transformer le texte « abonnement » en colonnes 0/1
X = pd.get_dummies(df.drop(columns=["churn"]), columns=["abonnement"])
y = df["churn"]

# ===== 3. Entraîner le modèle =====
# random_state=42 : même résultat à chaque exécution (indispensable en CI)
modele = RandomForestClassifier(n_estimators=100, random_state=42)
modele.fit(X, y)

# ===== 4. Écrire le modèle dans le dossier « model » =====
# save_model refuse d'écrire dans un dossier non vide : on supprime l'ancien d'abord
# (indispensable pour relancer le script, ou pour un deuxième build Jenkins)
shutil.rmtree("model", ignore_errors=True)

# Pas de serveur MLflow ici : on écrit directement dans un dossier ordinaire,
# exactement comme exporter_modele.py au TP5.
mlflow.sklearn.save_model(
    modele,
    "model",
    serialization_format="cloudpickle"
)

print("Modèle entraîné et écrit dans le dossier model/")