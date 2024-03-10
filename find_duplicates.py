# Find and return the duplicate elements in a list
# IP = [1,2,3,4,1,2] OP = [1,2]

def find_duplicates(arr):
    res = []
    seen = []
    for i in arr:
        if i in res:
            seen.append(i)
        else:
            res.append(i)
    return seen

print(find_duplicates([1,2,3,4,1,2]))
            
