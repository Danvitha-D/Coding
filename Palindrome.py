# str = input("Enter a Text:")
# if str == str[::-1]:
#     print("the text is palindrome")
# else:
#     print("the text is not a palindrome")

# num= int(input("Enter the input in numbers: "))
# temp = num
# rev= 0
# while num >0:
#     digit = num % 10
#     rev = rev* 10 + digit
#     num= num//10
# if temp == rev:
#     print("number is palindrome")
# else:
#     print("number is not a palindorme")

text = input("enter a text: ")
rev = ""
for i in text:
    rev = i + rev
if text == rev:
    print("palindrome")
else:
    print("not a palindrome")
   


