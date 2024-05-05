# The script of the game goes in this file.

init:
    transform flip:
        xzoom -1.0

    transform flipback:
        xzoom 1.0

    transform midleft:
        xalign 0.18
        yalign 1.0

    transform middle:
        xalign 0.5
        yalign 0.5

    transform upmiddle:
        xalign 0.5
        yalign 0.2

    transform midright:
        xalign 0.80
        yalign 1.0

    transform bigger:
        xzoom 1.5
        yzoom 1.5

    transform abitbigger:
        xzoom 1.25
        yzoom 1.25

    transform abitsmaller:
        xzoom 0.75
        yzoom 0.75

    transform forarrow:
        xalign 0.85
        yalign 0.9

    transform arroww:
        xzoom 0.25
        yzoom 0.25
        xalign 0.95
        yalign 0.9

    transform daleee:
        # xzoom 0.25
        # yzoom 0.25
        xalign 0.78
        yalign 0.95

init python:
    renpy.add_layer("arrowlayer", above="overlay") # this is a new function in 6.99.8 that allows us to add new layers in a much simpler manner

# image arrowpic = "images/arrow.png"

screen test():
    # image "images/arrow.png" at arroww
    image "images/dalee1.png" at daleee

define slowdissolve = Dissolve(3)
# init:
    # transform walk(start, end, tall):
    #     xpos start ypos 0 xanchor 0.5 yanchor 0
    #     linear 0.5 xpos end

# colors used to dim and shit
image dimmed = "#00000088" #hope this is half transparent (haven't tested)
image full_black = "#000000ff" #
image full_white = "#ffffffff" #

init python:
    class Colors:
        bap = ""
        fle = ""
        vi = ""
        pr = ""
        me = ""
        narrator = ""
        speech = ""

        def __init__(self):
            self.bap = "#FF8BAF"
            self.fle = "#FFB06A"
            self.vi = "#6A91FF"
            self.pr = "#8569A9"
            self.me = "#333333"
            self.narrator = "#386B8B"
            self.speech = "#333333"
            # self.me = "#2f8b58"

define col = Colors()

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define bap = Character("Бапуся", what_color=col.speech, color=col.bap)
define fle = Character("Флэшмобщик", what_color=col.speech, color=col.fle)
define vi = Character("/выебал/", what_color=col.speech, color=col.vi)
define pr = Character("Пронзатор", what_color=col.speech, color=col.pr)
define me = Character("", what_color=col.speech, color=col.me)
define narrator = Character(None, what_color=col.narrator, what_italic=True)

# The game starts here.
define e = Character("scolar", color="#F86983")
default question_tally = 0     
define colorlike = "ff"  


label start:
    label variables:
        # flags 
        $ vjb_flag = False

        # points
        $ bap_points = 0
        $ fle_points = 0
        $ vi_points = 0
        $ pr_points = 0
        $ me_points = 0

    python:
        _preferences.set_volume('music', 0.3)
        renpy.restart_interaction()

    
    label mainmenu:
        scene bg rainbow with pixellate  
        menu:
            "Вступление":
                jump beginning
            "Бедосяфон":
                jump bdsphone
            "Болталовка":
                jump talk
            "Тест":
                jump test


