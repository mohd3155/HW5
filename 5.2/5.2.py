
# EX1

keys=['Ten','Twenty','Thirty']
values=[10,20,30]

dictionary=dict()

for item in range(len(keys)):
    dictionary[keys[item]] = values[item]

print(dictionary)

# EX2

sample_dict ={
    "name": "kelly",
    "age" : 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict.pop('name')
sample_dict.pop('salary')
print(sample_dict)