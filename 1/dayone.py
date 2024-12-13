import pandas as pd
from collections import Counter

def main():

    totalDistance = 0
    similarityScore = 0

    df = pd.read_csv("input", header=None, index_col=False, delimiter="   ", engine="python", names=["ListA", "ListB"] )
    listA = df["ListA"].to_list()
    listB = df["ListB"].to_list()

    listA.sort(key=int)
    listB.sort(key=int)

    for index, item in enumerate(listA, start=0):
        totalDistance += abs(listA[index]-listB[index])

    for key, value in Counter(listB).items():
        if key in listA:
            similarityScore += key*value
            
    
    
    
    print(f"Total distance is: {totalDistance}")
    print(f"Similarity score is: {similarityScore}")


main()
