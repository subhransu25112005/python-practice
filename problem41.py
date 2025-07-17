with open("file.txt","r") as file:
    content1 = file.read()
with open("poem.txt","r") as file:
    content2 = file.read()
    if(content1==content2):
        print("YES!These files are identical")
    else:
        print("These files are not identical")
