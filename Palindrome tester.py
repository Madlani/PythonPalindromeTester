#Palindrome Question
#Print whether a given string is a Palindrome

def basicPalindromeTest(stringToTest):
	print (stringToTest == (stringToTest[::-1]))

#Now, print whether a given string is a palendrome regardless of case & spaces

def palendromeTestEnhanced(stringToTest):
    stringToTest = stringToTest.lower()
    stringToTest = stringToTest.replace(" ", "")
    print (stringToTest == (stringToTest[::-1]))

def palendromeTestEnhancedUserInput():
	stringToTest = input("Enter string to test")
	str(stringToTest)
	stringToTest = stringToTest.lower()
	stringToTest = stringToTest.replace(" ", "")
	print (stringToTest == (stringToTest[::-1]))

palendromeTestEnhancedUserInput()
