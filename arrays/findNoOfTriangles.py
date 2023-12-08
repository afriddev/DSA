def findNoOfTriangles(array):
    count = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                if( array[i]+array[j] > array[k] and array[i]+array[k] > array[j] and array[j]+array[k] > array[i] ):
                    count += 1
    return count
if __name__ == "__main__":
    array = [10, 21, 22, 100, 101, 200, 300]
    result = findNoOfTriangles(array)
    print(result)
    
