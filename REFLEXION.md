# Réflexion — TP2

## 1. Quel est le meilleur des 3 modèles ? Peut-on le prouver ?

Oui. On compare les résultats des trois modèles pour trouver celui qui a le meilleur score. Git garde les trois essais dans des commits différents. On peut donc vérifier quel code a été utilisé pour chaque essai.

## 2. Peut-on redonner exactement le modèle de l'Essai 1 ?

Oui. On retrouve le commit de l'Essai 1, puis on restaure le notebook avec `git checkout <commit> -- churn_model.ipynb`. On récupère ainsi exactement le code de cet essai.

## 3. Un camarade peut-il reproduire notre travail sur une autre machine ?

Oui, en grande partie. Avec `git clone`, il récupère le code et l'historique du projet. Il doit ensuite installer Python et les bibliothèques nécessaires pour pouvoir exécuter le projet.

# TP3 — Réflexion avec MLflow

## 1. Quel est le meilleur modèle ? Peut-on le prouver ?

Oui. MLflow enregistre les résultats de chaque entraînement. On peut ensuite classer les runs selon leur score F1 et voir quel modèle est le meilleur. Le résultat reste enregistré dans MLflow.

## 2. Peut-on redonner exactement le modèle de l'Essai 1 ?

Oui. Chaque run possède un identifiant. Avec cet identifiant, on peut recharger le modèle exact avec `mlflow.sklearn.load_model("runs:/<id_du_run>/model")`, sans refaire l'entraînement.

## 3. Un camarade peut-il reproduire notre travail sur une autre machine ?

En partie. Git fournit le code et MLflow garde les paramètres, les résultats et les versions des bibliothèques dans `requirements.txt`. Pour obtenir exactement le même résultat, il faut aussi avoir le même environnement. Docker permettra de mieux régler ce problème dans les prochains TP.