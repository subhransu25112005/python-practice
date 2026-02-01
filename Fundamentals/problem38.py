with open("poem.txt",'r') as file:
    content = file.read()
    if("twinkle" in content):
        print("Twinkle is present")
    else:
        print("twinkle is not present")