label beginning:
    play music seabird 
    scene full_white with pixellate
    show screen test(_layer="arrowlayer") # shows screen on layer bglayer
    $ renpy.show_screen("test", _layer="arrowlayer")
    # pause

    label first_dialogue:
        # show bg rainbow
        "…"
        "Что?"
        "…"
        "Что происходит?..."
        "..."
        "Я чувствую характерный соленый морской запах и пытаюсь разлепить глаза, но яркий свет неприятно меня слепит."
        "У меня жутко болит голова и попытки сконцентрироваться ни к чему не приводят."
        "Я накрываю лицо ладонью и пытаюсь сосредоточиться."
        "Кажется, вчера я пил? Или нет? Сложно сказать."
        "Я неуверенно открываю глаза и, прищурившись, жду, когда глаза привыкнут к свету."

        scene sky1 with slowdissolve

        "Я пытаюсь вспомнить хоть что-нибудь, но в голове абсолютная пустота. Ноль. Ничего." 
        "Я даже не помню ничего о себе."
        "Сперва это сильно меня пугает. Может быть меня огрели чем-нибудь по голове? Я спешно проверяю затылок, но следов травмы нет."
        "Нужно начать с чего-нибудь совсем простого. Например с имени. Да, точно. Начну с имени."

        $ temp_name = renpy.input("Как меня зовут?..", length=32, exclude=" 0123456789+=,.?!<>{{}[[]")
        $ temp_name = temp_name.strip()
        if temp_name == "":
            $ temp_name = "Я"

        $ me.name = temp_name
        # me "Ну, хорошо хоть имя свое не забыл. Больше ничего и не помню. А дальше-то что делать? (тут имя для примера, как будет выглядеть)"
        "Ну, хорошо хоть имя свое не забыл. Больше ничего и не помню. А дальше-то что делать?"
        "Я не спешу подниматься и бью себя по карманам. В них нет ни паспорта, ни водительских прав, совсем ничего. Хотя постойте…"
        "Кажется, в кармане куртки лежит телефон."

        jump bdsphone

    label afterphone:
        "Сколько бы я ни пытался его включить, он совсем не реагирует."
        me "Сломался что ли?"
        me "Так. Окей. Не будем отчаиваться."
        # pause
        hide phone with dissolve
        hide dimmed with dissolve
        "По крайней мере я могу попытаться выяснить, где я нахожусь. И, прямо как в \"Мальчишнике в Вегасе\", восстановить цепочку событий."

        scene dock1 with dissolve

        "Оказывается, я очнулся в корабельном порту. Вокруг ни души, а я никак не могу понять, как меня сюда занесло."
        "Судя по всему сейчас раннее утро. Я продолжаю осматриваться."
        me "Разве это не доска объявлений?"
        "Я щурюсь, пытаясь разглядеть доску получше, а затем поднимаюсь с земли и направляюсь к ней."

        me "Сейчас посмотрим, где я. Может, хотя бы так я что-нибудь вспомню."

        scene board1 with pixellate
        pause # 2.0

        me "Что тут у нас… Хмм. ВЖБ?"

        label vjb:
            menu:
                " {fast}"
                "Звучит достаточно интересно.":
                    me "Интересно хуесно"
                    $ vjb_flag = True
                "Просто какой-то бред":
                    me "Хуйня какая-то"
                    $ vjb_flag = False
            jump after_vjb

        label after_vjb:
            me "Что там дальше… Говняки, реклама какого-то культа. Жуть какая."
            me "Ищу девушку? Пошлую? Кто-то до сих пор ищет партнеров таким образом?"
            "Сколько бы я не пялился на эти объявления, все равно ничего непонятно, да и карты тут никакой нет."

        scene dock1 with pixellate

        "Я осматриваюсь вокруг себя в надежде, что в такую рань здесь окажется хоть кто-нибудь, но никого не вижу. Это тоже кажется мне странным, ведь обычно корабли прибывают очень рано."

        me "Ничего не понимаю. Тут будто нет никого."
        me "Ни души."
        me "Черт возьми."
        me "Да какого хрена вообще происходит!"
        me "Эй!!! Тут вообще есть кто-нибудь?!"
        me "ХОТЬ КТО-ТО?!"

        show fle shad at center with dissolve:
            abitbigger

        $ fle.name = "???"

        fle "Чего орешь?"
        fle "Стой-ка! Кажется, я раньше тебя не видел."

        "Я так сильно удивляюсь тому, что за спиной внезапно звучит чей-то голос, что нелепо от него шарахаюсь."

        fle "Тише-тише, приятель! Нечего так пугаться. Что ты тут забыл в такую рань? Или ты из сибирских?"
        me "Что? В каком смысле из сибирских?"  

        $ fle.name = "Флэшмобщик"

        fle "Ой, не бери в голову. Обычно местные зовут меня Флешмобщиком." 

        show fle w with dissolve:
            abitbigger

        "Флешмобщик крепит на доску объявлений какую-то бумажку, пока я все еще удивленно на него пялюсь."

    label glava1:
        show fle wcringe
        fle "Эй, чего так смотришь? Мы что, знакомы?"
        "Этот парень, Флешмобщик, выглядит неуверенно. Всматривается в мое лицо так, словно пытается вспомнить, где мог меня видеть."
        "Он чешет в затылке и робко улыбается. И это ему очень идёт."
        me "Может быть."
        fle "В смысле \"может быть\"? Ты и сам не знаешь?"
        me "Есть такое. Я понятия не имею, как тут оказался."
        "Кажется, он удивляется. Его можно понять."
        "Раннее утро, какой-то чел говорит, что он потерялся. Не каждый день случается что-то подобное.."
        show fle wopen
        fle "Ух ты. Может, ты вчера перебрал, дружище?"
        me "Может быть. А может и нет. Тоже не знаю."
        me "И где мы находимся – тоже."
        flew "Серьезно? Мы в порту города Флаймер!"
        show fle w
        fle "Это лучшее место в мире! Место, где найдётся кто угодно, готовый ответить на твои вопросы."
        fle "Тебе повезло, что ты попал сюда, а не в соседний город."
        me "Соседний город? Что с ним не так?"
        show fle wcringe
        fle "Ага, он в нескольких километрах отсюда. Поверь мне, это жуткое место."
        fle "Постоянные землетрясения…"
        fle "Сексуальные преступления…"
        fle "Драки!"
        fle "В общем, ты бы точно не хотел там оказаться."

        menu:
            me " {fast}"
            "Звучит круто.":
                me "А зачем тогда ты мне его рекламируешь?"
                $ fle_points -= 2
            "Да, ты прав, такое себе.":
                me "Повезло, что я попал сюда. И встретил тебя."
                $ fle_points += 2
        show fle w
        "Возникшая на его лице улыбка может затмить своим сиянием солнце."
        fle "Кстати, как тебя зовут?"
        "Точно. Я же не представился. Вот идиот."
        me "[me.name]."
        fle "А я Флешмобщик."
        "Он протягивает руку, и я замечаю на его запястье множество браслетов. Фенечек."
        menu:
            me " {fast}"
            "В первый раз был бета-тест?":
                # me "А зачем тогда ты мне его тогда рекламируешь?"
                $ fle_points += 3
            "Ты же уже представлялся.":
                # me "Повезло, что я попал сюда. И встретил тебя."
                $ fle_points -= 3
        fle "Ну да, а теперь мы знакомимся по-настоящему."
        show fle whappy
        "Надо же, он даже подмигивает чертовски задорно."
        "Я пожимаю его руку и не могу её отпустить."
        fle "Ого. У тебя белая горячка?"
        fle "Или ты всегда такой горячий?"
        "Я смущённо смеюсь, и мы разнимаем руки. Кажется, он тот ещё шутник."
        show fle w
        flew "Слушай, тебе повезло встретить именно меня, ведь я спасатель всех заблудших."
        me "А?"
        fle "Да шучу я. В общем, тебе лучше дойти до поста охраны."
        fle "Там работает такой смурной тип… Он мог что-нибудь видеть…"
        fle "А если он не поможет, то кто-нибудь из моих друзей точно сможет."
        show fle whappy
        "От его улыбки исходит такое тепло, что сразу становилось понятно –"
        "Этот парень не сделает ничего плохого."
        "Он и правда спасает заблудшие души вроде моей."
        fle "Слушай, me_name, больно было падать?"
        me "А? Откуда?"
        fle "С небес. Ты же ангел, раз из ниоткуда тут без памяти оказался."
        menu:
            " {fast}"
            "Рассмеяться":
                "Я смеюсь. Он, видимо, рассчитывал на такую реакцию. Он выглядит как неплохой парень."
                $ fle_points += 1
            "Нахмуриться":
                "Шутка звучит так себе, если честно, так что я просто вежливо киваю. Кажется, он расстроен такой реакцией."
                $ fle_points -= 1
        show fle w 
        fle "А ты так хочешь знать, кем ты был раньше?"
        me "Это было бы неплохо, правда? Ну, знать кто ты такой."
        fle "Или тебе выпал огромный шанс."
        me "Какой шанс?"
        fle "Сочинить свою историю заново. Люди обычно сюда за этим приходят."
        fle "Стать кем-то, кем ты раньше не был."
        fle "Или кем ты никогда не мог бы стать."
        "Яркое утреннее солнце слепит меня. Морской воздух и крики чаек пьянят. Этот парень…"
        "В его словах что-то есть."
        menu:
            me " {fast}"
            "Нет, знаешь, я бы всё равно хотел знать, кто я":
                "Если я и захочу кем-то притворяться, я все равно должен знать, от чего отказываюсь."
                $ fle_points -= 5
            "Думаю, в твоих словах есть логика":
                "Начать жизнь с абсолютно чистого листа — не каждый раз выпадает такой шанс"
                $ fle_points += 5
        fle "Может ты и прав."
        fle "В любом случае, если тебе будет нужна помощь, зови – и я сразу появлюсь."
        me "Как Сяо из Геншина?"
        show fle whappy
        "Он смеётся, и от этого мне становится тепло на сердце."
        fle "Посмотрите-ка, а Геншин ты помнишь."
        fle "Если решишь остаться здесь, точно сойдёшь за своего."
        show fle w
        label test:
        fle "Слушай, а какой цвет тебе больше нравится?"
        $ temp_name = renpy.input(fle, "Слушай, а какой цвет тебе больше нравится?", length=50, exclude=" 0123456789+=,.?!<>{{}[[]")
        fle "Окей, [temp_name]"











    jump end


