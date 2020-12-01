delimeter = ","
list_of_words = ["hello", "yes", "goodbye", "last"]
for i in range(len(list_of_words)):
    if i < len(list_of_words)-1:
        print(list_of_words[i], end=delimeter)
    else:
        print(list_of_words[i])
