"""
Write a program to fill in a letter template given below with name and date. 
letter = ''' Dear <|Name|>, 
             You are selected! 
             <|Date|> 
'''

"""
name = input("Enter you name: ")
date = input("Enter date (DD-MM-YYYY): ")
# This is only the one way of doing this from hundreds.
letter = f"""Dear <|{name}|>,
You are selected!
<|{date}|>"""

print(letter)