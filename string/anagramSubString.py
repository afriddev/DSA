def solution(string):
    emptyArray = []
    for i in range(0,len(string)):
        if i <2:
            emptyArray.append([string[i:i+1],string[i:i+1]])
        else:
            emptyArray.append([string[0:i],string[len(string)-i:len(string)]])
    print(emptyArray)
if __name__ == "__main__":
    string = "xyyx"
    solution(string)
