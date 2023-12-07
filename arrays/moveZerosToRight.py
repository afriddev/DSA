def moveZerosToEnd(array):
    countOfNonZeros = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[countOfNonZeros] = array[i]
            countOfNonZeros+=1
    
    while(countOfNonZeros < len(array)):
        array[countOfNonZeros] = 0
        countOfNonZeros+=1
if __name__ == "__main__":
    array = [1,23,0,53,0,54,0,3,46,0,46,45,2,534,0]
    moveZerosToEnd(array)
    print(array)
