import time
import matplotlib.pyplot as plt
import threading

runTimes = False


def getRunTime(func):
    def wrapper(userInput):
        start = time.time()
        func(userInput)
        return time.time() - start
    return wrapper


def getData(userFile):
    global runTimes

    exec(f"import {userFile}")
    inputTimes = eval(f"{userFile}.inputTimes")
    # print(inputTimes)
    userFunc = getRunTime(eval(f"{userFile}.main"))

    tempRunTimes = {}
    for key, value in inputTimes.items():
        tempRunTimes[key] = userFunc(value)
    

    runTimes = tempRunTimes




def createGraph(runTimes):
    plt.plot(list(runTimes.keys()), list(runTimes.values()))

    plt.xlabel('Size Of Input') 
    plt.ylabel('Run Time(in seconds)') 
    
    plt.title('Yo Tim')
    
    plt.show()
    

def generateGraphFromFile(userFile):
    getData(userFile)
    createGraph(runTimes)

# generateGraphFromFile("sample")