label bdsphone:
    # scene dock1 with pixellate  

    pause 1
    show dimmed with dissolve
    pause 0.5
    show phone at upmiddle with dissolve:
        abitbigger

    $ bds_counter = 0

    me "Что это за знак такой?"

    label bdsturnon:
        menu:
            " {fast}"
            "Попробовать включить телефон":
                play sound "audio/meow.mp3"
                if renpy.random.choice((1, 2, 3)) == 3:
                # hide phone
                    $ bds_counter += 1
                    show phone angry at upmiddle:
                        abitbigger
                    pause 1.0
                    # show full_black with dissolve

                    # stop sound fadeout 1.5
                    pause 1.5
                    show phone at upmiddle with dissolve:
                        abitbigger
                    if bds_counter >= 2:
                        jump bdsturnoff
                    else:
                        jump bdsturnon
                else:
                    jump bdsturnon
        jump afterphone

    label bdsturnoff:
        menu:
            " {fast}"
            "Попробовать включить телефон":
                play sound "audio/meow.mp3"
                if renpy.random.choice((1, 2, 3)) == 3:
                # hide phone
                    $ bds_counter += 1
                    show phone angry at upmiddle:
                        abitbigger
                    pause 1.0
                    # show full_black with dissolve

                    # stop music fadeout 1.5
                    pause 1.5
                    show phone at upmiddle:
                        abitbigger
                    jump bdsturnoff
                else:
                    jump bdsturnoff
            "...":
                # "bdsya" "Слабак (ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ)" with de
                jump afterphone
                
        jump afterphone
                
