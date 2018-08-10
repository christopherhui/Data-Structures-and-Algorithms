def isPalindrome(string):
    string = string.lower()

    if len(string) == 1:
        return True
    else:
        if string[0] == ' ':
            return isPalindrome(string[1:len(string)])

        elif string[len(string) - 1] == ' ':
            return isPalindrome(string[0:len(string) - 1])

        elif string[0] == string[len(string) - 1]:
            return isPalindrome(string[1:len(string) - 1])

        else:
            return False


print(isPalindrome("racecar"))
print(isPalindrome("lamp"))
print(isPalindrome("kayak"))
print(isPalindrome("Aibohphobia"))
print(isPalindrome("Live not on evil"))
print(isPalindrome("Go hang a salami; Im a lasagna hog"))

