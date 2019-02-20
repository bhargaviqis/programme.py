def reverseWordSentence(Sentence):  
    words = Sentence.split(" ") 
    newWords = [word[::-1] for word in words] 
    newSentence = " ".join(newWords) 
    return newSentence
Sentence = "she is very beautiful"
print(reverseWordSentence(Sentence)) 
