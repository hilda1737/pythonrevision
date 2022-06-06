# Write a Python script to sort (ascending and descending) a dictionary by value
# Write a Python script to add a key to a dictionary.
dictt={2:2,4:5,7:8,6:8,8:9}
dict2=dictt.update({4:6})
print(dictt)
# Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4={}
for c in (dic3,dic1,dic2):
    dict4.update(c)
print(dict4)
# Write a Python script to check whether a given key already exists in a dictionary.
dict={2:'green',3:'black',6:'blue'}

print(dict.get(4))
# Write a Python program to iterate over dictionaries using for loops.
words={2:'green',3:'black',6:'blue'}
for c in (words.keys(),words.values()):
    print(c)
    # Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
    # Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
x={}

for values in (1,15):
    if values<=15:
        values.update({x})
        #   x[1]=1*1

        print(x)



d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
#     d[x]=x*x
  print(d) 
# #  Write a Python program to multiply all the items in a dictionary.





figures={1:2,2:4,5:5,4:6}
multi=1
for key in figures:
     multi=multi*multi[key]
print(multi)
    
# my_dict = {'data1':100,'data2':-54,'data3':247}
# result=1
# for key in my_dict:    
#     result=result * my_dict[key]

# print(result)
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
# Write a Python program to sum all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict))
