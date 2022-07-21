# Détection du type de chaussures de sport Nike 

Vision par ordinateur pour détecter le type de chaussures de type sneakers (seulement entraîné pour la marque Nike)




**Objectif de ce projet :**

En tant qu'accro aux baskets, il est très facile pour moi de deviner le type de chaussures que je regarde.
Mais par exemple, lorsque je montre la photo à mes proches, ils ne peuvent pas différencier dunk et jordan.
  
C'est pourquoi mon projet de vision par ordinateur vise à vous dire de quel type de chaussures il s'agit en lui donnant une image en entrée. Nous aimerions avoir une précision de 80 % en pourcentage.

Voici un **exemple concret** :  

Vous choisissez cette image :

<img src="https://github.com/axelooc59/Detecting-type-of-sneakers-shoes/blob/main/mocha.png" alt="draw" width="200"/>

Il retournera son type qui est *Jordan 1 High*.

Mon programme supportera les types de chaussures suivants :
* Jordan 1 High
* Jordan 1 Mid
* Jordan 1 low
* Jordan 3
* Jordan 4
* Dunk low (forme classique)
* Dunk high

En tant que débutant en apprentissage automatique et afin de rendre ce projet plus facile et possible, la seule image acceptée est celle ci-dessous.   
A savoir que la chaussure est orientée vers la gauche et sur un fond blanc.

## Etapes de ce projet 
Ce projet comporte trois étapes principales :
1. Collecter des données pour entraîner notre modèle
2. Prétraitement des données collectées
3. Créer notre modèle en lui donnant nos données


### 1. Collecte des données 
(fichier [collecting_data.ipynb](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/collecting_data.ipynb))  
Afin de collecter les données, nous allons gratter l'image des baskets du site web [restocks.net](https://restocks.net), de cette façon nous obtiendrons des données facilement étiquetées.
  
Pour cela, nous utilisons la bibliothèque *requests* de python et un peu de javascript pour obtenir le lien de l'image.

Nous trions chaque image dans le dossier correspondant.

Voir le code dans *collecting_data.ipynb*.

Nous avons pu collecter un total de 725 images. Ce n'est pas beaucoup pour entraîner un réseau neuronal profond. C'est pourquoi j'avais choisi précédemment d'utiliser le même modèle de type de photos de baskets pour rendre cet entraînement possible.

### 2. Prétraitement des données 
(fichier [pre_processes.ipynb](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/pre_procceses.ipynb))  

Pour le prétraitement de nos données, nous n'avons pas grand chose à faire. J'ai resivé toutes les images à une taille de 200x200 pixels et divisé chaque image par 256 afin d'avoir des valeurs entre 0 et 1 pour notre réseau profond.  
+ A 1 signifie un pixel noir, et un zéro signifie un pixel d'écriture.

J'ai séparé le jeu de données en un jeu de formation (80%) et un jeu de validation (20%).

### 3. Écriture de notre réseau neuronal profond
(fichier [pre_processes.ipynb](https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/pre_procceses.ipynb))  
J'ai créé un réseau de neurones convolutif (CNN) qui est vraiment approprié pour traiter l'image.
Pour ce faire, j'ai utilisé la bibliothèque keras de **TensorFlow**.

J'ai réussi à atteindre une précision de 82% sur l'ensemble de validation.

Ci-dessous le résultat de la prédiction par mon réseau neuronal sur l'ensemble de validation :  
(En rouge nous avons une prédiction erronée,à gauche nous avons l'étiquette réelle et à droite la prédiction).  
<img src="https://github.com/axelooc59/Detecting-type-of-sneakers-shoes-by-ML-/blob/master/CV_SNKRS/prediction.png" alt="dessin" />


Traduit avec www.DeepL.com/Translator (version gratuite)
