#Random
import random
from membership import binarysortsearchmember
from Mutation6 import binarysortsearchmemberone

def randomTest(arraySize=100, start=0, stop=100):
    array=[]
    for i in range(0,arraySize,1):
        array.append(random.randint(start, stop))
    return array

def test():
    key = 0
    LappCounter = 1
    k = True
    while k == True:
        randomarray = randomTest()
        sakjagforsoker = []
        for testings in randomarray:
            sakjagforsoker.append(testings)
        if key == 0:
            nummer = random.randint(0,7)
            key = randomarray[nummer]
            print("The key is " + str(key))
        CorrectAnswer = binarysortsearchmember(key,randomarray)
        MutationAnswer = binarysortsearchmemberone(key,sakjagforsoker)
        if CorrectAnswer == MutationAnswer:
            LappCounter += 1
        else:
            print("Result should give "+ str(CorrectAnswer) + " but gives " + str(MutationAnswer))
            print("Mutation is found on lapp " + str(LappCounter))
            break
test()