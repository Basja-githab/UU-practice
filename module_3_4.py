def single_root_words(root_word, *other_words):
    sawe_words = []
    root_word = root_word.lower()
    len_root_word = len(root_word)              # длина root_word
    short_word = other_words[0]
    for word in other_words:
        if len(word) < len(short_word):
            short_word = word                   # самое короткое слово в other_words
    if len_root_word < len(short_word):         # root_word короче всех слов в other_words
        for word in other_words:
            word = word.lower()
            if word.count(root_word) > 0:       # root_word входит в  word
                sawe_words.append(word)
        return sawe_words
    else:                                       # root_word длиннее всех слов в other_words
        for word in other_words:
            word = word.lower()
            if root_word.count(word) > 0:
                sawe_words.append(word)
        return sawe_words

print(single_root_words ('Rich', 'richIest', 'Orichalcum', 'Cheers', 'richieS'))
print(single_root_words ('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))