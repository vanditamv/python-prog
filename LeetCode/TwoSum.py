'''Input: nums = [3,2,4], target = 6
Output: [1,2]'''

def twoSum(array,target):
    prevMap = {}  #value :index
    for i,n in enumerate(array):
        comp = target - n 
        if comp in prevMap:
            return [i,prevMap[comp]]
        prevMap[n] = i
    return
        
