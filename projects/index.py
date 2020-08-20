# calculate the sum of all numeric values.
# return the sum of values that == to int
# print the sum
# what is the big(o) time and space? 



def the_sum(values):
    sum = 0
    for v in values.keys():
       if(type(values[v])== int):
        sum = sum + values[v]
    return sum
        
d = {
        "cat": "bob",
        "dog": 23,
        19: 18,
        90: "fish"
        }

print(the_sum(d)) 