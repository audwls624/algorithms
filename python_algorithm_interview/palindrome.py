def str_process(s):
    strs = ''
    for char in s:
        if char.isalnum():
            strs += char.lower()
    return strs

def is_palindrome(string):
    processed_string = str_process(string)
    medium = len(processed_string) // 2
    return processed_string[:medium] == processed_string[medium+1:][::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))