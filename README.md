# NAS-MPLS

Projet NAS TC INSA Lyon
Autoconfigurateur MPLS pour GNS3 via un script Python

## Lancement

Pour lancer le script il faut utiliser la commande suivante : 

    python3 main.py 0

Il faut aussi avoir allumé les routeurs sur GNS3.

NB : - bien vérifier que les routeurs ont bien fini de s'allumer
     - les scripts est lent (18 min), bien attendre sa fin
     - les protocoles sont lents à converger, dans nos simulations les routes BGP mettaient jusqu'à 10 min à se créer

## JSON proposé

Le JSON propose des ports fixes adaptés à la configuration visible dans le schéma. Avant de lancer le script, il faut vérifier que les ports sur GNS3 des routeurs correspondent bien à ceux inscrits dans le JSON.

## Schéma proposé

Vous trouverez un schéma du montage sur lequel nous avons fait nos tests. Il est indiqué les adresses utilisées, numéro d'AS, router-id... 
Il y est aussi indiqué les types de lien vers l'extérieur (client, peer, provider).

## Auteurs

Romain Berthomieu, Pakinam Tarek, Gaspard Michel, Maxime Bouhadana et Antoine Merle