def solution(string):
    resultString = ''.join(sorted(string))
    return resultString
if __name__ == "__main__":
    string = 'afrid'
    result = solution(string)
    print(result)
