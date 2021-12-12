#dictionay methods

mydict={
        "fast":"horse is fast",
        "suraj":"hero",
        "marks":[10,90,89,76,88],
        1:2,
        "anotherdict": {"suraj": "scientist"}
        }


print(list(mydict.keys()))
print(list(mydict.values()))
print(mydict.items())
print(mydict)
updatedict= {
    "lovish":"friends",
    "ram":"shyam",
    "lavanya":"superstar",
    "suraj":"Advocate"
    }
mydict.update(updatedict)
print(mydict)
print(mydict.get("suraj"))
print(mydict["suraj"])

#diffrence between get ans [] syntax
print(mydict.get("suraj safi"))
print(mydict["suraj safi"])#not present in dictionary and user is responsible to feed

