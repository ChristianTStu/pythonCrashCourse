#To add whitespace 
#\t adds a tab to your text

print("Python")
print("\tPython")

# \n adds a newline in a string

print("Languages:\nPython\nC\nJavascript")

# To strip whitespace on the right side of the string use the method rstrip()

favorite_language = 'python '
print(favorite_language)

print(favorite_language.rstrip())

# To strip whitespace on the left side of the string use the method lstrip()

favorite_language1 = ' python'
print(favorite_language1)

print(favorite_language1.lstrip())

# To strip whitespace on the all sides of the string use the strip() method.

favorite_language2 = ' python '
print(favorite_language2)

print(favorite_language2.strip())