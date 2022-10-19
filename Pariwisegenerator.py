from random import randint
import random
from membership import binarysortsearchmember
from Mutation5 import binarysortsearchmemberone

def pairwisegenerator(Elements=100, highest=1000, lowest=1):
        defaults = []
        typicals = []
        testCases = []

        for NumberOfElements in range(Elements):
            defaults.append(randint(lowest, highest))
        while len(typicals) < len(defaults):
            NewTypical = randint(lowest, highest)
            if NewTypical != defaults[len(typicals)]:
                typicals.append(NewTypical)
        """0-wise"""
        testCases.append(defaults)
        """1-wise"""
        for element in range(Elements):
            newTestCase = defaults[0:element] + typicals[element:element + 1] + defaults[element + 1:]
            testCases.append(newTestCase)
        """2-wise"""
        for element1 in range(Elements):
            for element2 in range(element1 + 1, Elements):
                newTestCase = defaults[0:element1] + typicals[element1:element1 + 1] + \
                              defaults[element1 + 1:element2] + typicals[element2:element2 + 1]\
                              + defaults[element2 + 1:]
                testCases.append(newTestCase)
        return testCases


def test():
    LappCounter = 1
    k = True
    while k == True:
        gigaarray = pairwisegenerator()
        key = 0
        for elementarray in gigaarray:
            sakjagforsoker = []
            for testings in elementarray:
                sakjagforsoker.append(testings)
            if key == 0:
                nummer = random.randint(0,7)
                key = elementarray[nummer]
                print("The key is " + str(key))
            CorrectAnswer = binarysortsearchmember(key,elementarray)
            MutationAnswer = binarysortsearchmemberone(key,sakjagforsoker)
            if CorrectAnswer == MutationAnswer:
                LappCounter += 1
            else:
                print("Result should give "+ str(CorrectAnswer) + " but gives " + str(MutationAnswer))
                print("Mutation is found on lapp " + str(LappCounter))
                k = False
                break


test()
