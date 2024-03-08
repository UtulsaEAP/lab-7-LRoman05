"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def exceptionHandling():
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != '-1':
        # FIXME: The following line will throw ValueError exception.
        #        Insert try/except blocks to catch the exception.
        try:
            age = int(parts[1]) + 1
            print(f'{name} {age}') # I don't need to do it this way, but I want it to also catch errors if the input is lacking spaces
        except ValueError:
            age = 0
            print(f'{name} {age}')
        except IndexError:
            print(f'Does {name} not have an age?')
        #Here is where the print code would go, if I didn't add an extra feature to this
        # Get next line
        parts = input().split()
        name = parts[0]

if __name__ == '__main__':
    exceptionHandling()