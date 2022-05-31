while (currentPopulation != 0 ) and ( currentGeneration < generations):
    expired = round(float((currentInfected / 100) * deathRate))
    currentInfected -= expired
    currentPopulation -= expired
    totalDeaths += expired

    recovered = round(float((currentInfected / 100) * recoveryRate))
    currentInfected -= recovered
    currentRecovered += recovered
    
    if( currentInfected < 0 ):
        currentInfected = 0

    possibleInfectees = (currentPopulation - currentInfected) - currentRecovered
    newInfections = round((float(currentInfected * r)))

    if(currentPopulation - currentInfected == currentRecovered):
        newInfections = 0

    if(newInfections > possibleInfectees):
        newInfections = possibleInfectees

    currentInfected += newInfections

    currentGeneration = currentGeneration + 1

    print(currentGeneration, currentPopulation, currentInfected, totalDeaths)
