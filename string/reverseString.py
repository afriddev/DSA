def solution(string):
    resultString = ''
    o = -1
    for i in string:
        resultString = resultString + string[o]
        o-=1
    return resultString
    
if __name__ == "__main__":
    string = 'afrid'
    result = solution(string)
    print(result)
