def wordcount(text):
    text=text.lower()
    words=text.split()
    global words_freq
    words_freq={}
    for word in words:
        if word in words_freq:
            words_freq[word]+=1
        else:
            words_freq[word]=1
def main():
    text=input("Enter the Sentence Here :")
    wordcount(text)
    print(words_freq)
main()