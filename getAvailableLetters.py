def getAvailableLetters():
    
    lettersGuessed = input("Input a list of letters: ")
    
    import string
    lowerCaseLetters = string.ascii_lowercase
    notInLettersGuessed = ''
    
    for letter in lowerCaseLetters:
        if letter not in lettersGuessed:
            notInLettersGuessed = notInLettersGuessed + letter
    return notInLettersGuessed