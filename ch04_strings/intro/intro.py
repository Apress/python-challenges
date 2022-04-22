# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


str1 = 'String with same contents but different quotes'
str2 = "String with same contents but different quotes"
str3 = "String with same contents but " + "XXX quotes".replace("XXX", "different")

print("str1:", str1)
print("str2:", str2)
print("str3:", str3)

if str1 == str2:
    print("same content")
if str1 is str2:
    print("reference str1 / str2 equal")
if str1 == str3:
    print("same content")
if str1 is str3:
    print("reference str1 / str3 equal")

print(list("Text as List"))


name = "Carl Heinz Miller"
print(name.lower())
print(name.upper())

print(name.split())

time = '20:26:45'
hrs, mins, secs = time.split(':')
print(hrs, mins, secs)


print("-repeater-" * 3)

with_whitespace = "  --CONTENT--  "
stripped1 = with_whitespace.strip()
stripped2 = stripped1.strip("-")
print("strip1:", stripped1, "length: ", len(stripped1))
print("strip2:", stripped2, "length: ", len(stripped2))

