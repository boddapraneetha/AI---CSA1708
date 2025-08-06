sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

sorted_sentence = ' '.join(words)

print("Sorted sentence:")
print(sorted_sentence)
