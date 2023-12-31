# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dic = dict()
for line in handle:
    if "From" in line and "From:" not in line:
        line = line.split()
        word = line[5][:line[5].find(":")]
        dic[word] = dic.get(word, 0) + 1

lst = sorted([(k, v) for (k, v) in dic.items()])
for (k, v) in lst: print(k, v)

