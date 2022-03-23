#!/usr/bin/env python3
import Caesar_Cipher

# Ընդհանուր առմամբ խնդիրն իրականացված է։
# Թերությունների մեծ մասը կապված են մուտքագրման ժամանակ, բացառիկ դեպքերը հաշվի չառնելու հետ։
# Վերոնշյալ թերություններից ոչ բոլորն եմ նշել։

while True:
    try:
        massage = input('Enter e clear massage: ')
        key = input('Make up your key 1 --> 25: ')
        try:
            int(key)
        except ValueError:
            print('You have to enter a number form 1 to 25')
            break
        else:
            knownkey = int(input('Enter your key --> '))
            decoding = Caesar_Cipher.decod(massage, int(key))
            encoding = Caesar_Cipher.encod(decoding, int(knownkey))
            if massage.lower() == encoding.lower():
                print(f'Decoded --> {decoding}, \nEncoded --> {encoding}')
            else:
                print('You entered incorect key')

        if int(key) > 25 or int(key) < 1:
            print('You can\'t enter less then 1 or more then 25')
            continue


    except KeyboardInterrupt:
        print('  Okay i\'m not gonna work if you want')
        break
    except EOFError:
        print('So why you closed me?')
        break



# decoded = Caesar_Cipher.decod(massage, key)
# print(Caesar_Cipher.decod(massage, key))
# print(Caesar_Cipher.encod(decoded, key))
