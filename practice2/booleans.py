
# W3 Examples:

# №1:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# №2:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# №3:
print(bool("Hello"))
print(bool(15))

# №4:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# №5:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# №6:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# №7:
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

# №8:
def myFunction() :
  return True
print(myFunction())

# №9:
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

# №10:
x = 200
print(isinstance(x, int))


# Own examples:

# №1:
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 3)
print(5 >= 5)

# №2:
a = 1
b = 2
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# №3:
print(bool("Python"))
print(bool(0))

# №4:
x = ""
y = 42
print(bool(x))
print(bool(y))

# №5:
bool("test")
bool(0.0)
bool([1, 2, 3])

# №6:
bool(True)
bool(1)
bool(-1)
bool((1, 2))
bool({1: "a"})

# №7:
class MyClass:
    def __len__(self):
        return 0
my_obj = MyClass()
print(bool(my_obj))

# №8:
def check_even(num):
    return num % 2 == 0
print(check_even(4))

# №9:
def is_positive(num):
    return num > 0
if is_positive(-1):
    print("Positive")
else:
    print("Not Positive")

# №10:
y = 3.14
print(isinstance(y, float))
