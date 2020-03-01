import re

alf = 'абвгдежзийклмнопрстуфхцчшщыьэюя'


def format(text1):
    text = text1.lower()
    format_arr = re.findall(r'[а-яё]', text)
    format_text = ''.join(format_arr).replace('ё', 'е')
    return format_text


def crypt(text, key):
    # alf = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
    crypt_text = ''
    for letter in text:
        for letter_key in key:
            key = key[1::] + letter_key
            crypt_text += alf[(alf.index(letter_key) + alf.index(letter)) % len(alf)]
            break
    return crypt_text



def decrypt(crypt_text, key):
    decrypt_text = ''
    for letter in crypt_text:
        for letter_key in key:
            key = key[1::] + letter_key
            decrypt_text += alf[(alf.index(letter) - alf.index(letter_key)) % len(alf)]
            break
    return decrypt_text
