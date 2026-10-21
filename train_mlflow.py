# ===== 1. Importer les bibliothèques =====
import pandas as pd  # Lire et manipuler le fichier CSV
import mlflow  # Module principal de MLflow
import mlflow.sklearn  # Intégration de MLflow avec scikit-learn

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ===== 2. Charger et préparer les données =====
df = pd.read_csv("churn_data.csv")

# Transformer la colonne texte 'abonnement' en colonnes numériques (0/1)
X = pd.get_dummies(
    df[
        [
            "age",
            "salaire",
            "abonnement",
            "anciennete",
            "consommation",
        ]
    ],
    drop_first=True,
)

# Variable cible : 1 = le client part, 0 = le client reste
y = df["churn"]

# Séparer les données : 80 % pour l'entraînement, 20 % pour le test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# ===== 3. Choisir l'expérience MLflow =====
mlflow.set_experiment("churn-prediction")


# ===== 4. Entraîner et enregistrer le modèle =====
with mlflow.start_run(run_name="essai-1"):

    # Créer le modèle avec ses paramètres
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
    )

    # Entraîner le modèle
    model.fit(X_train, y_train)

    # Prédire les résultats sur les données de test
    y_pred = model.predict(X_test)

    # Calculer la précision du modèle
    acc = accuracy_score(y_test, y_pred)

    # ===== 5. Enregistrer les résultats dans MLflow =====

    # Enregistrer les paramètres
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)

    # Enregistrer la métrique de performance
    mlflow.log_metric("accuracy", acc)

    # Enregistrer le modèle entraîné
    mlflow.sklearn.log_model(
        sk_model=model,
        name="model",
        serialization_format="cloudpickle",
    )

    # Afficher la précision dans le terminal
    print("Accuracy :", acc)