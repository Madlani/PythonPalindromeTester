#Palindrome Question
#Print whether a given string is a Palindrome

def basicPalindromeTest(stringToTest):
	print (stringToTest == (stringToTest[::-1]))

#Now, print whether a given string is a palendrome regardless of case & spaces

def palendromeTestEnhanced(stringToTest):
    stringToTest = stringToTest.lower()
    stringToTest = stringToTest.replace(" ", "")#removes spaces
    print (stringToTest == (stringToTest[::-1]))
