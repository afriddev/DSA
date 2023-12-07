

def bubbleSort(a):
  sorted = False
  o = len(a)-1 
  while not sorted:
	  sorted = True
	  for i in  range (o):
		  if(a[i]>a[i+1]):
			  sorted = False
			  a[i],a[i+1] = a[i+1],a[i]
    o-=1
  
if __name__ == "__main__":
  a  = [4,7,3,1,97,67]
  bubbleSort(a)
  print(a)
  
  
  
