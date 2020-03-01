import metods


def seach_len_key(crypt_text):
    rang_reply = {}
    max_reply = 0
    len_key = 0
    for distans in range(1, 31):
        # print('distans :'+str(distans))
        count = 0
        for num in range(len(crypt_text) - distans):
            #    print( crypt_text[num]+'<>'+crypt_text[num+distans])
            if crypt_text[num] == crypt_text[num + distans]:
                #       print("----equal------")
                count += 1
        #  print('next num')
        rang_reply[distans] = count
    print(rang_reply.values())
    len_key = int(input())
    return len_key


def separate(len_key, crypt_text):
    arr_letter = []
    for count in range(len_key-1):
        count_in_text = 0
        str = ''
        while count_in_text < len(crypt_text) - len_key:
            str += crypt_text[count + count_in_text]
            count_in_text += len_key
        arr_letter.append(str)
    return arr_letter


def seach_popular_letter(str):
    rating = {}
    for letter_alf in metods.alf:
        value = 0
        for letter_str in str:
            if letter_alf == letter_str:
                value += 1
        rating[letter_alf] = value
    most_reply_letter = ''
    max_value = max(rating.values())
    for key, value in rating.items():
        if value == max_value:
            most_reply_letter = key
    print(rating.items())
    print(max_value, most_reply_letter)
    return most_reply_letter


def seach_key(letter):
    return metods.alf[metods.alf.index(letter) - metods.alf.index('о') % len(metods.alf)]
