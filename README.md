# Destination_Recommender_System

## Overview

A destination recommender system that takes the user's origin point and the month during which they will be traveling as input, and recommends them the top ten destinations they can travel to.

## Achievements

2nd position at [Enter the Travel-Verse Hackathon by Airline Reporting Corporation(ARC)](https://www.hackerearth.com/challenges/hackathon/enter-the-travel-verse/) organized on HackerEarth.

![Alt text](Images/ARC2.png?raw=true "Result")

## Sample Screenshots

![Alt text](Images/Img1.png?raw=true "Result1")

![Alt text](Images/Img2.png?raw=true "Result2")

![Alt text](Images/Img3.png?raw=true "Result3")

![Alt text](Images/Img4.png?raw=true "Result4")

## Solution

We employed different pre-processing techniques to clean [the dataset](https://travelverse-hackathon.arccorp.com/travelverse-compressed-dataset.csv.gz). Then we created the recommendation matrix from the remaining data which we used for our recommendation system. We created a small Tkinter GUI in python to test our system.

## How-To-Run

1) Unzip TravelVerse.zip
2) Run TravelVerse.py

Note:

1) TravelVerse.py may take a few minutes to run since it loads the entire recommendation matrix on memory.
2) TravelVerse.zip contains data required to run the recommender system.
3) This data was obtained by running PreProcessing.py in batches on the dataset.

## Goal

With the help of our system, travel agencies can understand their customers better and launch attractive holiday packages accordingly. For example, a travel agency offering holiday packages from Mumbai can use our system to analyze monthly trends and offer month-specific holiday packages to target a larger customer base and maximize their profits. Normal users can also use this system to plan their next vacation.

## Future Scope

1) This system can be hosted on a cloud platform where it can process data continuously and provide recommendations based on the most recent trends, providing reliability and adaptability.
2) It can be modified to work as an API service, then it can be attached to a variety of web and mobile applications which require this kind of system.
