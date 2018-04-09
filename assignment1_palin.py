def palindrome_fun(str):
	string_lower=str.lower()
	if str=="":
	   return True

	string_lower=''.join(a for a in string_lower if a.isalnum())

	reverse_str=string_lower[::-1]

	if(reverse_str==string_lower):
		return True
	else:
		return False

s=input("Enter the string")
p=palindrome_fun(s)
if(p==1):
	print("Palindrome")
else:
	print("Not a Palindrome")
