def solution(string,key):
    for i in string:
        if i == key:
            return "found"
    return "notFound"
if __name__ == "__main__":
    string = 'afrid'
    key = 'd'
    result = solution(string,key)
    print(result)
