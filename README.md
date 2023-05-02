Ce Git contient :

Partie Transmission :
  - Arduino :
    - capteursTransmi.ino : Récupère les données des capteurs et les envoie à la Raspberry par liaison I2C
    - programmeDeLaDocumentation : Programme récupéré de la documentation du capteur de température et d'humidité qui permet de l'afficher sur un écran LCD.

  - Raspberry
    - capture.sh : Script bash qui prend une photo via l'utilisation de testcam.py
    - ecritureCSV.py : Reste d'ancien code inutilisé, qui servait uniquement à sauvegarder les données en csv, il a été merge dans ecritureTempsReel.
    - ecritureTempsReel : recoit les données via LoRa sur Rpi Rx, les formate, transfère vers influxDB et sauvegarde un csv. 

Partie Compression :
- l'algorithme qui fait la compression
- 2 algorithmes qui ermettent de tester la qualité de la compression

Partie Seuillage :



