def solution(array):
    emptyArray = []
    for i in range(0,len(array)):
        o = array[i]
        k = i
        for j in range(i+1,len(array)):
            if(o > array[j]):
                o = array[j]
                k = j
        array[i],array[k]= array[k],array[i]
if __name__ == "__main__":
    array= [0,1,0,2,0,2,1,0]
    solution(array)
    print(array)
    
