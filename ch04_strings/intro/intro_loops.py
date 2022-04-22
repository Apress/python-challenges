# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


message = "Python has several loop variants"
for i in range(len(message)):
    print(i, message[i], end=',')

for i, current_char in enumerate(message):
    print(i, current_char, end=',')

for current_char in message:
    print(current_char, end=',')

