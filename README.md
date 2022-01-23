# NAS-MPLS

Projet NAS TC INSA Lyon
Autoconfigurateur MPLS pour GNS3 via un script Python

## Lancement

Pour lancer le script "main" il faut utiliser la commande suivante : 

    python3 main.py 0

Il faut aussi avoir allumé les routeurs sur GNS3.

NB : - il faut bien vérifier que les routeurs ont bien fini de s'allumer
     - le script est lent (18 min), bien attendre sa fin
     - les protocoles sont lents à converger, dans nos simulations les routes BGP mettaient jusqu'à 10 min à se créer



Pour lancer le script "update", qui permet de configurer de nouveaux routeurs tout en les ajoutant au JSON (/!\ ne fonctionne pas pour l'instant) :

	python3 update.py {nouveau(x)_routeur(s).json}

NB : - il y a un exemple de fichier JSON à remplir sous le nom "new_routers.json"
	 - ce script ne fonctionne pas pour le moment : il faut prendre en compte le fait qu'il faut créer de nouvelles interfaces dans les routeurs auxquels les nouveaux sont connectés

## JSON proposé

Le JSON "config_routers" propose des ports fixes adaptés à la configuration visible dans le schéma. Avant de lancer le script, il faut vérifier que les ports sur GNS3 des routeurs correspondent bien à ceux inscrits dans le JSON.

## Schéma proposé

Vous trouverez un schéma du montage sur lequel nous avons fait nos tests. Il y est indiqué les adresses utilisées, numéro d'AS, router-id... 
Il y est aussi indiqué les types de lien vers l'extérieur (client, peer, provider).

## Archives

Il y a 2 archives dans notre dossier projet. Blank_project contient une architecture vierge sur laquelle on peut lancer le script. Les routeurs clients y sont déjà configurés mais pas les VPC client (qu'il faut configurer à la main). Le script s'occupera de configurer les routeurs de notre réseau. 

Il y a aussi une autre archive (projet_fonctionnel) avec une instance de GNS3 dont tous les routeurs ont été configurés, si vous voulez tester notre configuration sans avoir à lancer le script.

## Auteurs

Romain Berthomieu, Pakinam Tarek, Gaspard Michel, Maxime Bouhadana et Antoine Merle
