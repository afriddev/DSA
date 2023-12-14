def solution(string,to):
    resultString = string[to:len(string)] + string[0:to]
    return resultString
if __name__ == "__main__":
    string = 'ridaf'
    to = 3
    result = solution(string,to)
    print(result)
