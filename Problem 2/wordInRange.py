def wordInRange():
    #Type your code here
    try:
        with open(str(input()),"r") as inFile:
            lower = str.lower(str(input()))
            upper = str.lower(str(input()))
            if(lower>upper): #this method of checking for faulty imputs should be self-explanatory
                print("No such range exists. The first input should be the higher number on an alphabetized list.")
            else:
                line=str(inFile.readline()).rstrip("\n")
                while(line!=""):
                    line=line.strip("\n")
                    if(lower<=line<=upper): #turns out you can absoluetly use a double inequality instead of an "and" setup
                        print(f'{line} - in range')
                    else:
                        print(f'{line} - not in range')
                    line=inFile.readline()
    except FileNotFoundError:
        print("File not found.")

if __name__ == '__main__':
    wordInRange()