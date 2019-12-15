import os
import reference

def search(ch):
    for j in range(84):
        if ch == reference.apparent[j]:
            return j
            break

fn = input("Enter your name of the file to decode : ") 
fn = fn + '.txt'
file1 = open(fn,"r")
file2 = open("temp2.txt","w")
while True:
    ch = file1.read(1)
    if not ch:
        break
    i = search(ch)
    file2.write(reference.real[int(i)])

file1.close()
file2.close()    
os.remove(fn)
os.rename("temp2.txt", fn)
