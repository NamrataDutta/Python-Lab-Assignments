#User enters the sentence
s = input("Enter the sentence")
#splitting the sentence
mid=s.split()

#calculating the length of the words after the split
a=len(mid)
#if the length of the word is even then it will print 2 words in the middle
if a%2==0:
    x=a/2
    y=int(x-1)

    print("The middle word is :", (mid[y]+" "+mid[y+1]))
else:
    x=int(a/2)
    print(mid[x])
#checking each word with other and which one has more characters
longest = 0
for word in s.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print("The longest word is : %s" % longest_word)
#each letter goes to the front of the word and joined to get reversed words
def reversed_words(sequence):

    return ' '.join(word[::-1] for word in sequence.split())
print("Sentence with reversed words is : ", reversed_words(s))

