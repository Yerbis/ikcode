print('Enter or paste a string(ex: "Hello there I am a human!")')



def counter(istring):
    d = {}
    for c in istring:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

string = input()
result = counter(string)





for key in result:
    print(f"The letter '{key}' was found {result[key]} times")
    