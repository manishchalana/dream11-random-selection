




bat = 'bat'
bowl = 'bowl'
wk = 'wk'
ar = 'ar'

# ('player name')
t1 = 'mi'
t2 = 'rr'
numOfTeams = 5

p1 = {'name': 'Q Kock', 'type':wk, 'points': 9, 'team': t1, 'star':1}
p2 = {'name': 'R Sharma', 'type':bat, 'points': 10, 'team': t1, 'star':1}
p3 = {'name': 'S Yadav', 'type':bat, 'points': 9, 'team': t1, 'star':0}
p4 = {'name': 'I Kishan', 'type':bat, 'points': 8.5, 'team': t1, 'star':0}
p5 = {'name': 'H Pandya', 'type':ar, 'points': 9.5, 'team': t1, 'star':1}
p6 = {'name': 'K Pandya', 'type':ar, 'points': 8.5, 'team': t1, 'star':0}
p7 = {'name': 'K Pollard', 'type':bat, 'points': 9, 'team': t1, 'star':1}
p8 = {'name': 'J Behrendorff', 'type':bowl, 'points': 8.5, 'team': t1, 'star':0}
p9 = {'name': 'R Chahar', 'type':bowl, 'points': 8, 'team': t1, 'star':0}
p10 = {'name': 'A Joseph', 'type':bowl, 'points': 8.5, 'team': t1, 'star':0}
p11 = {'name': 'J Bumrah', 'type':bowl, 'points': 9, 'team': t1, 'star':1}
p12 = {'name': 'A Rahane', 'type':bat, 'points': 9, 'team': t2, 'star':0}
p13 = {'name': 'J Butler', 'type':bat, 'points': 10.5, 'team': t2, 'star':1}
p14 = {'name': 'S Smith', 'type':bat, 'points': 9, 'team': t2, 'star':1}
p15 = {'name': 'S Samson', 'type':wk, 'points': 9, 'team': t2, 'star':0}
p16 = {'name': 'R Tripathi', 'type':bat, 'points': 8.5, 'team': t2, 'star':0}
p17 = {'name': 'L Livingstone', 'type':bat, 'points': 8, 'team': t2, 'star':0}
p18 = {'name': 'K Gowtham', 'type':ar, 'points': 8.5, 'team': t2, 'star':0}
p19 = {'name': 'J Archer', 'type':bowl, 'points': 9, 'team': t2, 'star':1}
p20 = {'name': 'S Gopal', 'type':bowl, 'points': 8.5, 'team': t2, 'star':0}
p21 = {'name': 'J Unadkat', 'type':bowl, 'points': 8, 'team': t2, 'star':0}
p22 = {'name': 'D Kulkarni', 'type':bowl, 'points': 8.5, 'team': t2, 'star':0}


players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11,
           p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22]
teams = [t1, t2]

from dreamteam import Dream11


if __name__ == '__main__':        
    myTeam = Dream11(players, teams)  
    teams = myTeam.generateTeams(numOfTeams, captain=True) 

    



