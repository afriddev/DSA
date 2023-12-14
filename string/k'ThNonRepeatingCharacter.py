def solution(string,key):
    emptyArray = []
    for i in string:
        char = i
        count = 0
        for j in string:
            if(i == j):
                count+=1
        if(count == 1):
            emptyArray.append(char)
    print(emptyArray[key-1])
if __name__ == "__main__":
    string = 'geeksforgeeks'
    key = 3
    solution(string,key)
