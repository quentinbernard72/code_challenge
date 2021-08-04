# code_challenge
48 hours code challenge for Rhobs 

AUTHOR : Quentin BERNARD
DATE : Wednesday the 4th of August, 2021

DESCRIPTION : 

This repository contains the project of code challenge in the process of joining the Rhobs team as Data Analyst.
The challenge was to compute some metrics on a database :

- The number of listeners by music
- The average age by music
- A function giving a pyramid age with arguments (city and slice of years)

Everything can be found in the file __main__.py. This file is organized in four sections (0 to 3) :

Section 0 : IMPORTS AND CONNECTION TO DATABASE
Section 1 : NUMBER OF LISTENERS BY MUSIC
Section 2 : AVERAGE AGE BY MUSIC
Section 3 : PYRAMID AGE

Functions are explained by comments and explicit variables.
Answers to questions can be found by computing functions in the different sections. After each of these functions, I put an example that can be freely executed and modified (no need for functions requiring no argument) by removing the hastag.

Section 1 : numberOfListenersByMusic (no argument) and displayNumberOfListenersByMusic (no argument) which compute the number of listeners by music
Section 2 : averageAgeByMusic (no argument) and displayAverageAgeByMusic (no argument) which compute the average age by music
Section 3 : pyramidAge (arguments : city, slice) and displayAverageAge (arguments : city, slice) which compute the pyramid age for the city

REMARKS :

I hesitated on the way to give the results not knowing what was expected so I may have bypassed the database essence of the project with a more iterative approach.
From my readings on MongoDB I guess that some of the work could have been done with queries. However, I did not see how to deal with the data stored in a dictionnary being itself a value of a changing key (the name of the person !) which at first sight is not convenient for queries.
