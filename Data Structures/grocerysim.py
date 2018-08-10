from pythonds.basic.queue import Queue
import random
import math


class lessGroceriesRegister:
    def __init__(self, gpm, gMax):
        self.gpm = gpm
        self.task = None
        self.timeRemaining = 0
        self.groceriesMax = gMax

    def startTask(self, task):
        self.task = task
        self.timeRemaining = 60 * task.getGroceries() / self.gpm

    def countdown(self):
        if self.timeRemaining > 0:
            self.timeRemaining = self.timeRemaining - 1
        else:
            self.task = None

    def busy(self):
        if self.task == None:
            return False
        else:
            return True

    def getMax(self):
        return self.groceriesMax


class moreGroceriesRegister:
    def __init__(self, gpm, gMin):
        self.gpm = gpm
        self.task = None
        self.timeRemaining = 0
        self.groceriesMin = gMin

    def startTask(self, task):
        self.task = task
        self.timeRemaining = 60 * task.getGroceries() / self.gpm

    def countdown(self):
        if self.timeRemaining > 0:
            self.timeRemaining = - 1
        else:
            self.task = None

    def busy(self):
        if self.task == None:
            return False
        else:
            return True

    def getMin(self):
        return self.groceriesMin


class Groceries:
    def __init__(self, time, limit):
        self.timeStamp = time
        self.limit = limit
        self.amount = random.randrange(1, self.limit + 1)

    def getGroceries(self):
        return self.amount

    def getStamp(self):
        return self.timestamp

    def waitTime(self, currentTime):
        return currentTime - self.timeStamp


def Simulation(timeTot, lg, mg, limit, ppl, gMin):
    aList = []  # lessGroceriesRegister
    bList = []  # Queue for lessGroceriesRegister
    cList = []  # Queue for moreGroceriesRegister
    dList = []  # moreGroceriesRegister
    waitingTimes = []
    for i in range(0, lg):
        aList = aList + [lessGroceriesRegister(12, 8)]
        bList = bList + [Queue()]

    for j in range(0, mg):
        dList = dList + [moreGroceriesRegister(12, 9)]
        cList = cList + [Queue()]

    for currentSecond in range(timeTot):

        if newTask(ppl):
            groceries = Groceries(currentSecond, limit)

            if groceries.amount > gMin:
                count = math.inf
                for l in cList:
                    if l.isEmpty():
                        count = 0
                        smallest = l
                    elif l.size() < count:
                        count = l.size()
                        smallest = l

                if cList != []:
                    smallest.enqueue(groceries)

            elif groceries.amount <= gMin:
                count = math.inf
                for l in bList:
                    if l.isEmpty():
                        count = 0
                        smallest = l
                    elif l.size() < count:
                        count = l.size()
                        smallest = l

                if bList != []:
                    smallest.enqueue(groceries)

        for register in range(0, len(aList)):

            if (not (aList[register]).busy()) and (not (bList[register]).isEmpty()):
                nextTask = (bList[register]).dequeue()
                waitingTimes.append(nextTask.waitTime(currentSecond))
                (aList[register]).startTask(nextTask)

        for register1 in range(0, len(dList)):

            if (not (dList[register1]).busy()) and (not (cList[register1]).isEmpty()):
                nextTask = (cList[register1]).dequeue()
                waitingTimes.append(nextTask.waitTime(currentSecond))
                (dList[register1]).startTask(nextTask)

        for y in aList:
            y.countdown()

        for z in dList:
            z.countdown()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print(averageWait)


def newTask(ppl):
    avgNumTasks = 3600 // (ppl * 2)
    num = random.randrange(0, avgNumTasks + 1)
    if num == avgNumTasks:
        return True
    else:
        return False


Simulation(3600, 1, 1, 20, 100, 8)
Simulation(3600, 10, 10, 20, 100, 8)