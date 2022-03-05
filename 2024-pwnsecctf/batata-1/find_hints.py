import itertools

# Function to try and fill in the '?' in a binary string
def generate_possible_values(binary_hint):
    # Find positions of '?'
    question_mark_positions = [i for i, c in enumerate(binary_hint) if c == '?']
    
    # Generate all combinations of '0' and '1' for the positions of '?'
    possibilities = []
    for bits in itertools.product('01', repeat=len(question_mark_positions)):
        hint_list = list(binary_hint)
        for i, pos in enumerate(question_mark_positions):
            print("generating...")
            hint_list[pos] = bits[i]
        possibilities.append(''.join(hint_list))
    
    return possibilities

# Provided values
n = 968434716306234329049790539051148474562570955225198433106955896282324447414567840538259304270045968726065384789159417819966134935021806766869215089169283897959136964436432853959067385452100435697237250348183695901606991260428418817946428764786067388030585201424627203867418391261512331439925537684346763657164285919547275064716652000368669648103158067340898359900741168297192437784557981449852523796034300270332838503916474382637420694720663722431540098864846490924341402049765373120596918247394998693250698779676759962459890610735451766963199130876930624904518341327977064192544431194078765805603578804086399063060447339535497295171780974146844017023441567879801060423234469448682102788420142307916559634197417702341212190793490987952381328514993282475556428895368165971738730327
p_hints = ['11100?10???00?11?10111100??110?000011?????00????1110?11?111??10?0??0010?1?10?0??00??101??1110?0?1?11111?00?010?0???00?11100?1????11?111011000?111100?0??0?1?101??10110?1?0?0???1?0?0110011??00011?0??11?011??01?1001?0????11111????00011111?10??1?00010?01?001100000?10???101?????0?0011?00010?11100011?0010000??011000?00?0111?00001?0??0?1111110?10?0?011011????00101?1100100????11?100??00111??00111?01011?0?1110?11?11001?11101??0????1??10?']
q_hints = ['1?010110?0?0010???000001101??000??0?10??1?0??1???10?1?0?101111110011001??100??010?0??1?1?01?110000111000?10011??0???0111?111??11?1?0?0????10?10?01?1001??1?10110?1?0?001?1?11000?10????0?01?00?0?1?0001??1101?000110?1???0111111?10001000010??0?1???0101?001010000?1?0??00?0000?11111??0???01??00010??110?0?010?0???0001?00111?0010????1?10??0??0?00?1010110?11101?0101?0?0?110?01001?010011?111????1001???1?1?1?1?1?011011?011010?0010????10001']

# Generate possible values for p and q from the hints
p_possibilities = generate_possible_values(p_hints[0])
q_possibilities = generate_possible_values(q_hints[0])

# Convert binary strings to integers
def binary_to_int(binary_str):
    return int(binary_str, 2)

# Check each combination of p and q to see if p * q == n
for p_bin in p_possibilities:
    p = binary_to_int(p_bin)
    for q_bin in q_possibilities:
        print("trying...")
        q = binary_to_int(q_bin)
        if p * q == n:
            print(f"Found valid p and q:")
            print(f"p: {p} (binary: {p_bin})")
            print(f"q: {q} (binary: {q_bin})")
            # Exit after finding the first valid pair
            exit()

print("No valid pair of p and q found.")

