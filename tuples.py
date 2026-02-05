mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Own examples:
yourtuple = ("orange", "kiwi", "grape")
thistuple = tuple(("orange", "kiwi", "grape")) # note the double round-brackets
theirtuple = ("mango", "coconut", "grape")
ourtuple = ("aaa", 'a', 123, 45.6, True)
histuple = (True, False, True, False)

print(type(yourtuple))

#NOT a tuple
notatuple = ("orange")
print(type(notatuple))


