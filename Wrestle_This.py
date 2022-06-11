from wrestle_pkg.Home_Page import show_homepage
from wrestle_pkg.AEW import *
from wrestle_pkg.WWE import *

category =  ('Select a Category:'"\n" + "\n" + 
             '1) Championships'"\n" +
             '2) Hall Of Fame'"\n" +
             '3) Pay Per Views'"\n"
            )
category_Alt = ('Select a Category:'"\n" + "\n" + 
             '1) Championships'"\n" +
             '2) Company History'"\n" +
             '3) Pay Per Views'"\n"
            )

# Championship Belts

Championships = "Championships"

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

#Hall of Fame
hall_of_fame = "Hall Of Fame"

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
aew_tag_team_title = ("5) AEW World Tag Team Championsip")

while True:
    show_homepage()

    choice = input()

    #Select Promotions 
    #This is WWE
    if choice == "1":
        print("\n" + category)
        Category_Pick = input()
        
        if Category_Pick == "1":
            
            show_belts()
            belt_pick = input()
            
            if belt_pick == "1":
                
                show_ic_title()
                qa_pick = input()
                if qa_pick == "1":
                    print("That is correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            
            elif belt_pick == "2":
                tag_title()
                qa_pick = input()
                if qa_pick =="4":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            elif belt_pick == "3":
                us_title()
                qa_pick = input()
                if qa_pick =="3":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            elif belt_pick == "4":
                women_wwe_title()
                qa_pick = input()
                if qa_pick =="4":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            elif belt_pick == "5":
                wwe_title()
                qa_pick = input()
                if qa_pick =="2":
                    print("Correct!")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

        elif Category_Pick == "2":
            wwe_hof()
            wrestle_pick = input()
            
            if wrestle_pick == "1":
                macho()
                qa2_pick = input()
                
                if qa2_pick == "2":
                    print("Too hot to handle too cold to hold! OHHHHH YEAH!(You're Correct!)")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            
            elif wrestle_pick == "2":
                taker()
                qa2_pick = input()
                
                if qa2_pick == "3":
                    print("Too hot to handle too cold to hold! OHHHHH YEAH!(You're Correct!)")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

            if wrestle_pick == "3":
                flair()
                qa2_pick = input()
                
                if qa2_pick == "2":
                    print("Too hot to handle too cold to hold! OHHHHH YEAH!(You're Correct!)")
                else:
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")

        elif Category_Pick == "3":
            wwe_ppv
            wrestle_pick = input()
            if wrestle_pick == "1":
                mania()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            elif wrestle_pick == "2":
                summerslam()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
            elif wrestle_pick == "3":
                royalRumble()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("TOMBSTONE PILE DRIVER!!! REST IN PEACE (You're Wrong)")
        
    #This is AEW
    
    if choice == "2":
        print("\n" + category_Alt)
        Category_Pick = input()
        
        if Category_Pick == "1":
            aew_belts_question
            belt_pick = input()
            
            if belt_pick == "1":
                AEW_Mens_World_Title
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                        
            elif belt_pick == "2":
                AEW_Womens_World_Title
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "3":
                AEW_TNT_Title
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "4":
                AEW_TBS_Title
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "5":
                AEW_Tag_Team_Title
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
        elif Category_Pick == "2":
            aew_history
            hist_pick = input()
            
            if hist_pick == "1":
                print() 
            
        
        elif Category_Pick == "3":
            aew_ppv
        


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


    