import string
str = input("Введіть рядок: ")
str1 = ''.join(char for char in str if char.isalnum() or  char == ' ')
qwe = str1.split()
hashtag = '#'
for word in qwe:
    hashtag += word.title()
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
print(hashtag)
