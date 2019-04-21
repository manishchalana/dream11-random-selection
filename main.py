




bat = 'bat'
bowl = 'bowl'
wk = 'wk'
ar = 'ar'


t1 = 'srh'
t2 = 'kkr'
numOfTeams = 8

# ('player name', 'player role', 'player points in dream11 app', 'player team', 'star player i.e. identifier to denote whether must be included in the team or not (if star =1, player will be included in the team'))

p1 = {'name': 'J Bairstow', 'type':wk, 'points':10 , 'team': t1, 'star':1}#
p2 = {'name': 'D Warner', 'type':bat, 'points': 11, 'team': t1, 'star':1}#
p3 = {'name': 'Y Pathan', 'type':bat, 'points': 8, 'team': t1, 'star':0}#
p4 = {'name': 'M Pandey', 'type':bat, 'points': 8.5, 'team': t1, 'star':0}#
p5 = {'name': 'V Shankar', 'type':ar, 'points': 8.5, 'team': t1, 'star':0}#
p6 = {'name': 'S Al Hasan', 'type':ar, 'points': 8.5, 'team': t1, 'star':0}#
p7 = {'name': 'D Hooda', 'type':bat, 'points': 8, 'team': t1, 'star':0}#
p8 = {'name': 'Rashid Khan', 'type':bowl, 'points': 9, 'team': t1, 'star':0}#
p9 = {'name': 'Bhuvi', 'type':bowl, 'points': 8.5, 'team': t1, 'star':0}#
p10 = {'name': 'S Sharma', 'type':bowl, 'points': 8.5, 'team': t1, 'star':0}#
p11 = {'name': 'S Kaul', 'type':bowl, 'points': 8.5, 'team': t1, 'star':0}#


p12 = {'name': 'C lynn', 'type':bat, 'points': 9.5, 'team': t2, 'star':0}#
p13 = {'name': 'N Rana', 'type':bat, 'points': 9, 'team': t2, 'star':0}#
p14 = {'name': 'R Uthappa', 'type':bat, 'points': 9, 'team': t2, 'star':0}#
p15 = {'name': 'D Karthik', 'type':wk, 'points': 9, 'team': t2, 'star':0}#
p16 = {'name': 'S Gill', 'type':bat, 'points': 8, 'team': t2, 'star':0}#
p17 = {'name': 'S Narine', 'type':ar, 'points': 9, 'team': t2, 'star':0}#
p18 = {'name': 'A Russell', 'type':ar, 'points': 10.5, 'team': t2, 'star':1}#
p19 = {'name': 'P Chawla', 'type':bowl, 'points': 8.5, 'team': t2, 'star':0}#
p20 = {'name': 'K Yadav', 'type':bowl, 'points': 8.5, 'team': t2, 'star':0}#
p21 = {'name': 'L Ferguson', 'type':bowl, 'points': 8.5, 'team': t2, 'star':0}#
p22 = {'name': 'P Krishna', 'type':bowl, 'points': 8, 'team': t2, 'star':0}#    

players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11,
           p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22]
teams = [t1, t2]

from dreamteam import Dream11


if __name__ == '__main__':        
    Dream11(players, teams).generateTeams(numOfTeams, captain=True) 

    



