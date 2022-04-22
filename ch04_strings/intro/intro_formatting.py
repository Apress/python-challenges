# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


product = "Apple iMac"
price = 3699

# formatting
print("the", product, "costs", price)
print("the {} costs {}".format(product, price))
print("the %s costs %d" % (product, price))
print(f"the {product} costs {price}")

##################
num = 7

print('{0:0>5d}'.format(num))  # left
print('{0:0<5d}'.format(num))  # right

print('{:05d}'.format(num))

print("%0*d" % (5, num))
print(format(num, "05d"))

temp = 'test'
print(temp.rjust(10, '0'))
print(temp.ljust(10, '0'))
