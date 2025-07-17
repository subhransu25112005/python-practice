with open("old.txt",'r') as f:
    content = f.read()
    with open("new.txt","w") as f:
        f.write(content)
