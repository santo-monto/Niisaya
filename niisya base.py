import string
import nltk
import sys  #Used for tokenizing purposes.

keyword=['have', 'news', 'updates', 'events', 'exams', 'Writeup', 'lab', 'assignment', 'Batches', 'file.', 'Batch', 'questions', 'tomorrow', 'file', 'form', 'submitted', 'attending', 'seminar',
        'Email', 'id-', 'gmail.com', 'pesitbsc', 'class', 'mail', 'id', 'presentations', 'tatynerds.com', 'books', 'college', 'Caed', 'submission', 'Tuesday', 'C', "ma'am",
         'write', 'record', 'till', 'where', 'we', 'module', 'holiday', 'update', 'ya', 'inform', 'presentation', 'must', 'teams', 'topics', 'Confirm', 'report','homework','yes']

rank=[8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10,
       10, 10, 10, 10, 10, 10, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,10]

prokeyword=['guess','may','may be',]

nearray=['no','not']

summ=0

print("Enter the chat segment")

tempstring=sys.stdin.read()

temparray=nltk.word_tokenize(tempstring)

uni=set(temparray)

s=len(temparray)
t=len(keyword)

for i in range(s):
    if temparray[i] in prokeyword:

        print("Not predictable")
        exit()
for i in range(s):
    if temparray[i] in nearray:

        print("Negative")
        exit()

for i in range(s):

            for j in range(t):

                if temparray[i] == keyword[j] :

                    summ=summ+10


#print(freq)
#print(temparray)
#print(temparray)

if summ>=10:
    print("important")

##elif:
    ##if temparray in prokeyword:

        #print("Not predictable")

#elif summ<10:

#    print("neutral")
