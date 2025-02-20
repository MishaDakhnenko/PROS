def capitalize_name(s):
    return ' '.join(word.capitalize() for word in s.split())
s = input().strip()
print(capitalize_name(s))