# label bdsphone:
#     # scene dock1 with pixellate  

#     pause 1
#     show dimmed with dissolve
#     pause 0.5
#     show phone at upmiddle with dissolve:
#         abitbigger

#     $ bds_counter = 0

#     me "Что это за знак такой?"

#     label bdsturnon:
#         menu:
#             " {fast}"
#             "Попробовать включить телефон":
#                 play sound "audio/fart.mp3"
#                 if renpy.random.choice((1, 2, 3)) == 3:
#                 # hide phone
#                     $ bds_counter += 1
#                     show phone angry at upmiddle:
#                         abitbigger
#                     pause 1.0
#                     # show full_black with dissolve

#                     # stop sound fadeout 1.5
#                     pause 1.5
#                     show phone at upmiddle with dissolve:
#                         abitbigger
#                     if bds_counter >= 2:
#                         jump bdsturnoff
#                     else:
#                         jump bdsturnon
#                 else:
#                     jump bdsturnon
#         jump afterphone

#     label bdsturnoff:
#         menu:
#             " {fast}"
#             "Попробовать включить телефон":
#                 play sound "audio/fart.mp3"
#                 if renpy.random.choice((1, 2, 3)) == 3:
#                 # hide phone
#                     $ bds_counter += 1
#                     show phone angry at upmiddle:
#                         abitbigger
#                     pause 1.0
#                     # show full_black with dissolve

