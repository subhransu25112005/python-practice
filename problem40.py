word = "Donkey"
with open("file.txt","r") as file:
    content = file. read()
    content_new = content.replace(word,"#####")
    with open("file.txt","w") as file:
        file.write(content_new)