def is_palindrome(text):
    clean_text = text.lower().replace(' ', '')
    return clean_text == clean_text[::-1]

def find_palindrome(source):
    for length in range(len(source), 1, -1):
        for start in range(len(source) - length):
            end = start + length
            part = source[start:end]
            if is_palindrome(part):
                return part
    return None

def find_all_palindromes():
    return [
        find_palindrome(source)
        for source in [
            'hellol howow are you?',
            'adcccbdaabcdc',
            'cdcacccccaacbccbbdcabcabdbbb',
            'Sam, was it a cat I saw?',
            'abc' * 20 + 'No lemon, no melon' + 'def' * 20
        ]
    ]

if __name__ == '__main__':
    find_all_palindromes()
