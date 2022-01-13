def binary(arr, x):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(high+low)//2
    print(low, high, mid, x)
    
    if mid>x:
      high=mid-1
    elif mid<x:
      low=mid+1
    else:
      return mid   
  return -1

nums=[]
for i in range(101):
    nums.append(i)
numsearch=int(input("What number do you want to find?"))
result=binary(nums,numsearch)

if result != -1:
  print("Element is present at index "+ str(result)+". This means this is element number "+str(result+1)+" in the list.")
else:
  print("Element is not present in this list")
