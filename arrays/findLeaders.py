def findLeaders(array):
    leaders = []
    for i in range(len(array)):
        element = array[i]
        leader = True
        for j in range(i+1,len(array)):
            if(array[j] > element):
                leader = False
        
        if(leader):
            leaders.append(array[i])
    for k in leaders:
        print(k,end=" ")
if __name__ == "__main__":
    array = [17,16,4,8,35,34,3,2,1]
    findLeaders(array)
