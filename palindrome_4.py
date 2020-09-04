def is_palindrome(text):
    clean_text = text.lower().replace(' ', '')
    for i in range(int(len(clean_text) / 2)):
        if clean_text[i] != clean_text[-(i + 1)]:
            return False
    return True

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
