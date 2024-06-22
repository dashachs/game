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

    transform downmiddle:
        xalign 0.5
        yalign 0.7

    transform flepocket:
        xalign 0.55
        yalign 0.7

    transform mypocket:
        xalign 0.15
        yalign 1.5

    transform midright:
        xalign 0.78
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
    renpy.add_layer("pinlayer", above="arrowlayer") # this is a new function in 6.99.8 that allows us to add new layers in a much simpler manner

# image arrowpic = "images/arrow.png"

screen test():
    # image "images/arrow.png" at arroww
    image "images/dalee1.png" at daleee

screen test1():
    # image "images/arrow.png" at arroww
    image "images/items/pin.png" at upmiddle

define slowdissolve = Dissolve(3)

# colors used to dim and shit
image dimmed = "#00000088" #hope this is half transparent (haven't tested)
image full_black = "#000000ff" #
image full_white = "#ffffffff" #

define premium = False

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
define fle = Character("Флешмобщик", what_color=col.speech, color=col.fle)
define vi = Character("/выебал/", what_color=col.speech, color=col.vi)
define pr = Character("Пронзатор", what_color=col.speech, color=col.pr)
define me = Character("ГГ", what_color=col.speech, color=col.me)
define narrator = Character(None, what_color=col.narrator, what_italic=True)

# Images of vi


# The game starts here.
define e = Character("scolar", color="#F86983")
default question_tally = 0   
define good_colors = ["красный", "оранжевый", "желтый", "жёлтый", "зеленый", "лиловый", "розовый"]
define bad_colors = ["синий", "фиолетовый", "серый", "чёрный", "черный"]
define smartass_answers = ['пенис', 'хуй', 'залупа', 'жопа', 'попа', 'очко', 'анус', 'анал', 'пенис', 'сиськи', 'письки', 'писька', 'сиська', 'титьки', 'титька', 'перчик', 'пизда', 'пусси', 'киска', 'снежинка', 'пизда' 'вагина', 'влагалище', 'вульва', 'пещерка', 'пирожок', 'вареник']
define typo_colors = ["краснвй"]

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

    # Меню для перескакивания на тестовые кейсы
    label mainmenu:
        scene bg rainbow with pixellate  
        menu:
            "Вступление":
                jump beginning
            "Ви":
                jump viee
            "Test":
                jump testik
    #         "Бедосяфон":
    #             jump bdsphone
    #         "Болталовка":
    #             jump talk
    #         "Тест":
    #             jump test
    #         "Цвета":
    #             jump colorgrade


