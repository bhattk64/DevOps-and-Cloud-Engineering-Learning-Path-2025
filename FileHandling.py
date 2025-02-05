#to open a file
f=open("sample.txt","a")
f.write("hello world")
f=open("sample.txt","r")
print(f.read())

#"x"=create-will create a file,return an error if the file exists
#"a"=append-will create a file if the specified file dosent exists
#"w"=write-will create a file if the specified file doesnt exists

#for deleting you must import os model
import os
os.remove("sample.txt")
