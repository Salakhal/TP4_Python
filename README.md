# TP 4 : Polymorphisme :

#  Exercice 1 :

## Objectif pédagogique
Ce TP a pour objectif d’explorer le **polymorphisme** en Python à travers :
- l'utilisation d'interfaces communes,  
- les substitutions dynamiques,  
- et la démonstration que plusieurs classes peuvent partager une même interface et être utilisées de façon interchangeable.

---

## Résultat attendu :
```
Ouaf !
Miaou !
Meuh !
Bip bop !
Ouaf !
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="186" height="163" alt="image" src="https://github.com/user-attachments/assets/178331c5-0372-4a17-b23b-12c37b743597" />


#  Exercice 2

## Objectif pédagogique
Ce TP a pour objectif d’approfondir le **polymorphisme** en Python en créant une hiérarchie de **formes géométriques** capables de calculer leur **aire** via une interface commune.  

Les concepts abordés :  
- Classes **abstraites** avec méthodes obligatoires,  
- Polymorphisme pur via substitution et collections hétérogènes,  
- Surcharge de la méthode `__str__()` pour un affichage uniforme.

---

## Résultat attendu :
```
Cercle – aire : 28.27 – Couleur : rouge
Rectangle – aire : 20.00 – Couleur : vert
Triangle – aire : 6.00 – Couleur : bleu
Carre – aire : 16.00 – Couleur : jaune
Tous les tests unitaires sont passés !
```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="580" height="164" alt="image" src="https://github.com/user-attachments/assets/80b2809f-e9f7-4919-b755-e6a8ae13f3de" />

# Exercice 3 : Polymorphisme avec les moyens de paiement

## Objectif pédagogique
- Concevoir une **interface commune** (`Paiement`) pour différents moyens de paiement.
- Appliquer le **principe de substitution** : un même appel `payer()` déclenche le comportement approprié selon la sous-classe.
- Manipuler une **collection hétérogène** d’objets et mesurer la souplesse du polymorphisme.

---

## Résultat attendu :

```
Paiement de 100.00€ effectué par Carte Bancaire (5678...)
Paiement de 50.00€ effectué par Carte Bancaire (4321...)
Paiement de 75.00€ effectué via PayPal (user1@example.com)
Paiement de 200.00€ effectué via PayPal (user2@test.com)
Paiement de 150.00€ effectué en crypto BTC (Wallet wallet123)
Paiement de 300.00€ effectué en crypto ETH (Wallet wallet456)

```
##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="838" height="198" alt="image" src="https://github.com/user-attachments/assets/70afe12c-a2f3-4438-a923-52610a060dcc" />















