def word_frequency(file):
    with open(file, 'r') as file:
        text = file.read()
    
    word_count = {}
    words = text.split()
    
    for word in words:
        word = word.strip('!?.,:;()').lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word, count in word_count.items():
        print(f"{word}: {count} time(s).")

word_frequency('sometext-1.txt')
