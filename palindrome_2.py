def is_palindrome(text):
    clean_text = text.lower().replace(' ', '')
    return clean_text == clean_text[::-1]

def find_palindrome(source):
    longest = ''
    for start in range(len(source) - 2):
        for end in range(start + 2, len(source)):
            part = source[start:end]
            if is_palindrome(part) and len(part) > len(longest):
                    longest = part
    return longest

def find_all_palindromes():
    return [
        find_palindrome(source)
        for source in [
            'hellol howow are you?',
            'adcccbdaabcdc',
            'cdcacccccaacbccbbdcabcabdbbb',
            'Sam, was it a cat I saw?',
            'abc' * 100 + 'No lemon, no melon' + 'def' * 100
        ]
    ]

if __name__ == '__main__':
    find_all_palindromes()
