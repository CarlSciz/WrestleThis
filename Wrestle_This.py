from wrestle_pkg.Home_Page import show_homepage




#Wrestling Promotions
WWE = "WWE"
AEW = "AEW"
NWA = "NWA"
IMPACT = "IMPACT"
NXT = "NXT"
WCW = "WCW"



category =  ('Select a Category:'"\n" + "\n" + 
             '1) Championships'"\n" +
             '2) Hall Of Fame'"\n" +
             '3) Pay Per Views'"\n"
            )


# Championship Belts

Championships = "Championships"

wwe_belts = ( 'Pick a belt:' + "\n" + "\n" +
             '1) Intercontinental Championship' "\n" +
             '2) Tag Team Championship' "\n" +
             '3) United States Championship' "\n" +
             '4) Women WWE Championship' "\n" +
             '5) WWE Championship')

aew_belts = ('Pick a belt:' + "\n" + "\n" +
             '1) AEW World Championship' "\n" + 
             '2) AEW Women World Championship' "\n" +
             '3) AEW TNT Championship' "\n" +
             '4) AEW TBS Championship' "\n" +
             '5) AEW World Tag Team Championship')

nwa_belts = ( 'Pick a belt:' + "\n" + "\n" +
              '1) NWA Worlds Heavyweight Championship,' "\n" +
              '2) NWA World Women Championship'
              '3) NWA World Television Championship' "\n" +
              '4) NWA World Tag Team Championship' "\n" +
              '5) NWA National Championship' )

impact_belts = ('Pick a belt:' + "\n" + "\n" +
               '1) Impact World CHampionship' "\n" +
               '2) Impact X Division Championship' "\n" +
               '3) Impact World Tag Team Championship' "\n" +
               '4) Impact Knockout Chmapionship')

nxt_belts = ('Pick a belt:' + "\n" + "\n" +
            '1) NXT Championship' "\n" +
            '2) NXT North American Championship' "\n" +
            '3) NXT Tag Team Championship' "\n" +
            '4) NXT Women Championship' "\n" +
            '5) NXT Women Tag Team Championship')

wcw_belts = ('Pick a belt:' + "\n" + "\n" +
            '1) WCW Championship' "\n" +
            '2) WCW United States Championship' "\n" +
            '3) World Tag Team Championship' "\n" +
            '4) WCW Cruiserweight Championship' "\n")

#Belt Question

#Answer is Honky Tonk Man (454 days)
ic_title = ('Who is the longest reigning Intercontinental Champion?' + "\n" + "\n" +
            '1) Honky Tonk Man' "\n" +
            '2) Macho Man Randy Savage' "\n" +
            '3) The Miz'"\n" +
            '4) Shawn Michaels The Heartbreak Kid')

#Answer is Demolition (698 days)
tag_title = ('Who is the longest reigning Tag Team Champions' "\n" +
            '1) The Dudley Boyz: Bubba Rey and Devon' "\n" +
            '2) The Wild Samoans: Afa and Sika' "\n" +
            '3) The Hart Foundation: Bret Hart and Road Doagg' "\n" +
            '4) Demolition: Ax and Smash')

#Answer is Ric Flair (6)
us_title = ('Who has won the United States Championship the most?' + "\n" + "\n" +
            '1) John Cena' "\n" +
            '2) Chris Benoit' "\n" +
            '3) Ric Flair' "\n" +
            '4) Lex Luger')

#Answer is CM Punk (14)
wwe_title = ('Who has successfully defended the WWE Championship the most?' + "\n" + "\n" +
             '1) Hulk Hogan' "\n" +
             '2) CM Punk' "\n" +
             '3) Seth Rollins' "\n" +
             '4) The Undertaker')

#Answer is Trish Stratus (7)
women_wwe_title = ('Who has the most title reigns as WWE Women World Champion?' "\n" +
                    '1) The Fabulous Moolah' "\n" +
                    '2) Alundra Blayze' "\n" +
                    '3) Mickeie James' "\n" +
                    '4) Trish Stratus')


#Hall of Fame
hall_of_fame = "Hall Of Fame"

wwe_hof = ('Pick a wrestler:'  + "\n" + "\n" +
            '1) Macho Man Randy Savage' "\n" +
            '2) The UnderTaker' "\n" +
            '3) Rick Flair')

#Savage Flying Elbow Drop
macho = ('What was Macho Man Randy Savage finishing move?' "\n" +
        '1) OOOHH Yeah SuperPlex' "\n" +
        '2) Savage Flying Elbow Drop' "\n" +
        '3) Cream Crop Leg Drop')

#23-2 is the answer
taker = ('What is the Wrestlemania Record of The UnderTaker?' "\n" +
        '1) 15-10 ' "\n" +
        '2) 19-6' "\n" +
        '3) 23-2' "\n" +
        '4) 20-5')

#16 is the answer
flair = ('How many World HeavyWeight Champioships does The Stylin,' +
'profilin, limosuine riding jet flying, kiss-stealing, wheelin-n-dealin son of gun Ric Flair have?'"\n" +
        '1) 12-time' "\n" +
        '2) 16-time' "\n" +
        '3) 10-time' "\n" +
        '4) 14-time')

aew_hof = ('Pick a wrestler:'+ "\n" + "\n" +
            '1) Cody Rhodes' "\n" +
            '2) Kenny Omega' "\n" +
            '3) Young Bucks')

