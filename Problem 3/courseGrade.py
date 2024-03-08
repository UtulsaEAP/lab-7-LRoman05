"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def courseGrade():
    
    # TODO: Declare any necessary variables here. 
      LineData=[]
      MainData=[]
      ClassAvg=[0,0,0]
      file = str(input())
      reportNum = file.strip(' 3/.bdefIlmnoPprSstuvx')
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
      with open(file,"r") as grades:
           LineData=grades.readline()
           while(LineData!=""):
            MainData.append(LineData.split())
            LineData=grades.readline()
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
      with open(f"./Problem 3/report{reportNum}.txt","+w") as Report:
          for i in range(0,len(MainData)):
              GradeAvg=(float(MainData[i][2])+float(MainData[i][3])+float(MainData[i][4]))/3
              MainData[i].append(['F','F','F','F','F','F','D','C','B','A','A'][int(GradeAvg//10)])
              printStr=""
              for x in MainData[i]:
                  printStr+=x+"\t" #remain professional. Remain Professional... No profanity. Ok. The TABs in the expected output were something I didn't notice for the longest time.
              Report.write(printStr.strip("\t")+"\n")
          for i in range(0,len(MainData)):
              ClassAvg[0] += float(MainData[i][2])
              ClassAvg[1] += float(MainData[i][3])
              ClassAvg[2] += float(MainData[i][4])
          Report.write(f'Averages: midterm1 {ClassAvg[0]/len(MainData):.2f}, midterm2 {ClassAvg[1]/len(MainData):.2f}, final {ClassAvg[2]/len(MainData):.2f}')

if __name__ == "__main__":
    courseGrade()
    
    