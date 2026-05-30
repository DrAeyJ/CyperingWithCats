import random


class CatCyphers:
    def __init__(self):
        self.funcs = {'cipher':
                                {
                                    'aeyj':
                                        {
                                            '1': self.cipher_1,
                                            '2': self.cipher_2,
                                            '3': self.cipher_3
                                        },
                                    'paw-x':
                                        {
                                            '1': self.cipher_1_paw
                                        }
                                },
                    'decipher':
                                {
                                    'aeyj':
                                        {
                                            '1': self.decipher_1,
                                            '2': self.decipher_2,
                                            '3': self.decipher_3
                                        },
                                    'paw-x':
                                        {
                                            '1': self.decipher_1_paw,
                                            '2': self.decipher_2_paw,
                                        }
                                }
        }

    def cipher_1(self, w, shift=0):
         x=[]
         for i in w:
             if i.lower() in ' абвгдеёжзийклмнопрстуфхцчшщьыъэюя': ind=' абвгдеёжзийклмнопрстуфхцчшщьыъэюя'.index(i.lower())
             else: x.append('??'); continue
             if ind==34: x.append('00'); continue
             if ind<10: x.append('0'+str(ind)); continue
             x.append(str(ind))
         return ''.join(x)

    def decipher_1(self, w, shift=0):
         x=[]
         for i in range(0, len(w)-1, 2):
             if w[i]+w[i+1] == '??': x.append('??'); continue
             ha=int(w[i] + w[i+1])
             if int(w[i]+w[i+1]): l = ('абвгдеёжзийклмнопрстуфхцчшщьыъэюя' * 5)[int(w[i] + w[i+1]) - 1]
             elif int(w[i]+w[i+1]) == 0: l=' '
             # noinspection PyUnboundLocalVariable
             x.append(l)
         return ''.join(x)

    def cipher_2(self, w):
        x = []
        ha = ' абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
        for i in w:
            x.append((6 - len(bin(ha.index(i))[2:])) * '0' + bin(ha.index(i))[2:])
        return ''.join(x)

    def decipher_2(self, w):
        setw = ""
        ha = ' абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
        for i in [w[i:i + 6] for i in range(0, len(w), 6)]:
            setw += ha[int(i, 2)]
        return setw

    def cipher_1_paw(self, w):
        ha = {}
        w = "Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites 1. Ну, здравствуйте, здравствуйте. Je vois que je vous fais peur 2, садитесь и рассказывайте. Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и приближенная императрицы Марии Феодоровны, встречая важного и чиновного князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла несколько дней, у нее был грипп, как она говорила (грипп был тогда новое слово, употреблявшееся только редкими). В записочках, разосланных утром с красным лакеем, было написано без различия во всех: Si vous n'avez rien de mieux à faire, Monsieur le comte (или mon prince), et si la perspective de passer la soirée chez une pauvre malade ne vous effraye pas trop, je serai charmée de vous voir chez moi entre 7 et 10 heures. Annette Scherer» Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и приближенная императрицы Марии Феодоровны, встречая важного и чиновного князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла несколько дней, у нее был грипп, как она говорила (грипп был тогда новое слово, употреблявшееся только редкими). В записочках, разосланных утром с красным лакеем, было написано без различия во всех: Dieu, quelle virulente sortie! 4 — отвечал, нисколько не смутясь такою встречей, вошедший князь, в придворном, шитом мундире, в чулках, башмаках и звездах, с светлым выражением плоского лица. Он говорил на том изысканном французском языке, на котором не только говорили, но и думали наши деды, и с теми, тихими, покровительственными интонациями, которые свойственны состаревшемуся в свете и при дворе значительному человеку. Он подошел к Анне Павловне, поцеловал ее руку, подставив ей свою надушенную и сияющую лысину, и покойно уселся на диване."
        haha = []
        x = 1
        for i in w:
            if i.lower() in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
                if i.lower() not in haha:
                    ha[i.lower()] = x; haha.append(i.lower()); x+=1
        ha[0] = ' '
        return ha

    def decipher_1_paw(self, w):
        ha = self.cipher_1_paw()                            #this cipher from my friend is lost, gotta recreate it some time soon
        x=[]
        for i in range(0, len(w), 2):
            x.append(ha[int(w[i] + w[i+1])])
        return ''.join(x)

    def decipher_2_paw(self, w):
        x = []
        ha = self.cipher_1_paw()                            #this cipher from my friend is lost, gotta recreate it some time soon
        for i in range(0, len(w), 6):
            if w[i:i + 6] == '0' * 6: x.append(' '); continue
            x.append(ha[int(w[i:i + 6], 2)])
        return ''.join(x)


    def cipher_3(self, w):
        x=[]
        key = bin(random.randint(123456789123456789, 987654321987654321))[2:]
        binw = bin(int(self.cipher_1(w)))[2:]
        key = (key * (len(binw) // len(key) + 1))[:len(binw)]
        for i in range(len(binw)):
            if key[i] == '1': x.append(binw[i])
            elif key[i] == '0': x.append('1' if binw[i] != '1' else '0')
        x = int(''.join(x), 2); key = int(key, 2)
        return x, key

    def decipher_3(self, w, key):
        x, binw, binkey = [], bin(w)[2:], bin(key)[2:]
        for i in range(len(binw)):
            if binkey[i] == '1': x.append(binw[i])
            elif binkey[i] == '0': x.append('1' if binw[i] != '1' else '0')
        x = str(int(''.join(x), 2))
        if len(x)%2!=0: x = '0' + x
        return self.decipher_1(x)
