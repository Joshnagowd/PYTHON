mylist=[12,32,123,43]
newlist=set(mylist)
print(newlist)
newlist.remove(max(newlist))
print(newlist)
print(max(newlist))