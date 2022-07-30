from wrestle_pkg.Home_Page import *
from wrestle_pkg.AEW import *
from wrestle_pkg.WWE import *
from wrestle_pkg.NWA import *
from wrestle_pkg.NXT import *
from wrestle_pkg.WCW import *
from wrestle_pkg.Impact import *

# Championship Belts

Championships = "Championships"

#Hall of Fame
hall_of_fame = "Hall Of Fame"

#Pay Per Views
ppv = "Pay Per Views"

belts_pick = ("Championships")
hof_pick = ("Hall Of Fame")
ppv_pick = ("Pay Per Views")

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
           
            wwe_ppv()
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
            aew_belts_question()
            belt_pick = input()
            
            if belt_pick == "1":
                AEW_Mens_World_Title()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                        
            elif belt_pick == "2":
                AEW_Womens_World_Title()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "3":
                AEW_TNT_Title()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "4":
                AEW_TBS_Title()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "5":
                AEW_Tag_Team_Title()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
        elif Category_Pick == "2":
            aew_history()
            hist_pick = input()
            if hist_pick == "1":
                rhodes()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else:
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif hist_pick == "2":
                omega()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else:
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif hist_pick == "3":
                bucks()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else:
                    print("WRONG! You just got boo'd out of the Arena!")
            
        
        elif Category_Pick == "3":
            aew_ppv()
            ppv_pick = input()
            
            if ppv_pick == "1":
                all_out()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else:
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "2":
                double_or_nothing()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else:
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "3":
                full_gear()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else:
                    print("WRONG! You just got boo'd out of the Arena!")
        


    elif choice == "3":
        print("\n" + category)
        Category_Pick = input()
        
        if Category_Pick == "1":
            nwa_belts_question()
            belt_pick = input()
            
            if belt_pick == "1":
                nwa_WorldHeavyWeight
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                        
            elif belt_pick == "2":
                nwa_WorldWomenChampionship()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "3":
                nwa_WorldTagTeamChamps()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "4":
                nwa_National()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "5":
                nwa_WorldTelevisionChampionship()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
        elif Category_Pick == "2":
            nwa_hof_question()
            hof_pick = input()
            
            if hof_pick == "1":
                rhodes()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")

            if hof_pick == "2":
                Harley_Race()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            if hof_pick == "3":
                Nick_Aldis()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
        elif Category_Pick == "3":
            nwa_ppv_question()
            ppv_pick = input()
            
            if ppv_pick == "1":
                Crockett_Cup()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")

            if ppv_pick == "2":
                Starrcade()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            if ppv_pick == "3":
                HardTimes()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
    #This is Impact
    elif choice == "4":
        print("\n" + category_Alt)
        Category_Pick = input()
        
        if Category_Pick == "1":
            impact_belts_question
            belt_pick = input()
            
            if belt_pick == "1":
                ImpactWorldChampionship()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "2":
                ImpactKnockOutChampionship()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "3":
                ImpactWorldTagChampionship()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "3":
                ImpactXDivisionChampionship()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
           
            elif belt_pick == "4":
                ImpactKnockOutsTagTeamChampionship()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
        elif Category_Pick == "2":
            impact_hof_question()
            hof_pick = input()
            
            if hof_pick == "1":
                Abyss()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif hof_pick == "2":
                GailKim()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif hof_pick == "3":
                AjStyles()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
        elif Category_Pick == "3":
            impact_ppv_question()
            ppv_pick = input()
            
            if ppv_pick == "1":
                Slammiversary()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "2":
                BoundforGlory()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "3":
                DestinationX()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
    #This is NXT
    elif choice == "5":
        print("\n" + category_Alt)
        Category_Pick = input()
        
        if Category_Pick == "1":
            nxt_belts_question()
            belt_pick = input()
            
            if belt_pick == "1":
                nxt_championship()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif belt_pick == "2":
                nxt_North_American_championship()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "3":
                nxt_Tag_Team_championship()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "3":
                nxt_Women_championship()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "4":
                nxt_Women_Tag_championship()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
        elif Category_Pick == "2":
            nxt_hof_question()
            hof_pick = input()
            
            if hof_pick == "1":
                gargano()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
            elif hof_pick == "2":
                Undisputed_Era()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif hof_pick == "3":
                samoaJoe()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
        elif Category_Pick == "3":
            nxt_ppv_question()
            ppv_pick = input()
            
            if ppv_pick == "1":
                takeOver()
                qa2_pick = input()
                if qa2_pick == "1":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "2":
                WarGames()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "3":
                inYourHouse()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
                    
        
    elif choice == "6":
        print("\n" + category_Alt)
        Category_Pick = input()
        
        if Category_Pick == "1":
            wcw_belts_question()
            belt_pick = input()
            
            if belt_pick == "1":
                wcw_championship()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
           
            elif belt_pick == "2":
                wcw_UnitedStates_championship()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "3":
                wcw_cruiser_championship()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "4":
                wcw_tag_team_championship()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif belt_pick == "2":
                wcw_women_championship()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
        elif Category_Pick == "2":
            wcw_hof_question()
            hof_pick = input()
            
            if hof_pick == "1":
                sting()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
           
            elif hof_pick == "2":
                nwo()
                qa2_pick = input()
                if qa2_pick == "3":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif hof_pick == "3":
                four_horsemen()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
        elif Category_Pick == "3":
            wcw_ppv_question()
            ppv_pick = input()
            
            if ppv_pick == "1":
                halloweenHavoc()
                qa2_pick = input()
                if qa2_pick == "4":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "2":
                greatAmericanBash()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
            
            elif ppv_pick == "3":
                superBrawl()
                qa2_pick = input()
                if qa2_pick == "2":
                    print("Correct!")
                else: 
                    print("WRONG! You just got boo'd out of the Arena!")
        
                    
            
        
    elif choice == "7":
        print("\n" +"\nRKO Out of NOWHERE!!! Goodnight...."+ "\n" + "\n")

        break


    