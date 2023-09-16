with open('/home/advaitnd/Documents/Documents on Laptop/Programming_Languages/Git/My-Notes/Python/Project/Matlib Generator/story.txt', 'r') as f:
    story = f.read()

words = set()
start_word = -1
start_target = "<"
end_target = ">"

for i,char in enumerate(story):
    if char == start_target:
        start_word = i
    if char == end_target and start_word != -1:
        word = story[start_word: i+1]
        words.add(word)
        start_word = -1

dic = {}
for word in words:
    value = input(f"Enter the replacable word for {word}: ")
    dic[word]= value

for word in words:
    story = story.replace(word,dic[word])
print(story)