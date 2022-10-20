import re

random = open("random.txt").read()
#flag = open("flag.txt").read()

#random += flag
random += random[:-1]

query = input("What are you looking for? ")

results = re.findall("[a-z][A-Z]*?" + query + "[a-z]*?\n", random)
print(*results, sep = "\n")
