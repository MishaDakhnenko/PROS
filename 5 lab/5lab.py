import re

n = int(input())
for _ in range(n):
    card = input().strip()
    if re.match(r'^[456](\d{15}|\d{3}(-\d{4}){3})$', card) and not re.search(r'(\d)\1{3,}', card.replace('-', '')):
        print("Valid")
    else:
        print("Invalid")
