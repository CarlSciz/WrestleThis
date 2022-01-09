WWE = "WWE"
Championships = "Championships"

category =  ('Select a Category:'"\n" + "\n" + 
             'Championships'"\n" +
             'Hall Of Fame'"\n" +
             'Pay Per Views'"\n"
            )

wwe_belts = ( 'Pick a belt:' + "\n" + "\n" +
             'Intercontinental Championship' "\n" +
             'Tag Team Championship' "\n" +
             'United States Championship' "\n" +
             'Women WWE Championship' "\n" +
             'WWE Championship')


#Come Back and fix this, Actual get it centered instead of using tabs.
print ('\033[1m' + '\t\t\t\tWrestle This' + '\033[0m')
print (2 * "\n")
print ('\x1B[3m' + 'Pick a Wrestling Company:' + '\x1B[3m' + "\n"+ "\n"+
       'WWE'"\n"+
       'AEW'"\n"+
       'NWA'"\n"+
       'Impact(TNA)'"\n"+
       'NXT'"\n"+
       'WCW'"\n" + "\n"
       )

User_Pick = input()

if User_Pick == "WWE":

    print ("\n" + category)
    Category_Pick = input() 
    if Category_Pick == "Championships":
        print ("\n" + wwe_belts )
