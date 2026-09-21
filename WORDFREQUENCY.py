Sentence=(input("Enter a sentence: "))
words=Sentence.split()
frequency={}
count=0
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
for word,count in frequency.items():
    print(word,":",count)
print(frequency)