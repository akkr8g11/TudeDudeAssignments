words = ["banana", "apple", "grape", "kiwi", "date"]
sorted_words = sorted(words, key=lambda work:(len(work), work))
print (sorted_words)