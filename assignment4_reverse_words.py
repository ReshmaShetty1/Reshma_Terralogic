str=input("Enter the string:")#take input from user

String_array=str.split()#splits the string and adds the data to the string array

fetch_str=String_array[::-1]#fetches the data from end of the list, stores the data to a variable

final_str=' '.join(fetch_str)#return the string in which string elements are separeted by ''

print("Reversed order of the string:",final_str)
