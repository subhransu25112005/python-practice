words = {
    "chair" :"kurshi",
    "window":"khidki",
    "wall":"dibaar" ,
    "roof" : "chat" ,

}
word = input("Enter your word here: ")
if(word in words):
    print(words[word])
else:
    print("Word is not found!")
