# Pomodoro Timer

Ce projet consiste en une application de minuterie Pomodoro réalisée en utilisant le module Tkinter en Python. La technique Pomodoro est une méthode de gestion du temps développée par Francesco Cirillo dans les années 1980, qui encourage la division du temps de travail en intervalles courts appelés "Pomodoros", suivis de courtes pauses.

## Constantes

Le projet utilise les constantes suivantes pour définir la durée du travail, des pauses courtes et longues, ainsi que les couleurs utilisées dans l'interface graphique.

- Durée du travail (`WORK_MIN`): 25 minutes
- Pause courte (`SHORT_BREAK_MIN`): 5 minutes
- Pause longue (`LONG_BREAK_MIN`): 20 minutes
- Couleurs (`PINK`, `RED`, `GREEN`, `YELLOW`): Couleurs définies en hexadécimal
- Police (`FONT_NAME`): "Courier"

## Fonctionnalités

- **Réinitialisation de la minuterie (`reset_timer`):** Permet de réinitialiser la minuterie en annulant tout minutage en cours et réinitialisant l'affichage.
  
- **Démarrage de la minuterie (`start_timer`):** Démarre la minuterie en fonction du nombre de sessions de travail et de pauses courtes/longues. Utilise également une mécanique de comptage pour alterner entre les sessions de travail et les pauses.

- **Mécanique de minuterie (`count_down`):** Affiche le temps restant sous forme de minuterie descendante. Utilise également la récursivité pour mettre à jour la minuterie chaque seconde.

- **Interface utilisateur (`UI SETUP`):** Utilise Tkinter pour créer une interface graphique avec un bouton de démarrage, un bouton de réinitialisation, une image de tomate, une minuterie et des étiquettes pour afficher le statut du timer et les sessions de travail complétées.

## Installation et Configuration

- Python 3.9.6
- Importation du module tkinter (`import tkinter`)

## Capture d'écran

![Pomodoro Timer](assets/screenshot.png)

## Remarques

Projet réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