label beginning:
    play music seabird 
    scene full_white with pixellate
    show screen test(_layer="arrowlayer") # shows screen on layer bglayer
    $ renpy.show_screen("test", _layer="arrowlayer")
    # show screen test1(_layer="pinlayer") # shows screen on layer bglayer
    # $ renpy.show_screen("test1", _layer="pinlayer")
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

        $ whats_my_name = "Как меня зовут?.."
        label name:
            $ temp_name = renpy.input(whats_my_name, length=32, exclude="0123456789+=,.?!<>{{}[[]")
            $ temp_name = temp_name.strip()
            if temp_name == "":
                $ temp_name = "Я"
            if temp_name.lower() == "коля":
                $ whats_my_name = "Да нет, не Коля... Э-э-э, меня звали..." 
                jump name
            if temp_name.lower() in smartass_answers:
                "Родители, конечно, молодцы..."

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
                    $ vjb_flag = True
                "Просто какой-то бред":
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

        $ fle.name = "Флешмобщик"

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
        fle "Серьезно? Мы в порту города Флаймер!"
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
                $ fle_points += 3
            "Ты же уже представлялся.":
                $ fle_points -= 3
        fle "Ну да, а теперь мы знакомимся по-настоящему."
        show fle whappy
        "Надо же, он даже подмигивает чертовски задорно."
        "Я пожимаю его руку и не могу её отпустить."
        fle "Ого. У тебя белая горячка?"
        fle "Или ты всегда такой горячий?"
        "Я смущённо смеюсь, и мы разнимаем руки. Кажется, он тот ещё шутник."
        show fle w
        fle "Слушай, тебе повезло встретить именно меня, ведь я спасатель всех заблудших."
        me "А?"
        fle "Да шучу я. В общем, тебе лучше дойти до поста охраны."
        fle "Там работает такой смурной тип… Он мог что-нибудь видеть…"
        fle "А если он не поможет, то кто-нибудь из моих друзей точно сможет."
        show fle whappy
        "От его улыбки исходит такое тепло, что сразу становилось понятно –"
        "Этот парень не сделает ничего плохого."
        "Он и правда спасает заблудшие души вроде моей."
        fle "Слушай, [me.name], больно было падать?"
        me "А? Откуда?"
        fle "С небес. Ты же ангел, раз из ниоткуда тут без памяти оказался."
        menu:
            " {fast}"
            "/рассмеяться/":
                "Я смеюсь. Он, видимо, рассчитывал на такую реакцию. Он выглядит как неплохой парень."
                $ fle_points += 1
            "/нахмуриться/":
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
            
        label colorgrade:
            $ temp_name = renpy.input([fle.name, col.fle, "Слушай, а какой цвет тебе больше нравится?"], screen="myinput")
            $ temp_name = temp_name.strip().lower()
            if temp_name in good_colors:
                $ fle_points += 1
                fle "О, мне тоже нравится!"
            elif temp_name in bad_colors:
                $ fle_points -= 1
                fle "Эх, а мне не очень нравится."
            elif "нефрит" in temp_name:
                fle "Я тоже люблю цвет нефрита."
            elif temp_name in smartass_answers:
                fle "Я тоже люблю бежевый."
            elif temp_name in typo_colors:
                "[temp_name.capitalize()]? Заикаешься что ли?"
            
        # fle "Окей, [temp_name]"
        label catordog:
            fle "А что насчет животных? Ты был бы котом или собакой?"
            menu: 
                me " {fast}"
                "Котом":
                    $ fle_points += 1
                "Собакой":
                    $ fle_points -= 1
        me "А к чему все эти вопросы? Будет какой-то результат? Кто я из Магической Битвы, например?"
        fle "Результат? Да нет, мне просто хотелось узнать тебя лучше." 
        me "Тогда что насчет тебя? Расскажешь о себе что-нибудь?"
        fle "Что-нибудь о себе? Ну, например, я диджей на Flymer FM. Если у тебя есть любимые треки, я могу их поставить."
        me "Я бы скинул, но мой телефон сдох." 
        fle "Ничего страшного, мы сможем обменяться контактами позже. Или просто свяжись со мной во время радиоэфира."
        me "Договорились."
        me "Ну так что, отведешь меня к тому посту охраны?"
        menu:
            "Без лишних слов он берет меня за руку.{fast}"
            "/крепче сжать его руку/":
                $ fle_points += 4
            "/одернуть руку/":
                $ fle_points -= 4
        hide fle with dissolve

        scene guards1 with pixellate
        pause
        "Вдали маячит синий пост охраны и шлагбаум."
        "Если память не врёт, я видел таких за всю жизнь сотню."
        "Мы с Флешмобщиком останавливаемся неподалёку."
        show fle w at center with dissolve:
            abitbigger

        fle "Здесь наши пути разойдутся."
        "Он уже готовится уйти, как вдруг оборачивается и широко улыбается."
        show fle whappy
        fle "Но не навсегда."
        fle "Вечером у Барби в баре будет вечеринка."
        fle "Кен всех приглашал. Думаю, Барби не будет против, если придёт кто-то новенький."
        fle "Залетай, если до того времени не найдёшь себя, [me.name]."
        show fle w
        fle "Ах, да, кстати."
        "Он роется в карманах, словно пытается там что-то найти, затем он достает из кармана значок."
        
        pause 1
        show dimmed with dissolve
        show pin with dissolve:
            subpixel True
            flepocket zoom 0.5
            ease 1.5 upmiddle zoom 1.5

        me "Это мне? Спасибо."
        "Я неуверенно забираю значок себе и прячу его в карман."
        # show screen test1(_layer="pinlayer") # shows screen on layer bglayer
        # $ renpy.show_screen("test1", _layer="pinlayer")
        show pin with dissolve:
            # subpixel True
            upmiddle 
            ease 1.5 mypocket zoom 0.3
        hide dimmed with dissolve
        # hide pin
        fle "Да, тебе. Я словно знал, что встречу сегодня кого-то особенного. Может быть мы с тобой настоящие соулмейты, а?"
        fle "Ну, увидимся!"
        "Он очень быстро уходит, словно не хочет сталкиваться с тем, кто может сидеть в этой будке.."
        # show fle w at offscreenleft with ease
        hide fle with dissolve
        "Отчего-то мне становится тревожно. Я откашливаюсь в кулак и собираюсь постучать в дверь, как вдруг она внезапно открывается сама, а на пороге возникает…"

        # define premium = "vi"
        label viee:
            default p = "" if premium else "p"
            image vi = "images/vi/vi [p].png"
            image vi angry = "images/vi/vi [p]angry.png"
            image vi cringe = "images/vi/vi [p]cringe.png"
            image vi horny = "images/vi/vi [p]horny.png"
            image vi shadow = "images/vi/vi [p]shadow.png"
            image vi wow = "images/vi/vi [p]wow.png"
            scene guards2 with dissolve 
            show vi shadow at center with dissolve:
                abitbigger
            "На пороге возникает мужская грудь."
            "Я теряюсь и после пары секунд поднимаю голову, чтобы увидеть лицо мужчины."
            "Но, кажется, он большой фанат анонимности. Слишком большой."
            show vi with dissolve
            me "Здравствуйте…"
            vi "..."
            me "Доброе… э-э-э… утро?"
            vi "..."
            "Я всё так же стою на пороге, пока он загораживает мне проход."
            "Он такой широкий, что в одиночку может встать вместо двери." 
            me "Я…"
            vi "заходи."
            "Он отходит, и я наконец вхожу внутрь небольшой будки охраны."
            "Хоть она казалась крошечной снаружи, внутри она вся украшена."
            "Плакат с вертолётом, фигурка из \"Клинка, рассекающего демонов\", какой-то цветок. "
            menu:
                me "{fast}"
                "Да у тебя тут настоящая ТАРДИС!":
                    $ vi_points += 3
                "Ну и свалка. Понятно, чего ты такой молчаливый.":
                    $ vi_points -= 3
            "Он указывает на обычный офисный стул, и я сажусь. Ноги не устали, но отдохнуть всё равно хочется."
            vi "так кто ты такой?"
            me "Я здесь как раз за этим."
            vi "..."
            me "Я потерялся. Только имя своё знаю."
            vi "..."
            vi "как тебя зовут?"
            me "[me.name]."
            me "Не слышали раньше?"
            vi "нет. видимо, ты тут новенький."
            me "Мне Флешмобщик так же сказал."
            vi "..."
            "Хоть я и не вижу его лица, но уверен, что слышу усмешку. Мне кажется, или эти двое приятели?"
            vi "это он тебя сюда привёл, потеряшка?"
            "Кажется, даже его голос звучит теплее. Видимо, у них действительно хорошие отношения."
            "Я киваю. Он отходит от стола, что-то берёт и протягивает мне."

            # [Фон затемняется, посередине появляется визитка]
            pause 1
            show dimmed with dissolve
            pause 0.5
            show card at upmiddle with dissolve:
                abitbigger
            
            menu:
                me "{fast}"
                "Э-э-э… Это что ещё такое?":
                    $ vi_points -= 4
                "Спасибо.":
                    $ vi_points += 4
                "Зачем мне визитка?":
                    $ vi_points += 0

            vi "я тебе сейчас точно не помогу, но когда понадобится помощь, найди меня. я глава этого клуба."
            "Он кивает в сторону визитки."
            menu:
                "Так ЭТО – название клуба?{fast}"
                "Оригинально, мда уж…":
                    $ vi_points -= 3
                "Хоть и нелюдимый, но вроде весёлый?":
                    $ vi_points += 3
            hide card with dissolve
            hide dimmed with dissolve
            vi "эй, что молчишь?"
            "Надо что-то сказать, чтобы не казаться слишком странным, чёрт!"
            menu:
                me "{fast}"
                # "Надо что-то сказать, чтобы не казаться слишком странным, чёрт!{fast}"
                "Да ты ерунду какую-то несёшь.":
                    $ vi_points -= 4
                "Задумался. Спасибо, что беспокоишься.":
                    $ vi_points += 4
            "В ответ он только кивает."
            "Пусть он мало говорит, но кажется надежным парнем."
            "Одно только его присутствие дарит мне спокойствие. В моих обстоятельствах это ощущается почти спасением."
            "Если бы я только мог отплатить ему чем-то, кроме моей компании…"
            "Но увы."
            me "У тебя здесь столько всего. Расскажешь обо всём?"
            vi "неужели тебе правда интересно слушать про гиперфиксы какого-то парня, которого ты впервые видишь?"
            label testik:
            menu:
                me "{fast}" 
                "Я просто хочу узнать об этом месте побольше.":
                    $ vi_points -= 1
                "Почему бы и нет? Мне правда интересно.":
                    $ vi_points += 1
            vi "хорошо."
            # label testik:
            # scene guards2
            # show vi at center with dissolve:
            #     abitbigger
            "Он придвигает к себе стул, разворачивает ко мне спинкой и, широко раскинув ноги, опускается на сидение."
            "Локти он укладывает на спинку."
            vi "ну давай, спрашивай."
            me "Расскажи про…"
            window hide
            show vi at midright with ease

            menu (screen='choice_story'):
                # me "Расскажи про…{fast}"
                "Гобелен с вертолётом!":
                    $ vi_points += 1
                "Листовку с мышами.":
                    $ vi_points += 1
                "Бог-тян с кружки.":
                    $ vi_points += 1
                "Плакат с пропавшим.":
                    $ vi_points += 2
                "Растение, я не знаю.":
                    $ vi_points -= 1
            "(Бла-бла-бла, тут объяснения; за плакат с Гопарём +2, потому что его надо было заметить раньше, значит, мы внимательные)"
            "Кажется, я слышу теплоту, когда он рассказывает об этом."
            "Видимо, этот парень действительно нашел здесь свое место, и это как-то вдохновляет."
            show vi at center with ease
            vi "слушай…"
            "Я не вижу лица, но слышу, как меняется голос. Становится тише. Приходится прислушаться, чтобы услышать."
            "Наверняка этот парень покраснел, когда говорил."
            show vi horny 
            vi "твоя заинтересованность мне очень нравится. и с тобой очень приятно даже тратить время на болтовню."
            vi "если бы я мог, я бы тебя не отпустил, но…"
            menu:
                "Что?!{fast}"
                "/Возмутиться/":
                    $ vi_points -= 5
                "/Смутиться/":
                    $ vi_points += 1
                "/ВОЗБУДИТЬСЯ/":
                    $ vi_points += 5
            show vi

            vi "но у меня сейчас уже заканчивается смена, а потом треня."
            vi "нет, ты можешь пойти со мной, но…"
            vi "кажется, заглянуть в бюро находок тебе важнее."
            me "Что за Бюро находок?"
            vi "там можно найти кого или что угодно."
            me "О, как на доске в доках?"
            "Он смеётся! Я смог его рассмешить! И его смех мне очень нравится."
            "Но стоп! Чем я его насмешил?"
            vi "нет."
            vi "бюро находок действительно работает."
            "Нужно идти. Но его смех и энергетика завораживают меня."
            vi "иди. мы ещё обязательно встретимся."
            me "Удачи."
            scene guards1 with fade
            "Я выхожу из небольшой кабинки. Что ж, мне предстоит найти себя в Бюро находок."

            
            












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
        if bds_counter < 5:
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
        else:
            menu:
                "Неужели?.. {fast}"
                "Попробовать в последний раз":
                    play sound "audio/meow.mp3"
                    show phone angry at upmiddle:
                        abitbigger
                    pause 2.0    
                    jump afterphone
                
        jump afterphone

label musor:

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
    jump end


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
        vi "Hey there. I'm Vi, short for viee. Are you alone here?"
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
