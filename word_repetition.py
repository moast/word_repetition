#This script will tell you exatly how many times each word has been repeated in a given text

textToProcess = input("type text:")
splitTextIntoArray = textToProcess.split()
#example: "she is is tall" ==> ["she","is","is","tall"]

wordRepetationDic = {}
#dictionary contains the result
#example: {"she":1, "is":2, "tall":1}


for x in splitTextIntoArray:
	if x not in wordRepetationDic.keys():
	    wordRepetationDic[x] = 0
	    for j in splitTextIntoArray:
	        if x == j:
	            wordRepetationDic[x] = wordRepetationDic[x] + 1		   	

		
print(wordRepetationDic)
