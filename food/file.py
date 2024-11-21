# file create/write
"""
# with open('samia.txt',"w") as myFile:
    
# myFile.write("print('Hello')")
"""
  
## Read file
"""
#   with open("samia.txt","r") as myFile:
#   content =myFile.read()
#   print(content)
 """
#file rename  
"""
    import os
os.rename("samia.txt","samiaa.txt")
"""
# delete file 
"""
import os
os.remove("samiaa.txt")

"""
#create folder
"""
import os
os.mkdir("ostad/4")

"""

# directory rename
"""
import os
os.rename("ostad/4" ,"ostad/4_1")

"""
# delete directory

"""
import os
os.mkdir("ostad")


"""
# how zip a directory?

"""
import shutil
shutil.make_archive("ostad1" ,'zip' ,"ostad")

"""
# How to extract zip file?
"""
import zipfile
with zipfile.ZipFile("ostad1.zip", "r") as MyZipFile:
MyZipFile.extractall()
"""
# How to make csv file from list?
"""
with open("testcases.csv",mode='w',newline='') as  csvFile:
    csvFileWriter= csv.writer(csvFile)
    csvFileWriter.writer
   """
   
   # How to read csv file?
   
"""
with open("testcase.csv",mode="r") as myFile:
 myFileReader = csv.reader(myFile)  
      
for row in myFileReader:
 print(row)
 
 """
 #Error Handling 
 
 # gentle shutdown
 
try:
     with open("abc.txt", "r") as file:
         content = file.read()
         num=10/0
         
except Exception as e:
     print(f"error type is :{e}")
     
finally:           
    print("somehting went wrong ! please try again later")