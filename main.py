# -*-coding: utf8 -*-
import metods
import hack_Vigener

text = 'Мир таков, каков он есть. Трудно предположить, чтобы мир был создан единственно для удовлетворения наших потребностей. Это было бы чудом из чудес. Мир нейтрален. Он не дружествен и не враждебен человеку. Вам внушили, что человек рождается для того, чтобы умереть, и что вы должны всю жизнь терзаться этой мыслью. Чего ради? Смерть - не факт сознания. “Смысл раздумий о смерти в том, что они лишены смысла”, - писал Монтерлан. Смерть близких потрясает нас. А наша собственная? Бояться ее - значит представлять себе и мир, где мы есть, и мир, где нас нет. Эти два образа несовместимы.Вам внушили, что мы живем на краю пропасти…, но даже если мы идем по краю пропасти, ничто не толкает нас вниз.Вам внушили, что старые моральные ценности канули в прошлое . Это ложь… Я напомню вам для начала несколько древних как мир истин…Нельзя жить для себя. Думая только о себе, человек всегда найдет тысячу причин чувствовать себя несчастным. Никогда он не делал всего того, что хотел и должен был делать, никогда не получал всего того, чего, по его мнению, заслуживал, редко был любим так, как мечтал быть любимым. Без конца пережёвывая свое прошлое, он будет испытывать одни сожаления… Зачеркнуть прошлое все равно невозможно, попытайтесь лучше создать настоящее, которым вы… сможете гордиться. Всякий, кто живет ради других - ради своей страны, ради женщины, ради творчества, ради голодающих или гонимых, - словно по волшебству забывает свою тоску…    Второе правило - надо действовать. Вместо того, чтобы жаловаться на абсурдность мира, постараемся преобразить тот уголок, куда забросила нас судьба. Мы не в силах изменить вселенную, да и не стремимся к этому. Наши цели ближе и проще: заниматься своим делом - правильно выбрать его, глубоко изучить и достичь в нем мастерства… Если человек в совершенстве овладел каким-нибудь ремеслом, работа приносит ему счастье.    Третье правило - надо верить в силу воли… Безусловно, никто из нас не всемогущ. Не в моей власти помешать войне, но мои призывы, помноженные на призывы миллионов других людей, ослабят угрозу войны. Я не в силах выиграть битву, но я в силах быть храбрым солдатом, исполнить свой долг. “Возможности наши зависят от того, на что мы дерзнём,” поэтому надо быть всегда в форме. Усилием воли человек заставляет себя трудиться на совесть и совершать геройские поступки. Быть может, воля и есть царица добродетелей.Важно и четвертое правило - надо хранить верность. Верность слову, обязательствам, другим, самому себе.'
key = 'словод'
chek = ''

format_text = metods.format(text)
print('text:         ' + format_text)
crypt_text = metods.crypt(format_text, key)
print('crypt text:   ' + crypt_text)
decrypt_text = metods.decrypt(crypt_text, key)
print('decrypt text :' + decrypt_text)
crypt_text = metods.crypt(format_text, key)
print('crypt text:   ' + crypt_text)

count = 0
while count <= len(format_text) - 1:
    if text[count] == decrypt_text[count]:
        chek += '+'
    else:
        chek += '-'
    count += 1

print('              ' + chek)
len_key = hack_Vigener.seach_len_key(crypt_text)
arr = hack_Vigener.separate(len_key, crypt_text)  # input!!!!!!!!!!!!!!!!
hack_key = ''
for i in range(len_key - 1):
    letter = hack_Vigener.seach_popular_letter(arr[i])
    hack_key += hack_Vigener.seach_key(letter)
print(hack_key)

print('HACK:     '+metods.decrypt(crypt_text,hack_key))