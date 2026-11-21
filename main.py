import demoji

'''

EMOJI_TO_TEXT

is a cli based python application used for various applications
like removing emoji from text ,replace emoji with description
,detect emojis in string


'''

text=input('Please enter a text ')




while True:
    print('______________________________________')
    print('1:Remove emoji from text ')
    print('2:Replace emoji with description ')
    print('3:Detect emojis in string ')
    print('4:Change the input text ')
    print('5:exit')
    print('______________________________________')

    try:
        choice=int(input('Please enter a choice (1-5)'))
    except ValueError as e:
        print(e)
    while choice >5 or choice<1 :
        choice=int(input('Enter your choice '))

    match choice:
        case 1:
            txt=demoji.replace(text,'')
            print(txt)
        case 2:
            txt=demoji.replace_with_desc(text)
            print(txt)
        case 3:
            txt=demoji.findall(text)
            print(txt)
        case 4:
            text=input('Change text that you want ')
        case 5:
            break

print('THANKS!!! FOR visiting our application 🙂')