#                     # stop music fadeout 1.5
#                     pause 1.5
#                     show phone at upmiddle:
#                         abitbigger
#                     jump bdsturnoff
#                 else:
#                     jump bdsturnoff
#             "...":
#                 # "bdsya" "Слабак (ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ)" with de
#                 jump afterphone
                
#         jump afterphone


label talk:
    scene dock1
    show bap at midright
    show fle at midleft:
        flip

    # These display lines of dialogue.

    "/типа общаются/"

    fle "Bye Bapusya"

    bap "{i}Oh.{/i} B-Bye..."
    
    hide fle
    
    bap "{i}/sighs/{/i} He left... \nShould I go too?"

    label the_question: 
        e "Should I {i}leave{/i} or should I {i}stay{/i}?"
        call question_selector
        show bap at left with move:
            flip

        menu:
            "Stay":           
                show bap at midleft with move  #SCREEN 4-1
                bap "{i}/sighs/{/i} Okay, maybe I should wait..."
                call ebir_comes
            "Leave":
                show bap at left with ease:  #SCREEN 4-1
                    flipback
                bap "Yeah, I guess I'll leave..."
                show bap at offscreenleft with ease
                hide bap 
                # bap "{b}Yeah{/b}, because I am... {color=#808080}always... {size=-5}sleepy...{/size}{/color}"
            "[repeat_question] Could you repeat the question?":
                jump the_question
        jump end

    label ebir_comes:
        show vi at midright
        vi "Hey there. I'm Vi, short for Viebal. Are you alone here?"
        show bap at left with move
        show vi at right with move
        menu:
            "Yeah, I am. My name is Bapusya, nice to meet you, Vi.":           
                show bap happy at midleft with move
                show vi at midright with move
                bap "Yeah, I am. My name is Bapusya, nice to meet you, Vi."
                show vi smirk at midright
                vi "Nice to meet you, Bapusya."
                show 18 at middle 
            "{i}/shrugs/{/i} I'm waiting for someone, sorry.":
                show bap at left with ease:  #SCREEN 4-1
                    flipback
                bap "{i}/shrugs/{/i} I'm waiting for someone, sorry."
                vi "Oh, okay."
                hide bap 
                vi "{i}¯\_(-.-)_/¯{/i} Better luck next time."
        jump end


label question_selector:
    $ NumberGenerator = renpy.random.randint(1, 3)
    if NumberGenerator == 3:
        $ repeat_question = "What?"
    elif NumberGenerator >= 2 and NumberGenerator < 3 or NumberGenerator == 5:
        $ repeat_question = "Say that again?"
    else:
        $ repeat_question = "Huh?"
    # $ repeat_question = renpy.random.choice(["What?", "Say that again?", "Huh?"])
    $ question_tally += 1
    return

label end:
    "The End!"
    return
