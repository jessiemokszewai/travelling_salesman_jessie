# Traveling Salesman

This is a classic computer science problem, known as the **Traveling Salesman problem**. 

## Overview

A traveling salesman wishes to visit every city exactly once and return to the starting point. 
However, the salesman also wishes to find the shortest route.

A file, `city-data.txt`, containing the 
latitudes and longitudes of the fifty state capitals of the U.S.A. 
Each line contains:
- the name of the state, 
- the name of the city, 
- the latitude, and 
- the longitude. 

The distance between any two cities with the coordinates (x1, y1) and (x2,y2) is
 the standard Euclidean distance.

## Approach - Run a Randomised Optimisation Algorithm

This application optimises the travelling road map through a randomising algorithm including swapping and shifting 
cities. The process iterates for 10,000 times and through a high climbing approach, each iteration will optimise the 
road map until it cannot be further optimised or it reaches the end of the iteration.


