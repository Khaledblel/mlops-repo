# Projet de prédiction de churn avec MLflow

Ce projet montre comment entraîner un modèle de classification pour prédire si un client va partir (churn) ou non, puis enregistrer les résultats avec MLflow.

Le but est d'apprendre les bases de l'MLOps :
- générer des données,
- entraîner plusieurs modèles,
- comparer leurs performances,
- enregistrer les runs dans MLflow,
- charger un modèle précis à partir d'un run.

## Objectif

Le modèle prédit si un client va partir ou rester en fonction de variables comme :
- l'âge,
- le salaire,
- l'ancienneté,
- la consommation,
- le type d'abonnement.

## Structure du projet

- `generate_data.py` : génère les données d'entraînement et crée le fichier `churn_data.csv`.
- `train_mlflow.py` : entraîne 3 modèles avec des paramètres différents et enregistre les résultats dans MLflow.
- `lire_runs.py` : lit les runs MLflow et retrouve le meilleur modèle selon le score F1.
- `charger_modele.py` : recharge un modèle à partir d'un run précis et fait une prédiction.
- `churn_data.csv` : jeu de données utilisé pour entraîner le modèle.
- `mlruns/` : dossiers générés par MLflow pour stocker les runs.
- `mlflow.db` : base de données locale MLflow.
- `model.pkl` : modèle sérialisé éventuel généré pendant les travaux.

## Prérequis

Il faut avoir Python installé ainsi que les dépendances suivantes :
- pandas
- numpy
- scikit-learn
- mlflow

Le projet est prévu pour être exécuté dans un environnement virtuel.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install pandas numpy scikit-learn mlflow
```

## Utilisation

### 1. Générer les données

```bash
python generate_data.py
```

### 2. Entraîner les modèles

```bash
python train_mlflow.py
```

Cette commande crée plusieurs runs MLflow avec des essais différents.

### 3. Lire les résultats MLflow

```bash
python lire_runs.py
```

Cette commande permet de retrouver le meilleur modèle selon la métrique `f1`.

### 4. Charger un modèle et faire une prédiction

```bash
python charger_modele.py
```

Cela recharge le meilleur modèle enregistré dans MLflow et fait une prédiction sur un client exemple.

## Exemple d'interface MLflow

Pour visualiser les runs dans l'interface MLflow :

```bash
mlflow ui
```

Puis ouvrir l'URL affichée dans le navigateur, généralement :

```text
http://localhost:5000
```

## Explication rapide du workflow

1. On génère des données synthétiques.
2. On entraîne plusieurs modèles avec des hyperparamètres différents.
3. MLflow enregistre les paramètres et les métriques de chaque run.
4. On compare les résultats pour choisir le meilleur modèle.
5. On recharge le modèle d'un run précis pour l'utiliser ensuite.
