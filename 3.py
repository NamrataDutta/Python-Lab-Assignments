import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import ngrams
file = open('word.txt', 'r') #file contents
details = file.read();
lexographic=nltk.WordNetLemmatizer()
characters=word_tokenize(details)
sentences=sent_tokenize(details)
print(sentences)
list1=[]
for line in characters:
    lwords=lexographic.lemmatize(line)
    list1.append(lwords)
print(list1)
print("Bigrams")
sample=[]
bigrams=ngrams(characters, 2) #Bigram operation performed by using ngrams function
for a in bigrams:
    sample.append(a)
print(sample)
frequencydistribution=nltk.FreqDist(sample)
freq=frequencydistribution.most_common()
top5=frequencydistribution.most_common(5)
print("Word frequency of bigrams")
print(freq)
print("Top 5 bigrams")
print(top5)
concatenatesentence=[]
for sentence in sentences:
    for x,y in sample:
        for((word1,word2),count) in top5:
            if(x,y == word1,word2):
                concatenatesentence.append(sentences)
print("Combined sentence")
print(max(concatenatesentence))