
# LITREVIEW


## Description du projet

Son objectif est de commercialiser un produit permettant à une communauté d'utilisateurs de publier des critiques de livres ou d’articles et de consulter ou de solliciter une critique de livres à la demande.

## Mise en place et exécution en local de l'application

1. Téléchargez le projet depuis Github en clonant le projet en utilisant la commande suivante:  
```
git clone https://github.com/Antinii/Projet_9_Litreview.git
```
2. Créez un environnement virtuel Python en exécutant la commande suivante:
```
python -m venv env 
```
Puis, activez votre environnement virtuel avec la commande suivante:
```
source env/bin/activate pour Mac / Linux
env/Scripts/activate pour Windows
```
3. Dans votre environnement virtuel, installez les packages Python nécessaires :
```
pip install -r requirements.txt
```
NB : Puisque la base de données contenant du contenu visant à démontrer la fonctionnalité de l'application est incluse dans le repository.
Il n'est pas nécessaire de procéder aux migrations, mais si vous souhaitez recréer la BDD de zéro, supprimez le fichier db.sqlite3 et procédez aux migrations, à l'aide de la commande suivante :
```		
python manage.py migrate
```
4. Vous pouvez maintenant exécuter l'application en local à l'aide de la commande suivante :
```		
python manage.py runserver
```
5. L'application est prête, accédez-y à l'addresse suivante:
```
http://127.0.0.1:8000/
```
6. Dans la base de donnée communiquée, 4 comptes de démonstrations ont été créés avec quelques publications. Les noms d'utilisateurs sont les suivants :
```		
antini (superuser)
```
```		
Marc
```
```		
Emily
```
```		
Sarah
```
Le mot de passe est le même pour tous ces comptes :
```		
S3cret!!
```

Afin de générer un nouveau rapport flake8:
```		
flake8 --format=html --htmldir=rapport
```
