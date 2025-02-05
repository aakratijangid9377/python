def rem(l,word):
    for item in l:
        l.remove(word)
        return True

l = ["aakrati", "shubham", "mahendra", "rohan", "an"]
print(rem(l, "an"))
print(l)