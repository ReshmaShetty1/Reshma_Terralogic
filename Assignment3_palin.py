#Palindrome function
def palindrome_fun(str):

	string_lower=str.lower()#converts the string to lowercase and stored in a variable
	string_lower=''.join(a for a in string_lower if a.isalnum())#stores the string in a variable if the string is alphanumeric only
	reverse_str=string_lower[::-1]#reads the string from the end 
	#for neat display of the output
	string_array=str.split('\n')
	original_str=''.join(string_array)
	if(reverse_str==string_lower):#checks wether the strings are equal
		print("The string:",original_str,":is Palindrome")
	else:
		print("The string:",original_str,":is Not a palindrome")

#File 
s=input("Enter the File")
with open(s)as f:#opens a file
	fp=f.read()#reads the entire content in the file
	for i in fp.split('.'):#when the file pointer reaches '.', the entier line upto '.' is stored in i
		     palindrome_fun(i)#the line that is stored in i is passed to palindrome_fun()
	


	
		
