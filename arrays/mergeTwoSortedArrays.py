def solution(array1,array2):
    for i in range(0,len(array1)):
        smallestInArray2= array1[i]
        index = i
        for j in range(0,len(array2)):
            if(smallestInArray2 > array2[j]):
                smallestInArray2 = array2[j]
                index = j
        if(index!=i):
            array1[i],array2[index] = array2[index],array1[i]
    for j in range(0,len(array2)):
        o = array2[j]
        k = j
        for m in range(j+1,len(array2)):
            if(o > array2[m]):
                k = m
                o = array2[m]
        if(k!=j):
            array2[j],array2[k] = array2[k],array2[j]
if __name__ =="__main__":
    array1 = [1, 5, 9, 10, 15, 20]
    array2 = [2, 3, 8, 13]
    solution(array1,array2)
    print(array1)
    print(array2)
