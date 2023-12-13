def solution(array,query):
    for i in range(0,len(query)):
        totalSum =0
        for j in range(query[i][0],query[i][1]+1):
            totalSum = totalSum + array[j]
        print("Sum of elements in range {query} is {result}".format(query = query[i],result = totalSum))
if __name__ == "__main__":
    array = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    query = [[0, 4], [1, 3], [2, 4]]
    solution(array,query)
