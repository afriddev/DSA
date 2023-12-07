def reverseArray(array,start,end):
    while start < end :
        array[start],array[end] = array[end],array[start]
        start+=1
        end-=1
if __name__ == "__main__":
    unSortedArray = [2,42,1,5,66,3]
    start = 0
    end = len(unSortedArray)-1
    reverseArray(unSortedArray,start,end)
    print(unSortedArray)
    
