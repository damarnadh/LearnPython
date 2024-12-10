greeting = 'Good '
time = 'Afternoon'

#concatinating string
greeting = greeting + time + '!'
print(greeting)

#printing single quote string
message = "It's a message"
print(message)

#printing double quote string
message = '"It is a message!", beautiful'
print(message)

#escaping single quote string
message = '"It\'s a message!", beautiful'
print(message)

#printing raw string
message = r'c:\python\bin,d:/drive/disc'
print(message)

#passing variable in string
message = f'good {time}'
print(message)

#mutiple line string
message = '''
This
was 
multiple
line
message
'''
print(message)

#accessing
print(message[-14:])