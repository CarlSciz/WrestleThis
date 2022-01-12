
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
             'Intercontinental Championship' "\n" +
             'Tag Team Championship' "\n" +
             'United States Championship' "\n" +
             'Women WWE Championship' "\n" +
             'WWE Championship')

aew_belts = ('Pick a belt:' + "\n" + "\n" +
             'AEW World Championship' "\n" + 
             'AEW Women World Championship' "\n" +
             'AEW TNT Championship' "\n" +
             'AEW TBS Championship' "\n" +
             'AEW World Tag Team Championship')

nwa_belts = ( 'Pick a belt:' + "\n" + "\n" +
              'NWA Worlds Heavyweight Championship,' "\n" +
              'NWA World Women Championship'
              'NWA World Television Championship' "\n" +
              'NWA World Tag Team Championship' "\n" +
              'NWA National Championship' )

impact_belts = ('Pick a belt:' + "\n" + "\n" +
               'Impact World CHampionship' "\n" +
               'Impact X Division Championship' "\n" +
               'Impact World Tag Team Championship' "\n" +
               'Impact Knockout Chmapionship')

nxt_belts = ('Pick a belt:' + "\n" + "\n" +
            'NXT Championship' "\n" +
            'NXT North American Championship' "\n" +
            'NXT Tag Team Championship' "\n" +
            'NXT Women Championship' "\n" +
            'NXT Women Tag Team Championship')

wcw_belts = ('Pick a belt:' + "\n" + "\n" +
            'WCW Cruiserweight Championship' "\n" +
            'WCW United States Heavyweight Championship' "\n" +
            'WCW World Heavyweight Championship' "\n" +
            'WCW World Tag Team Championship' "\n" +
            'WCW World Television Championship')

#Hall of Fame
hall_of_fame = "Hall Of Fame"

wwe_hof = ('Pick a wrestler:')
aew_hof = ('Pick a wrestler:')
nwa_hof = ('Pick a wrestler:')
impact_hof = ('Pick a wrestler:')
nxt_hof = ('Pick a wrestler:')
wcw_hof = ('Pick a wrestler:')

#Pay Per Views
ppv = "Pay Per Views"

wwe_ppv = ('Pick a Pay Per View:')
aew_ppv = ('Pick a Pay Per View:')
nwa_ppv = ('Pick a Pay Per View:')
impact_ppv = ('Pick a Pay Per View:')
nxt_ppv = ('Pick a Pay Per View:')
wcw_ppv = ('Pick a Pay Per View:')



#Come Back and fix this, Actual get it centered instead of using tabs.
print ('\033[1m' + '\t\t\t\tWrestle This' + '\033[0m')
print (2 * "\n")
print ('\x1B[3m' + 'Pick a Wrestling Company:' + '\x1B[3m' + "\n"+ "\n"+
       'WWE'"\n"+
       'AEW'"\n"+
       'NWA'"\n"+
       'Impact'"\n"+
       'NXT'"\n"+
       'WCW'"\n" + "\n"
       )

User_Pick = input()

if User_Pick == "WWE":
    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == 1:
        print ("\n" + wwe_belts )
    elif Category_Pick == 2:
        print ("\n" + wwe_hof )
    elif Category_Pick == 3:
        print ("\n" + wwe_ppv)
            
if User_Pick == "AEW":
    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == 1:
        print ("\n" + aew_belts )
    elif Category_Pick == 2:
        print ("\n" + aew_hof )
    elif Category_Pick == 3:
        print ("\n" + aew_ppv)

if User_Pick == "NWA":
    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == 1:
        print ("\n" + nwa_belts )
    elif Category_Pick == 2:
        print ("\n" + nwa_hof )
    elif Category_Pick == 3:
        print ("\n" + nwa_ppv)

if User_Pick == "IMPACT":
    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == 1:
        print ("\n" + impact_belts )
    elif Category_Pick == 2:
        print ("\n" + impact_hof )
    elif Category_Pick == 3:
        print ("\n" + impact_ppv)
        
if User_Pick == "NXT":
    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == 1:
        print ("\n" + nxt_belts )
    elif Category_Pick == 2:
        print ("\n" + nxt_hof )
    elif Category_Pick == 3:
        print ("\n" + nxt_ppv)
        
if User_Pick == "WCW":
    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == 1:
        print ("\n" + wcw_belts )
    elif Category_Pick == 2:
        print ("\n" + wcw_hof )
    elif Category_Pick == 3:
        print ("\n" + wcw_ppv)