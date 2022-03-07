string_01 = "Thi(s is) (a very annoy)ing ((se(n)tence)) with some (brackets)"
string_02 = "This i(s a v)ery ann)oy(ing sentence w((i)th so)me (b(r(a(pesho(k(e(t(s))))))))"

counter = 0

counter = 0
is_balanced = True

for character in string_01:
    if character == "(":
        counter += 1
    elif character == ")":
        counter -= 1
        if counter < 0:
            is_balanced = False
            break

if is_balanced:
    print("Balanced brackets")
else:
    print("Not balanced brackets")

for character in string_02:
    if character == "(":
        counter += 1
    elif character == ")":
        counter -= 1
        if counter < 0:
            is_balanced = False
            break

if is_balanced:
    print("Balanced brackets")
else:
    print("Not balanced brackets")