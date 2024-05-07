# # # # # str = "Hello World"

# # # # # subString = str[0:5]    # slicing 

# # # # # print(subString)

# # # # # str = "hello world!, abe def ghi"

# # # # # print(str.upper())

# # # # # print(str.lower())

# # # # # print(str.capitalize())

# # # # # print(str.title())

# # # # # heading = "population in pakistan"

# # # # # print("Before using Title Method:", heading)
# # # # # print("After using Title Method:", heading.title())
# # # # # print("Capitalize Method: ", heading.capitalize())

# # # # # -> strip(), lstrip(), rstrip()

# # # # # str = "      Hello     "

# # # # # leftSide = str.lstrip()
# # # # # print("Remove left side blank spaces:", leftSide)

# # # # # rightSide = str.rstrip()
# # # # # print("Remove right side blank spaces:", rightSide)

# # # # # bothSides = str.strip()
# # # # # print("Remove both side blank spaces:", bothSides)

# # # # # replace()
# # # # str = "Hello World of gamming"

# # # # newStr = str.replace("World", "Universe")

# # # # print(newStr)

# # # # find()
# # # # str = "Hello World"

# # # # print(str.find("is"))

# # # # startswith(), endswith()

# # # str = "Hello WorlD"

# # # lowerCase = str.lower()

# # # # print(str.startswith("h"))
# # # print("Without lower case:", str.endswith("d"))
# # # print("With Lower Case: ",lowerCase.endswith("d"))

# # # isdigit(), isalpha(), isalnum()

# # str = input("Enter Character: ")

# # # newStr = str.isalpha()

# # # print("Upper Case:", newStr.upper())
# # # newStr = str.isdigit()

# # # print(newStr)

# # newStr = str.isalnum()
# # print(newStr)

# # str = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"

# # length = len(str)

# # print(length)

# str = input("Enter Values: ")

# print(str.isdigit())