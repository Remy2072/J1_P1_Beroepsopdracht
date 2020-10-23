import os
import sys
from time import sleep

print("\nHet verhaal van een nieuwkomer in Nederland.\n")

def Deel1():
    tekst = """\
    DEEL 1\n
    Jij en Adam wonen in de Turkse stad Istanbul, maar sinds er een nieuwe leider is van het land zijn er veel problemen. 
    De nieuwe leider Furkan maakt ruzie met andere landen, en er komt een burgeroorlog. 
    De Turkse inwoners gaan tegen de staat en Furkan in. 
    Nu moeten jij en Adam een keuze maken laten jullie je familie achter en vluchten jullie naar een veiliger gedeelte van Turkije, 
    of blijf je in je thuis stad en gaan jullie mee de burgeroorlog in.
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Je verlaat je familie en Istanbul en gaat naar Ankara.")                      #! Ga naar Deel 2
    print("2: Je blijft in Istanbul met Adam en je gaat de burgeroorlog in.")               #! Ga naar Deel 3
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel2()
            incorrect = False
        elif vraag == '2':
            Deel3()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel2():
    tekst = """\n
    DEEL 2\n
    Je bent dus gevlucht met Adam. 
    Je bent verdrietig dat je je familie hebt achtergelaten je hoopt het beste voor ze. 
    Omdat de oorlog zo heftig wordt in het land, en andere landen beginnen zich er mee te bemoeien zijn jullie ook niet meer veilig in Ankara. 
    De regering rekruteert alle Turkse mannen die 18+ zijn en kunnen vechten. 
    Jij en adam hebben nu nog maar 2 keuzes voor zich, of ze zoeken een smokkelaar die ze kan smokkelen naar West- Europa. 
    Of jullie kiezen ervoor om de rebellen te helpen en deze dictatuur stop te zetten.
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Jullie zoeken een smokkelaar die jullie brengt naar West-Europa.")              #! Ga naar Deel 4
    print("2: Jullie sluiten jullie aan bij de rebellen.")                                    #! Ga naar Deel 5
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel4()
            incorrect = False
        elif vraag == '2':
            Deel5()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel3():
    tekst = """\n
    DEEL 3\n
    Je hebt dus besloten om te blijven in Istanbul, het is een chaos de stad en de stad is verdeeld in meerdere delen. 
    De ene kant is van de rebellen en de andere kant is van de Regering. 
    Beide partijen patrouilleren in hun gebied. 
    Nu is de keus voor welke kant ga jij vechten en waarom. 
    De Turkse regering biedt jou familie veiligheid en als het over is een goed leven.
    terwijl de rebellen zeggen dat ze je vrijheid aanbieden en dat er een democratie komt als ze winnen. 
    Dit vinden jullie een lastige keus, wat kies jij?
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Je sluit je aan bij de regering en zorgt dat je familie veilig is.")             #! Ga naar Deel 6
    print("2: Je sluit je aan bij de rebellen en zorgt dat er een democratie komt.")           #! Ga naar Deel 7
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel6()
            incorrect = False
        elif vraag == '2':
            Deel7()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel4():
    tekst = """\n
    DEEL 4\n
    Jullie gaan dus opzoek naar een smokkelaar om naar West-Europa te gaan. 
    Na 1 week zoeken heeft Adam er een gevonden. 
    Adam zegt de smokkelaar wil negentigduizend Turkse lira dat is ongeveer tienduizend euro, 
    en dan maakt hij een nep paspoort voor ons, en neemt ons mee met een bus naar Nederland. 
    Maar zo veel geld hadden wij natuurlijk niet dus Adam vroeg aan de smokkelaar als jij wapens voor ons regelt doen wij een bank overval, 
    op de bank van Ankara en krijg je honderdduizend Turkse lira. 
    De smokkelaar vond dat een goed idee maar hij gaf ook een andere suggestie hij brengt jullie naar Nederland en jullie betalen hem in termijnen twintigduizend euro. 
    Nu moet je de keuzen maken ga jij een bankoverval plegen of ga je in de dikke schulden komen als je misschien aan komt in Nederland.
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Bankoverval plegen op de bank van Ankara.")                                       #! Ga naar Deel 8
    print("2: In de schulden komen.")                                                           #! Ga naar Deel 9
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel8()
            incorrect = False
        elif vraag == '2':
            Deel9()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel5():
    tekst = """\n
    DEEL 5\n
    Jullie hebben ervoor gekozen om de rebellen te helpen. 
    Jullie waren nu officieel aan het vechten tegen de staat, maar er kwam slecht nieuws de bondgenoten van Turkije waren aangekomen in Ankara. 
    Het was een heftig gevecht maar uiteindelijk hadden de rebellen verloren Adam werd geëxecuteerd,
    en jij moest voor 40 jaar naar de gevangenis en werd gezien als een terrorist.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)
            os.system("clear")
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel6():
    tekst = """\n
    DEEL 6\n
    Jullie hebben je dus aan gesloten bij het Turkse leger en jullie vechten al maanden tegen de rebellen. 
    Maar een paar soldaten vertrouwen Adam niet en ze denken dat hij een infiltrant is van de rebellen, 
    hij moet op verhoor komen en wordt in de gaten gehouden door de soldaten. 
    Jij doet veel goede voor het leger en wordt al snel een hoge rang in het leger en krijgt respect van de soldaten. 
    Enkele maanden verder is er chaos op de legerbasis een groep soldaten valt Adam aan en neemt hem mee naar de Generaal. 
    Jij ziet dit gebeuren en rent er achteraan. 
    Er wordt nu een openbaar verhoor gehouden en de generaal stelt jij een vraag vertrouw jij Adam dat hij geen infiltrant is of is hij het wel?
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Adam is een infiltrant. ")                                                        #! Ga naar Deel 10
    print("2: Adam is geen infiltrant.")                                                        #! Ga naar Deel 11
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel10()
            incorrect = False
        elif vraag == '2':
            Deel11()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel7():
    tekst = """\n
    DEEL 7\n
    Je hebt je aangesloten bij de rebellen.
    jij en Adam worden gelijk aan het werk gezet jullie moeten met een groep van vijftig man het winkelcentrum overnemen. 
    Het was een sneak attack en alles liep volgens plan totdat je 1 man tegen kwam en je moest hem vermoorden maar dat had je nog nooit gedaan. 
    Je vond het doodeng en je zat te twijfelen of je het wel moest doen of dat je hem spaarde.
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Je schiet hem dood ")                                                             #! Ga naar Deel 12
    print("2: Je laat hem leven")                                                               #! Ga naar Deel 13
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel12()
            incorrect = False
        elif vraag == '2':
            Deel13()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")
        
def Deel8():
    tekst = """\n
    DEEL 8\n
    Jij en Adam kiezen ervoor om en bankoverval te plegen je bent het er eigenlijk niet mee eens maar je hebt nu niet veel keus. 
    Jullie moesten een plan kiezen er waren er twee. 
    Het eerste plan was om naar binnen te stormen het juiste bedrag te eisen en weg gaan. 
    De 2e optie was een transport truck overvallen het geld eruit halen en in een busje weg rijden.
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Je overvalt de bank.")                                                            #! Ga naar Deel 14
    print("2: Je overvalt een transport wagen.")                                                #! Ga naar Deel 15
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel14()
            incorrect = False
        elif vraag == '2':
            Deel15()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel9():
    tekst = """\n
    DEEL 9\n
    Jullie kiezen er dus voor om in de schulden te komen. 
    Adam vindt dit geen prettig plan omdat hij juist een rustig nieuw leven wil opbouwen in Nederland, 
    en niet in armoede moest leven wat hij in Istanbul had. 
     Jij vond het niet zo erg je wilde liever geld verdienen uit de schulden komen en later met een groot potje terug naar Turkije als het weer veilig is. 
     De smokkelaar haalde ons midden in de nacht op hij wilde zijn naam nog steeds niet vertellen en zei dat ze achter in de bus moesten zitten. 
     Na lange nacht rijden zonder enige plaspauze of even frisse lucht te halen mochten we er eindelijk uit. 
     Daar stond een andere man met 2 jongeren die ook gingen vluchten. 
    De smokkelaars waren aan het overleggen en ze vroegen aan ons vinden jullie het erg als je achterin zit met ze 4e?,
    of willen jullie dat liever niet.
     """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Wij vinden het niet erg ze kunnen mee.")                                          #! Ga naar Deel 16
    print("2: Liever niet het is te riskant.")                                                  #! Ga naar Deel 17
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel16()
            incorrect = False
        elif vraag == '2':
            Deel17()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel10(): 
    tekst = """\n
    DEEL 10\n
    Adam was verbaasd dat jij zijn beste vriend niet zijn kant koos en zei dit had ik niet van jou verwacht. 
    Maar Adam zei dat hij bij de rebellen hoorde. 
    Jij was in Schock je was boos maar Adam zei kijk waar je voor kiest een dictatuur dit moet stoppen we moeten vluchten. 
    Jij kon hier maar twee dingen op bedenken. 
    Je laat Adam vrij en dan komt een groep rebellen vechten bij de militaire basis en ze weten alles, of je brengt adam naar de gevangenis.
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("\nKies 1 of 2")
    print("1: Je laat hem ontsnappen. ")                                                        #! Ga naar Deel 18
    print("2: Je brengt hem naar de gevangenis.")                                               #! Ga naar Deel 19
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel18()
            incorrect = False
        elif vraag == '2':
            Deel19()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")
        
def Deel11():
    tekst = """\n
    DEEL 11\n
    Adam heeft zich bewezen dat hij te vertrouwen is. 
    Toen kwamen de rebellen jij werd beschoten op je arm. 
    Jij en adam werden daar weg gehaald door het Russische leger. 
    Jullie kregen van de Turkse staat een visum om naar Rusland te gaan, om geopereerd te worden. 
    Eenmaal in Rusland was zijn arm geopereerd maar was er wel een stuk vlees van af. 
    Hij hoefde niet meer te vechten van de generaal en mocht naar Antalya om uit te rusten. 
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)           
            os.system("clear")
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel12(): 
    tekst = """\n
    DEEL 12\n
    Je shiet mis uit stress de man ontsnapt en vraagt om assistentie. 
    Jullie worden opgepakt en in de gevangenis gezet voor terrorisme de straf is 40jaar.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")            
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")           
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel13():
    tekst = """\n
    DEEL 13\n
    Je laat hem leven hij vlucht en roept versteking jullie worden opgepakt door het leger, 
    en gaan naar de gevangenis voor terrorisme de straf is 40jaar.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            Deel1()
            os.system("clear")            
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel14():
    tekst = """\n
    DEEL 14\n
    Je bent nu in de bank met adam je zegt tegen de mevrouw bij de bank dat ze het geld in deze tas moet stoppen. 
    Maar de politie staat voor de deur wat nu?
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\nKies 1 of 2")
    print("1: Geven jullie je over.")                                                           #! Ga naar Deel 20
    print("2: Jullie gaan vluchten. ")                                                          #! Ga naar Deel 21
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == '1':
            Deel20()
            incorrect = False
        elif vraag == '2':
            Deel21()
            incorrect = False
        else:
            print("voer 1 of 2 in.")
            vraag=input("Typ je antwoord >")

def Deel15():
    tekst = """\n
    DEEL 15\n
    Jullie zijn nu in een tunnel van een auto weg.
    De transpoort wagen komt eraan jullie nemen het voertuig over. 
    Maar er was undercover politie auto bij ze houden jullie aan en jullie moeten naar de gevangenis.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            Deel1()
            os.system("clear")            
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel16():
    tekst = """\n
    DEEL 16\n
    Jullie namen de andere vluchtelingen mee en gingen heel Europa door. 
    Van Turkije naar Bulgarije van Bulgarije naar Servië van Servië naar Hongarije van Hongarije naar Oosterwijk van Oosterijk naar Duitsland
    en van Duitsland werden jullie achtergelaten in Nederland om precies te zijn in Amsterdam. 
    De smokkelaars gingen razendsnel weg en lieten jullie achter met een map van Amsterdam. 
    Jullie gingen naar het gemeentehuis en kregen een tolk jullie legde alles uit en kregen een tijdelijk onderdak. 
    Nederland was op de hoogte van het probleem in Turkije en we mochten blijven na 3 maanden was alle documentatie gefikst en waren we Officieel Nederlanders. 
    De Nederlandse regering kon de veiligheid voor ons wel vast stellen dat wij die schulden aan de smokkelaars niet hoefde te betalen, 
    maar onze familie konden ze niet hiernaartoe halen.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")           
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel17():
    tekst = """\n
    DEEL 17\n
    Jullie namen de vluchtelingen niet mee omdat jullie het geen goed idee vonden maar jullie voelden je wel schuldig. 
    Toch ging de reis door en we moesten door heel Europa van Turkije naar Bulgarije van Bulgarije naar Servië 
    van Servië naar van Hongarije van Hongarije naar Oosterwijk van Oosterijk naar Duitsland en van Duitsland werden jullie achtergelaten in Nederland om precies te zijn in Amsterdam. 
    De smokkelaars gingen razendsnel weg en lieten jullie achter met een map van Amsterdam. 
    Jullie gingen naar het gemeentehuis en kregen een tolk jullie legde alles uit en kregen een tijdelijk onderdak. 
    Nederland was op de hoogte van het probleem in Turkije en we mochten blijven na 3 maanden was alle documentatie gefikst en waren we Officieel Nederlanders. 
    De Nederlandse regering kon de veiligheid voor ons wel vast stellen dat wij die schulden aan de smokkelaars niet hoefde te betalen, 
    maar onze familie konden ze niet hiernaartoe halen. Na elke jaren kreeg je een vrouw en kinderen en gingen jullie op vakantie naar Turkije, 
    waar het toen rustig was. Je was dol blij om je familie weer is te zien, maar jullie bleven toch wonen in Nederland.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")            
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)           
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel18():
    tekst = """\n
    DEEL 18\n
    In de nacht toen de bewakers van dienst gingen wisselen liet jij Adam vrij. 
    Hij zei ik hoop dat je het overleeft en ging weg ik snapte het eerst niet maar een uur later wel. 
    De rebellen kwamen en overrompelde ons. Jij werd beschoten op je arm. 
    Jullie kregen meer versterking en na een tijd werden er zo veel rebellen uitgeschakeld dat het over was Furkan had gewonnen. 
    De overige rebellen waren zich aan het verstoppen en jij zat met je familie lekker in Antalya om uit te rusten.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")           
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")           
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel19():
    tekst = """\n
    DEEL 19\n
    Adam ontsnapten uit de gevangenis omdat er nog een infiltrant was die hem hielp.
    Jij ging er achteraan maar die infiltrant schoot jou neer. 
    Niemand kon jou helpen het was te laat en je ging dood...
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")            
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)           
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")

