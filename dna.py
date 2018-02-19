
file_text = open("gc.txt") .read()

n = len(file_text)
c = 0
g = 0

for i in range (0,n):
    if file_text[i]=="C":
        c = c + 1
    else:
        c = c + 0
    if file_text[i]=="G":
        g = g + 1
    else:
        g = g + 0

    A = c + g

    print ("The length of the DNA is ", len(file_text))
    print ("The number of C letters: ")
    print ("The number of G letters: ")
    print ("Percentage of C+G: ", (100.00*A)/n)
