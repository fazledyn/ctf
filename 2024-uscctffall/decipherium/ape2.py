import sys

f = sys.argv[1]
content = open(f).read()

elements = content.split(" ")

periodic_table = {
    'Te': 52, 'Sb': 51, 'I': 53, 'La': 57, 'Sn': 50, 'No': 102,
    'Cs': 55, 'Dy': 66, 'Cd': 48, 'In': 49, 'Ba': 56, 'Yb': 70,
    'Xe': 54, 'Ho': 67, 'Fm': 100, 'Md': 101, 'Er': 68
}

decoded = ''
for element in elements:
    if element in periodic_table:
        decoded += chr(periodic_table[element])
    
print(decoded)
