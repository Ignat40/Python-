string = "the quick brown fox jumps over the lazy dog"
character = "1"

is_found = False

for i in string:
    if i == character:
        is_found = True
        

if is_found:
    print("Character found!")
else:
    print("Charatcter was not found...")