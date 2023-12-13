def solution(array,query):
    for i in range(0,len(query)):
        smallest = array[query[i][0]]
        for j in range(query[i][0],query[i][1]+1):
            if(smallest > array[j]):
                smallest = array[j]
        print("Smallest Number Between {rangeIs} is {answer}".format(rangeIs = query[i],answer = smallest ))
if __name__ == "__main__":
    array = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    query = [[0, 4], [4, 7], [7, 8]]
    solution(array,query)
    
