
r_data = open("random.txt", "r").readlines()
o_data = open("out.txt", "r").readlines()

for each in o_data:
    if each not in r_data:
        print(each)