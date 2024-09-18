allowed = "abc"

x = ["a","b","c","ab","ac","bc","abc"]
for i in x:
    if allowed in i or i in allowed or  i in allowed[i]:
        print(True)
    else:
        print( False)
