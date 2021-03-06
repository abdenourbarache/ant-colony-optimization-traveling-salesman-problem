from  random import random

def removeCityIfExist(citiesList, city):
    for c in citiesList:
        if c.get('name') == city:
            citiesList.remove(c)
            break

def getCandidateCities(candidatesCities, alreadyVisitedCities):
    finalList = candidatesCities.copy()
    for city in alreadyVisitedCities:
        removeCityIfExist(finalList, city)
    return finalList

def getNextCity(candidatesCities, a, b):
    totalProbabilities = 0.0
    for city in candidatesCities:
        totalProbabilities += (city.get('pheromones')**a * (1/city.get('distance'))**b)
    edegsProbabilities = []
    for city in candidatesCities:
        edegsProbabilities.append((city.get('pheromones')**a * (1/city.get('distance'))**b)/ totalProbabilities)
    cummulativeSum(edegsProbabilities)
    edegsProbabilities.append(0)
    randomNum = random()
    x = binary_search_iterative(edegsProbabilities, randomNum)
    indexX = edegsProbabilities.index(x)
    if x < randomNum:
        indexX -= 1
    return candidatesCities[indexX]

def updateEdgePheromone(citiesList, city, pheromoneToAdd):
    for c in citiesList:
        if c.get('name') == city:
            c['pheromones'] += pheromoneToAdd

def pheromoneEvaporation(graph, evaporationRate):
    for c1 in graph:
        for c2 in graph[c1]:
            c2['pheromones'] = (1 - evaporationRate)*c2['pheromones']

def globalBestReinforcement(graph, tours, reinforcementFactor):
    tours.sort(key = lambda x: x['total distance'], reverse=False)
    bestTour = tours[0].get('name')
    totalDistance = tours[0].get('total distance')
    for i in range(0, len(bestTour)-1):
        updateEdgePheromone(graph.get(bestTour[i]) , bestTour[i+1], reinforcementFactor* 1/totalDistance)
        updateEdgePheromone(graph.get(bestTour[i+1]) , bestTour[i],  reinforcementFactor* 1/totalDistance)


def updatePheromones(graph,totalDistance, visitedCities, evaporationRate, tours, reinforcementFactor):
    #evaporization 
    pheromoneEvaporation(graph, evaporationRate)
    #deposit pheromones
    for i in range(0, len(visitedCities)-1):
        updateEdgePheromone(graph.get(visitedCities[i]) , visitedCities[i+1], 1/totalDistance)
        updateEdgePheromone(graph.get(visitedCities[i+1]) , visitedCities[i], 1/totalDistance)
    #global best tour reinforcement
    globalBestReinforcement(graph, tours, reinforcementFactor)
    
def cummulativeSum(probabilities):
    probabilities.reverse();
    cummulativeSum = 0
    for i in range(0,len(probabilities)):
        cummulativeSum += probabilities[i]
        probabilities[i] = cummulativeSum
    probabilities.reverse()
    probabilities[0] = round(probabilities[0]) 
    return probabilities

def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0
    arrayClone = array.copy()
    arrayClone.reverse()
    while (start <= end):
        step = step+1
        mid = (start + end) // 2
        
        if element == arrayClone[mid]:
            return arrayClone[mid]

        if element < arrayClone[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return arrayClone[mid]

test = 3