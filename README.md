# dream11-random-selection
Sample a team to play Dream11

The code can create a random team(s) given playing 11 of both the teams. 

## Input requirements
- Name of the teams in variable t1 and t2 respectively. 

  Sample input:
 
 
  '''
  
  t1 = 'srh'
  
  t2 = 'kkr'
  
  '''

- Following details of all the players to be stored in the variable p1, p2, ..., p22, which are all dictionaries with the below key-value pairs.
  
  name : Name of the player (To be input as strings; should be unique)
  
  type: 'wk', 'bat', 'bowl', 'ar' for wicket-keeper, batsman, bowler, and all-rounder respectively. (To be input as one of the variables wk, bat, ar and bowl depending on the type of the player on main.py file)
  
  points: Cost of the player from Dream11 App (To be input as integer or floating point numbers)
  
  team: Name of the team player belongs to (To be input as variable t1/t2 on main.py file)
  
  star player identifier: 1 or 0; all players with value 1 for this key will be selected in all the teams and selection will only happen on players with the value 0 for this key


- Number of teams to be sampled given by variable 'numOfTeams'


## Logic
A random combination is chosen from the below list of possible combinations:

[1,3,2,5], [1,3,3,4], [1,4,1,5], [1,4,2,4], [1,4,3,3], [1,5,1,4], [1,5,2,3]


- Step1: Each of the tuple in the above list refers to a team combination where the four numbers denote number of wicket-keepers, batsman, all-rounder and bowler respectively in a hypothetical playing 11. A random combination is selected with equal probability for each of the combination. (Will be configurable in the next version)

- Step 2: Repeat below for each of the four categories i.e. wicket keeper, batsman, all-rounder and bowler. 

  Players are divided between stars and non-stars players set. 

  All star players are included in the team by default. In case number of star players in a category exceeds required number     of players, a random sample out of the star players is taken (Using softmax probabilities derived from the star players       set)

  After star players are included and their are still a few spots to fill from the non-star players, a random comibination is   selected from the non-star players set (Using softmax probabilities derived from the non-star players set)

- Step 3: The sampled team from step 2 has to satisfy a number of criterias as follows:

    - A minimum of 4 and a maximum of 7 players are allowed from each team.
    
    - Maximum number of points to create team is limited to 100.
    
    - The team should not be very similar to already selected teams. To check this, Dis-similarity index is defined as               follows:
          
      To calculate the dis-similarity index, all teams (currently sampled team and already selected teams) are converted to a       22 dimensional vector with each dimension corresponding to 22 players playing in the match. The value of the entry will       be equal to the points for the player if the player is part of sampled team, otherwise 0.
      
      The L2 norm is computed for the sampled team vector with the team vector of previously selected teams. This number has         to be greater than a threshold to pass the dis-similarity criteria. 
      
  If the team satisfies the above criteria, then team is added to the list of already selected teams. 




## Output 

Sample teams with a few additional details put together

### Sample Output
Sample Output for a hypothetical SRH vs KKR match:


------------ Team 1 ------------

S.No. Player C/VC Team  Type  Points

1    J BAIRSTOW       SRH    wk    10.0

2      D WARNER       SRH   bat    11.0

3        S GILL   vc  KKR   bat     8.0

4       D HOODA       SRH   bat     8.0

5     A RUSSELL       KKR    ar    10.5

6    S AL HASAN    c  SRH    ar     8.5

7   RASHID KHAN       SRH  bowl     9.0

8        S KAUL       SRH  bowl     8.5

9    L FERGUSON       KKR  bowl     8.5

10        BHUVI       SRH  bowl     8.5

11    P KRISHNA       KKR  bowl     8.0


Total points invested: 98.5

Wicket-keepers: 1 , Batsman: 3 , All-rounders: 2  Bowlers: 5

SRH : 7 KKR : 4

Similarity indices: []



------------ Team 2 ------------

S.No. Player C/VC Team  Type  Points

1   J BAIRSTOW       SRH    wk    10.0

2     D WARNER       SRH   bat    11.0

3       C LYNN       KKR   bat     9.5

4       N RANA       KKR   bat     9.0

5      D HOODA    c  SRH   bat     8.0

6       S GILL       KKR   bat     8.0

7    A RUSSELL       KKR    ar    10.5

8    V SHANKAR   vc  SRH    ar     8.5

9        BHUVI       SRH  bowl     8.5

10    S SHARMA       SRH  bowl     8.5

11   P KRISHNA       KKR  bowl     8.0


Total points invested: 99.5

Wicket-keepers: 1 , Batsman: 5 , All-rounders: 2  Bowlers: 3

SRH : 6 KKR : 5

Similarity indices: [24.76893215300167]



------------ Team 3 ------------


S.No. Player C/VC Team  Type  Points

1   J BAIRSTOW    c  SRH    wk    10.0

2     D WARNER   vc  SRH   bat    11.0

3       N RANA       KKR   bat     9.0

4     M PANDEY       SRH   bat     8.5

5    A RUSSELL       KKR    ar    10.5

6     S NARINE       KKR    ar     9.0

7    V SHANKAR       SRH    ar     8.5

8     S SHARMA       SRH  bowl     8.5

9   L FERGUSON       KKR  bowl     8.5

10    P CHAWLA       KKR  bowl     8.5

11   P KRISHNA       KKR  bowl     8.0


Total points invested: 100.0

Wicket-keepers: 1 , Batsman: 3 , All-rounders: 3  Bowlers: 4

SRH : 5 KKR : 6

Similarity indices: [29.609964538985857, 24.253865671269807]



------------ Team 4 ------------


S.No. Player C/VC Team  Type  Points

1    J BAIRSTOW    c  SRH    wk    10.0

2      D WARNER       SRH   bat    11.0

3     R UTHAPPA       KKR   bat     9.0

4       D HOODA       SRH   bat     8.0

5        S GILL       KKR   bat     8.0

6     A RUSSELL   vc  KKR    ar    10.5

7      S NARINE       KKR    ar     9.0

8   RASHID KHAN       SRH  bowl     9.0

9      P CHAWLA       KKR  bowl     8.5

10      K YADAV       KKR  bowl     8.5

11     S SHARMA       SRH  bowl     8.5


Total points invested: 100.0

Wicket-keepers: 1 , Batsman: 4 , All-rounders: 2  Bowlers: 4

SRH : 5 KKR : 6

Similarity indices: [27.050877989447958, 27.69927796892908, 26.90724809414742]








