# Prediction-des-prix-de-cloture-des-actions-CAC40

## Sujet
● Analyse journalière de la clôture d’une action d’une entreprise
● Prédiction de tous les cours de clôture des actions de chaque jour des années passées et les listez par ordre chronologique

## Outils informatique utilisé :
● Google colaboratory (Python )
● PySpark
● Mllib

## Description des données
Les données sont importées à partir de kaggle, le dataset est composé des actions quotidiennes des 
40 sociétés française les plus valorisées de Janvier 2010 à Avril 2020:
- 7 colonnes ( Name, Date, Open, Closing_price, Daily_high, Daily_low - Volume )
- 97648 lignes

## Les fichiers .py  :

Configuration de l’environnement de travail;
1. utils1.py : pour instancier mon SparkSession;
2. utils2.py : j’ai appelé toutes les bibliothèques que je vais utiliser
dans ce projet;
3. config_projet.py : dans ce script, j’ai appelée les deux premiers
scripts, et il contient trois fonctions, une fonction qui appel
Spark en appelant utils1.py, une fonction qui charge le dataset, et
la fonction qui fait le traitement des donner, et l’apprentissage.
Elle enrigistre le résultat sous forme d’un fichier csv et la figure
en format .png
4. execute.py : j’appelle config_projet.py, et y’a deux fonctions,
une fonction qui exécute les fonctions de script config_projet.py
lire le fichier de données et la fonction de prédiction ; 

## Le fichier execute.sh:
Pour exécuter le code