nwa_hof = ('Pick a wrestler:'+ "\n" + "\n" +
            '1) Dusty Rhodes' "\n" +
            '2) Harley Race' "\n" +
            '3) Nick Aldis')

impact_hof = ('Pick a wrestler:'+ "\n" + "\n" +
            '1) Abyss' "\n" +
            '2) Jeff Jarrett' "\n" +
            '3) Aj Styles')

nxt_hof = ('Pick a wrestler:'+ "\n" + "\n" +
            '1) Johnny Gargano' "\n" +
            '2) Adam Cole' "\n" +
            '3) Samoa Joe')

#Pay Per Views
ppv = "Pay Per Views"

wwe_ppv = ('Pick a Pay Per View:' "\n" +
            '1) Wrestlemania' "\n" +
            '2) SummerSlam' "\n" +
            '3) Royal Rumble')

#Answer is Wrestlemania III
mania = ('What Wrestlemania at the Pontiac Silverdome did Hulk Hogan defeated Andre The Giant for the WWF Championship' "\n" +
        '1) Wrestlemania II' "\n" +
        '2) Wrestlemania VI' "\n" +
        '3) Wrestlemania III' "\n" +
        '4) Wrestlemania IV')

#Answer is SummerSlam 1992
summerslam = ('What SummerSlam took place at the Wembley Stadium with an emotional main event for the Intercontinental Championship Davey Smith vs Bret Hart?' "\n" +
            '1) SummerSlam 1993' "\n" +
            '2) SummerSlam 1992' "\n" +
            '3) SummerSlam 1990' "\n" +
            '4) SummerSlam 1996')

#Answer is Royal Rumble 2001
royalRumble = ("What was the last Royal Rumble Stone Cold Steve Austin Won, cementing him with the most Royal Rumble Wins at 3?" "\n" +
             '1) Royal Rumble 2001' "\n" +
             '2) Royal Rumble 1998' "\n" +
             '3) Royal Rumble 2004' "\n" +
             '4) Royal Rumble 2007')

aew_ppv = ('Pick a Pay Per View:')
nwa_ppv = ('Pick a Pay Per View:')
impact_ppv = ('Pick a Pay Per View:')
nxt_ppv = ('Pick a Pay Per View:')


belts_pick = ("Championships")
hof_pick = ("Hall Of Fame")
ppv_pick = ("Pay Per Views")

the_ic_title = ("1) Intercontinental Championship")
the_tag_title = ("2) Tag Team Championship")
the_us_title = ("3) United States Championship")
the_women_title = ("4) Women WWE Championship")
the_wwe_title = ("5) WWE Championship")

aew_world_title = ("1) AEW World HeavyWeight Championship")
aew_women_title = ("2) AEW Women World Championship")
aew_tnt_title = ("3) AEW TNT Championship")
aew_tbs_title = ("4) AEW TBS Championship")
aew_tag_team_title = ("5) AEW World Tag Team Championsiop")


while True:
    show_homepage()

    choice = input()

    #Select Promotions 
    #This is WWE
    if choice == "1":
        print("\n" +category)
        Category_Pick = input()
        
        if Category_Pick.lower() == "1":
            
            print(wwe_belts)
            belt_pick = input()
            
            if belt_pick == "1":
                print(ic_title)
                qa_pick = input()
                if qa_pick == "1":
                    print("That is correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            elif belt_pick == "2":
                print(tag_title)
                qa_pick = input()
                if qa_pick =="4":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            elif belt_pick == "3":
                print(us_title)
                qa_pick = input()
                if qa_pick =="3":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            elif belt_pick == "4":
                print(women_wwe_title)
                qa_pick = input()
                if qa_pick =="4":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            elif belt_pick == "5":
                print(wwe_title)
                qa_pick = input()
                if qa_pick =="2":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

        elif Category_Pick == "2":
            print(wwe_hof)
            wrestle_pick = input()
            
            if wrestle_pick == "1":
                print(macho)
                qa2_pick = input()
                
                if qa2_pick == "2":
                    print("Too hot to handle too cold to hold! OHHHHH YEAH!(You're Correct!)")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            
            elif wrestle_pick == "2":
                print(taker)
                qa2_pick = input()
                
                if qa2_pick == "3":
                    print("Too hot to handle too cold to hold! OHHHHH YEAH!(You're Correct!)")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            if wrestle_pick == "3":
                print(flair)
                qa2_pick = input()
                
                if qa2_pick == "2":
                    print("Too hot to handle too cold to hold! OHHHHH YEAH!(You're Correct!)")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

        elif Category_Pick == "3":
            print(wwe_ppv)
            wrestle_pick = input()
            if wrestle_pick == "1":
                print(mania)
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            elif wrestle_pick == "2":
                print(summerslam)
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            elif wrestle_pick == "3":
                print(royalRumble)
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
        
    #This is AEW
    if choice == "2":
        print(aew_belts)

    elif choice == "3":
        print(nwa_belts)
    elif choice == "4":
        print(impact_belts)
    elif choice == "5":
        print(nxt_belts)
    elif choice == "6":
        print(wcw_belts)
    elif choice == "7":
        print("\n" +"\nRKO Out of NOWHERE!!! Goodnight...."+ "\n" + "\n")

        break



    