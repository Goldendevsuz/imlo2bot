from difflib import get_close_matches

from .uzwords import words

def check_word(word,words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False # bunday so'z mavjud emas

    if word in matches:
        available = True # mavjud
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}

if __name__ == '__main__':
    print(check_word("ҳато"))
    print(check_word("тариҳ"))
    print(check_word("хато"))
    print(check_word("олма"))
    print(check_word("ҳат"))
    print(check_word("ҳайт"))




