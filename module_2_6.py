def single_root_words(root_word, *other_words):
    same_words = []
    other_words = list(other_words)
    for i in range(len(other_words)):
        a = other_words[i].lower()
        b = root_word.lower()
        if b in a or a in b:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich',
                            'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement',
                            'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
