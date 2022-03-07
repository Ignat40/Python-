string = "the quick brown fox jumps over the lazy dog"
substring = "the quick "

found = False

for i in range(len(string) - len(substring) +1):
    miss_match = False
    for j in range(len(substring)):
        if string[i+j] != substring[j]:
            miss_match = True

    if miss_match is False:
        found = True

if found:
    print("Found!")
else:
    print("Not found...")