def Deel20():
    tekst = """\n
    DEEL 20\n
    Jij zei op het politiebureau dat het allemaal Adams plan was. 
    De smokkelaar kwam binnen als getuige dat jij gelijk had. Adam haatte je en jij mocht vrij hij zat vast. 
    Jij had stiekem geld verstopt en gegeven aan de smokkelaar en hij bracht jou met een privévliegtuig naar een privé vliegveld in Nederland. 
    Van daar ging jij naar Utrecht en regelde je dat jij in Nederland mocht blijven als vluchteling.
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")           
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")
    
def Deel21():
    tekst = """\n
    DEEL 21\n
    Jullie vluchten van de politie en kopen veel mensen om onderweg. 
    Jij en Adam bedenken een nieuw plan jullie gaan met zijn 2e zonder de hulp van de smokkelaar naar Europa dat lukt. 
    Jullie maakte nep paspoorten en vlogen naar Duitsland voor een business meeting onder neppe namen. 
    Vanuit daar reden jullie naar Nederland om daar te wonen. 
    Jullie legde het verhaal uit maar vertelde er niet bij dat jullie een bank hadden overvallen de Turkse regering wist ook niet dat zei dat waren. 
    Dus ze mochten gewoon blijven in Nederland. 
    Jullie kregen al snel een baan als schoon maker en jij ontmoete een vrouw en vormde een gezin. 
    EINDE.\n
    """
    for char in tekst:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("Wil je opnieuw beginnen?")
    print("""\
                                          [JA]                                     [NEE]
           """)
    
    vraag=input("Typ je antwoord >")
    incorrect = True
    while incorrect == True:
        if vraag == 'JA' or vraag == 'ja':
            os.system("clear")           
            Deel1()
            incorrect = False
        elif vraag == 'NEE' or vraag == 'nee':
            print("Het script is beëindigd.")
            sleep(3)            
            os.system("clear")            
            incorrect = False
        else:
            print("voer JA of NEE in")
            vraag=input("Typ je antwoord >")
Deel1() 

