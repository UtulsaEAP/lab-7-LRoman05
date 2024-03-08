def fileNameChange():
    #type your code here
    try:
        with open(input(),"r") as Photos:
            Line=Photos.readline()
            while(Line!=""):
                Line=Line.strip("\n")
                output=Line.split("_")
                output=output[0]+"_info.txt"
                print(output)
                Line = Photos.readline()
    except FileNotFoundError:
        print("File not found.")



if __name__ == '__main__':
    fileNameChange()