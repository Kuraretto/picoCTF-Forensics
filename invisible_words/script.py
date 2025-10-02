bytes = []

fileObj = open("hex", "r")

bytes = fileObj.read().split() #load hex into list, with ecah element being a single byte 

fileObj.close()
 
p1 = bytes[0::4] #put every 4th byte into p1, starting with index 0
p2 = bytes[1::4] #put every 4th byte into p2, starting with index 1

zipstring = " "

for f,b in zip(p1,p2):
 zipstring += f
 zipstring += b
 
print(zipstring)
