import string
import nltk  #Used for tokenizing purposes.
import sys


keyword=[]
rank=[]
probablity=[0]*20
h=0
c=0


for t in range(12):     #here we should put the outer loop.


    print("Enter the chat segment")
    sentence_user= sys.stdin.read()

    temparray=nltk.word_tokenize(sentence_user) # for tokenizing the string.

    s=len(temparray)
    t=len(keyword)

    for i in range(s):

        print(temparray[i])
        choice=raw_input("Excuse me! is this word considerable type 'Y' or 'N' or 'P' :")

        if choice=='Y':
            if temparray[i] not in keyword:

                rank.append(10)
                keyword.append(temparray[i])



        elif choice=='N':
            for j in range(t):

                if temparray[i]==keyword[j]:
                    rank[j]=rank[j]-1

                if rank[j]<0:
                    keyword[j]=='\0'
        elif choice=='P' :
            probablity[h]=temparray[i]
            h=h+1

print(keyword)
print(rank)
