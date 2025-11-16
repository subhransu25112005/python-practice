marks = {
    "Gugu" : 34,
    "gax" : 78,
    "hari" : 89,
    "ramu" : 67,
    "Govind" : 37,
    "Gudu" : 85
}
print(marks)
print(marks.keys())
print(marks.values())
marks.items()
print(marks)
print(marks.get("ramu"))
print(marks["ramu"])
marks["ramu"] = 90
print(marks)
marks["santosh"] = 30
print(marks)
marks.pop("Govind")
print(marks)
#print(marks.popitem())
#marks.clear()
#print(marks)
print(marks.keys())
for key in marks:
    print(key)