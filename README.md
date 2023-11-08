
![image](https://github.com/Projet-SCAR/SCAR/assets/90306617/c388bb57-7889-41c6-8f22-ef493058995c)

<h3 align="center">Projet SCAR</h3>

Partie Compression :
- compression.py : l'algorithme qui fait la compression
- compressionTestQualite.py et compressionTestRedimension.py : 2 algorithmes qui permettent de tester la qualité de la compression
  
Partie détection d'animaux :
- detection_en_direct.py fait un traitement en direct sur le flux d'image de la caméra reliée au réseau de l'école (nécessite une connexion au réseau de l'école ou au VPN)
- imageCameraEcole.py se connecte à la caméra reliée au réseau de l'école et détecte les éléments dessus (nécessite une connexion au réseau de l'école ou au VPN)
- imageImportee.py permet de détecter les éléments présents sur une image importée depuis l'ordinateur

Partie Seuillage :
- Seuillage.ipynb est un document Jupyter Notebook expliquant les démarches du programme de seuillage.
- graphSeuillage.py est un programme permettant de tracer sur un graphe temporel l'évolution du taux de vert et du taux de neige sur les images.
- seuillageArbreProba9imgs.py est un programme effectuant le seuillage sur plusieurs images.
- tableauSeuillage9imgs.py est un programme qui permet de tester plusieurs valeurs de seuils pour cette détection par seuillage.

Partie Transmission :
  - Arduino :
    - capteursTransmi.ino : Récupère les données des capteurs et les envoie au Raspberry par liaison I2C
    - programmeDeLaDocumentation : Programme récupéré de la documentation du capteur de température et d'humidité qui permet de l'afficher sur un écran LCD.

  - Raspberry (Il est nécéssaire de faire la commande "sudo chmod 666 /dev/ttys0" sur chaque Raspberry pour autoriser la communication)
    - capture.sh : Script bash qui prend une photo via l'utilisation de testcam.py
    - ecritureCSV.py : Reste d'ancien code inutilisé, qui servait uniquement à sauvegarder les données en csv, il a été merge dans dialogue.
    - dialogue.py : Code de la Raspberry émettrice pour envoyer ET écrire en .csv sur l'émettrice afin de garder une trace s'il y a un problème de communication
    - ecritureTempsReel.py : recoit les données via LoRa sur Raspberry réceptrice, les formate, transfère vers influxDB et sauvegarde un csv.

