from random import randint
from random_word import RandomWords

def mysort(my_list):
  new_list=[]
  while my_list:
    min=my_list[0]
    for i in my_list:
      if i<min:
        min=i
    new_list.append(min)
    my_list.remove(min)
  return new_list

def binary(arr, x):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(high+low)//2
    print(low, high, mid,arr[mid], x)
    
    if arr[mid]>x:
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    else:
      return mid   
  return -1

random_num_list=[]
for i in range(200):
    random_num_list.append(randint(0,1000))

r = RandomWords()
random_word_list=r.get_random_words()




list_type=input("Which type of list would you like to sort and search, words or numbers?")
if list_type=="words":
    print(random_word_list)
    search=input("What word do you want to find?")
    my_list=mysort(random_word_list)
if list_type=="numbers":
    print(random_num_list)
    search=input("What number do you want to find?")
    search=int(search)
    my_list=mysort(random_num_list)


print(my_list)
result=binary(my_list,search)

if result != -1:
  print("Element is present at index "+ str(result)+". This means this is element number "+str(result+1)+" in the list.")
else:
  print("Element is not present in this list")











