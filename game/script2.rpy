

label start:
    show fuyu sus
    
    e "..."

    e "Привет?"
    
    show fuyu nonsus
    
    e 'Ох, кажется, я вижу вас впервые.'
    
    $ name = renpy.input("Как вас зовут?", length=16).strip
    
    e '[name], какое замечательное имя!'

    scene bg street
    show fuyu offihappy
    
    a happy 'Меня зовут Фуюка, сегодня я представляю вам некоторые возможности доступные В.К. на данный момент.'
    
    a nonsushappy 'Для начала, стоит перейти в более комфортную обстановку.'
    
    scene bg room
    with fade
    
    show fuyu offihappy
    
    a 'Да, пока что фоны здесь всего-лишь обработанные фотографии, а спрайты нарисованы за 10 минут...'
    
    a offi "Однако всему своё время, Диана лишь только учится."

    a nonsus "О, может быть, вы хотите услышать какую-нибудь музыку?"
    
    menu:
    
        'Нет, спасибо':
        
                show fuyu nonsus
    
                a 'Хм?'
    
                show fuyu nonsushappy
    
                a 'Нет? Ха-ха, прости если прозвучит грубо, но у тебя всё равно нет выбора.'
         
        'Да, пожалуйста.':
             pass
    a offihappy "Замечательно!"
    
    a offi 'У меня не особо много выбора, так что я подключу на свой вкус.'
    
    play music relax 
    
    a happy 'Теперь, протестируем новые возможности.'
    
    show fuyu nonsushappy
    
    show fuyu at right
    with move
    
    a 'Как видишь, я умею не только стоять на месте, но и перемещаться по монитору'
    
    show fuyu offihappy at left
    with move
    
    a 'Здорово, не правда ли?'
    
    show fuyu happy at center
    with move
    
    a 'И ты даже представить себе не сможешь как сильно настрадалась Диана чтобы выдать мне такую возможность...'
    
    a pochtihappy 'так же, я могу выводить на экран картинки'
    
    show fuyu offihappy:
        xalign 0.8
    
    show sni:
        xalign 0.3 yalign 0.5

    a 'Смотри, это скриншот небольшого кусочка кода этой игры'
    
    hide sni
 
    show fuyu happy at default
    with move
    
    a 'по точно такому же принципу я могу приглашать к себе на экран ещё персонажей.'
    
    a pochtihappy 'однако это будет уже в следующих тестовых "демо" играх.'
    
    a offi 'На данный момент все самые базовые функции для создания уже хоть какой-то новеллы изучены, далее мы поработаем над концовками а так же интерфейсом'
    
    a happy 'На этом всё. Большое спасибо за внимание, удачи тебе и до скорых встреч!'
    
    stop music fadeout 1
    
   #obnova
   
    scene bg street
    
    show nova glo at opo1
   
    v 'какой прекрасный день'
    
    show fuyu offihappy at opo2

    a 'Это точно!'
    
    return