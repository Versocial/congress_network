
print("sdfsd")
f=open("congress.edgelist","r")
with open("congress.edgelist.csv","w")as out:
    out.write("s,t,w\n")
    for line in f.readlines():
        things=line.replace("}",' ').split(" ")
        print(things)
        out.write("{},{},{}\n".format(things[0],things[1],things[3]))
f.close()