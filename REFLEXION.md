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

# TP4 — Réflexion avec le Registry et l'API

## 1. Comment indiquer officiellement quel modèle doit être utilisé ?

L'alias `champion` désigne la version retenue dans le Registry. L'application peut la charger avec `models:/churn-model@champion`, et il suffit de déplacer cet alias pour choisir une autre version.

## 2. Comment une application peut-elle utiliser le modèle ?

Elle envoie les données à l'API avec une requête `POST /predict` contenant un JSON. L'API renvoie ensuite la prédiction dans sa réponse.

## 3. Que faut-il faire quand le modèle champion change ?

On met l'alias `champion` sur la nouvelle version, puis on redémarre l'API pour qu'elle la charge. Le code de l'API et celui des applications clientes restent inchangés.