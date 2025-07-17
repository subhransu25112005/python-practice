words = {
    "chair" :"kurshi",
    "window":"khidki",
    "wall":"dibaar"
}
word = input("Enter your word here: ")
if(word in words):
    print(words[word])
else:
    print("Word is not found!")
