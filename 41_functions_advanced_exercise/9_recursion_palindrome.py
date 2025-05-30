def palindrome(word, index):
    if len(word)//2 == index:
        return f'{word} is a palindrome'
    if word[-(index+1)] != word[index]:
        return f'{word} is not a palindrome'
    return palindrome(word, index+1)





print(palindrome("peter", 0))