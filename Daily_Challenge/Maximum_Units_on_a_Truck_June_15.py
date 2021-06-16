''' The Problem
-------------------
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
-------------------
'''

''' Thinking 
------------------
June 15th
* Time Complexity needs to be O(len(boxTypes) * numberOfBoxesi * numberOfUnitsPerBoxi)

June 16th
* Question: The problems ask maximum units or maximum boxes? These will lead to different answers -- It askes for units

* We can't put boxes with larger units on the truck first, and the consider the boxes that are lighter. The sum may not fully utilize 
  the truck's load. For example, {3(units)*1(box), 5*1, 7*1}, if the load is 8. We could only fit in one 7, but we can fit in one 3 and one 5
 , and the sum would be 8 > 7.

* This leads to thinking maybe we can create a large array with the length of the truckSize to do some experiments.

* One problem arise when constructing the array: how do we record in each step what box we take, that requires a lot of memory

* We deal with this by implementing an optimal strategy: when we have choice of forming a weight, we always choose the larger box when
* both can form the weight exactly

* For example, if we have 1(unit) * 3 and 3(unit) * 1, we would choose the 3(unit) if we want to form a three unit weight. There is no reason
* why we shouldn't choose this. If our goal is to form a 4 units, we could use the spared one unit to do so. (We are not aiming to include more boxes)

* In light of this, we could use a Treemap structure to decide which box to take in each step. If currently we are filling x units, we check the largest number in the 
* hashmap that is smaller than or equal than x. Suppose it is y. If there is still y units box left, we could take the existing result of arr[x-y], if could be as small as 0 and 
* as large as (x - y). If we found arr[x-y] == x-y, and box[y] > 0, then great we have found the optimal at this step. We can happily store x in arr[x], and minus 1 to box[y]

* But what if we found the y that is exact. We have to store every result and compare. That's a lot to memorize and need to iterate through all.

* PROBLEM - but still there is another problem. When we are constructing the array, how do we store what box we used in each step? 
* For example, if there is 2(unit) * 2 and 3(unit) * 1. And when constructing 4, we would use two 2 units boxes. If we store this step in 
* the original hash map, then we would meet a problem when constructing 5. Since we could have used one 3 units and one 2 units to construct 5. 
* but according to the map, we have used it all.

* How do we store what boxes we use? 

Correction
-----------------
* The trucksize is not about units, it's about boxes. The trucksize is how many boxes the truck can hold

* In this case, the problem is as simple as one can't imagine. Since the limit is how many boxes we can carry. We need to carry the boxes with the 
  largest units first. Takes a greedy approach and the problem is solved.

* To sort the 2-d array, we can use sort(key = lambda expression)

* Do not hurry on with the problem, read carefully 

Summary
-----------------

* Look clear about the constraints of the problem

* Pass lambda expression to a key is strange, look into documentation about lambda expression sometimes

* Although it is simple, there is still some implementation details need to be noted.
'''


def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda arr: -arr[1])
    maxUnit = 0
    for boxes, units in boxTypes:
        if truckSize >= boxes:
            maxUnit += boxes * units
            truckSize -= boxes
        else:
            maxUnit += truckSize * units
            return maxUnit
    return maxUnit


if __name__ == "__main__":
    print(maximumUnits([[1, 3], [1, 5], [1, 7]], 8))
