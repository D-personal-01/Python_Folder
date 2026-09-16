
#Q8. Write your own version of the replace() function. (CO2). Ask the user to input a sentence, a target word, and a replacement word. Replace all occurrences of the target word with the new word without using Python’s built-in replace() function. 


s = input("Enter a sentence: ")
a = input("Enter target word: ")
b = input("Enter replacement word: ")

w = s.split()
for i, word in enumerate(w):
    if word == a:
        w[i] = b

res = " ".join(w)
print("New sentence:", res)