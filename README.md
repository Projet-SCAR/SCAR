Ce Git contient :

Partie Transmission :
  - Arduino :
    - capteursTransmi.ino : Récupère les données des capteurs et les envoie au Raspberry par liaison I2C
    - programmeDeLaDocumentation : Programme récupéré de la documentation du capteur de température et d'humidité qui permet de l'afficher sur un écran LCD.

  - Raspberry
    - capture.sh : Script bash qui prend une photo via l'utilisation de testcam.py
    - ecritureCSV.py : Reste d'ancien code inutilisé, qui servait uniquement à sauvegarder les données en csv, il a été merge dans ecritureTempsReel.
    - ecritureTempsReel : recoit les données via LoRa sur Rpi Rx, les formate, transfère vers influxDB et sauvegarde un csv. 

Partie Compression :
- l'algorithme qui fait la compression
- 2 algorithmes qui permettent de tester la qualité de la compression

Partie Seuillage :
- Seuillage.ipynb est un document Jupyter Notebook expliquant les démarches du programme de seuillage.
- graphseuillage.py est un programme permettant de tracer sur un graphe temporel l'évolution du taux de vert et du taux de neige sur les images.
- seuillagearbreproba9imgs.py est un programme effectuant le seuillage sur plusieurs images.
- tableauseuillage9imgs.py est un programme qui permet de tester plusieurs valeurs de seuils pour cette détection par seuillage.

