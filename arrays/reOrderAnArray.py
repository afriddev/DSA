def solution(array1,array2):
    emptyArray = []
    o = 0
    for i in array2:
        emptyArray.insert(i,array1[o])
        o+=1
    print(emptyArray)
if __name__ == "__main__":
    array1 = [10,11,12]
    array2 = [1,0,2]
    solution(array1,array2)
