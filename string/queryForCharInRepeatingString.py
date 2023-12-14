def solution(string,times,query):
    emptyString =''
    for i in range(0,times):
        emptyString = string + emptyString
    for j in query:
        print(emptyString[j[0]:j[0]+1] == emptyString[j[1]:j[1]+1] )
if __name__ == "__main__":
    string = 'geeksforgeeks'
    times = 3
    query = [[0,8],[8,13],[6,15]]
    solution(string,times,query)
