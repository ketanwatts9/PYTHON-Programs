def count_vowels(s):
    count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            count += 1
    return count
    
def reverse(s):
    return s[::-1]

def palindrome(s):
    if s == s[::-1]:
        return 'palindrome'
    else:
        return 'not palindrome'
    