#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 02:58:47 2019

@author: ManishChalana
"""

import numpy as np
import collections
import pandas as pd



class Team:
    def __init__(self, players, teams):
        self.players = players
        self.team1 = teams[0]
        self.team2 = teams[1]
        numPlayers = collections.Counter([player['team'] for player in self.players])
        assert list(numPlayers.values())==[11,11],  "Invalid combination! Number of players in " + self.team1 + ": " + str(numPlayers[self.team1]) + "," + self.team2 + ": " + str(numPlayers[self.team2])
        
        
class Dream11(Team):
    
    def __init__(self, players, teams):
        super().__init__(players, teams)
        self.teamParams = {'min':4, 'max':7}
        self.maxPoints = 100
        self.combinations = [[1,3,2,5], [1,3,3,4], [1,4,1,5], [1,4,2,4], [1,4,3,3], [1,5,1,4], [1,5,2,3]]
#        self.combinationsProb = [0.14]*6 + [0.16] 
#        self.combinationsProb = [0.1,0.2,0.05,0.2,0.3,0.05,0.1]
        self.playerNames = [p['name'] for p in players]
        self.playerPointMap = {p['name']:p['points'] for p in self.players}
        self.playerTeamMap = {p['name']:p['team'] for p in self.players}
        self.playerTypeMap = {p['name']:p['type'] for p in self.players}
        self.playerTypeCount = collections.Counter(self.playerTypeMap.values())
                
    @staticmethod
    def getSoftmaxProbabilities(points, toneDownMultiplier=1):
        if len(points) == 0:
            return []
        points = [toneDownMultiplier*point for point in points]
        denom = np.sum([np.exp(point) for point in points])
        softMax = [np.exp(point)/denom for point in points]
        return softMax
    
    
    def sample(self, players, req): 
        numStars = np.sum([p['star'] for p in players])
        
        availableStars = [p['name'] for p in players if p['star']==1]
        availableStarsPoints = [p['points'] for p in players if p['star']==1]
        availableStarsSoftMax = Dream11.getSoftmaxProbabilities(availableStarsPoints)
        
        availableNonStars = [p['name'] for p in players if not(p['star']==1)]
        availableNonStarsPoints = [p['points'] for p in players if not(p['star']==1)]
        availableNonStarsSoftMax = Dream11.getSoftmaxProbabilities(availableNonStarsPoints)
    
        if numStars >= req:
            return ([] if len(availableStars)==0 else list(np.random.choice(availableStars, size = req, p=availableStarsSoftMax, replace=False)))
        else:
            return availableStars + list(np.random.choice(availableNonStars, size = req - numStars, p=availableNonStarsSoftMax, replace=False))      
    
    def calculateTeamVector(self, team):
        teamVector = [player['points'] if (player['name'] in team) else 0 for player in self.players]
        return teamVector

    def checkUniqueTeamCriteria(self, sampledTeam, selectedTeams):
        return (np.sum([set(team)==set(sampledTeam) for team in selectedTeams]) == 0)
    
    def checkMinPlayersTeamCriteria(self, teamDemography):
        return (teamDemography[self.team1]>=self.teamParams['min']) and (teamDemography[self.team2]>=self.teamParams['min']) 
    
    def checkMaxPlayersTeamCriteria(self, teamDemography):
        return (teamDemography[self.team1]<=self.teamParams['max']) and (teamDemography[self.team2]<=self.teamParams['max'])
    
    def checkMaxTeamPointsCriteria(self, sampledTeam):
        totalPoints = np.sum([self.playerPointMap[player] for player in sampledTeam])
        return (totalPoints <= self.maxPoints)
        
    def checkSimilarityIndexCriteria(self, sampledTeam, selectedTeams, selected, thresh=24):
        
        similarityIndexCriteria = False
        similarityIndices = []
        
        if selected>0:
            similarityIndices = [np.sqrt(np.sum(np.square(np.array(self.calculateTeamVector(sampledTeam)) - np.array(self.calculateTeamVector(team))))) for team in selectedTeams]
            if np.min(similarityIndices) > thresh:
                similarityIndexCriteria = True
        else:
            similarityIndexCriteria = True
        return similarityIndices, similarityIndexCriteria
    
    def chooseCaptain(self, sampledTeam, captain):
        [c, vc] = ['', '']
        if captain:
            sampledTeamSoftmax = [self.playerPointMap[name] for name in sampledTeam]
            [c, vc] = np.random.choice(sampledTeam, size=2, replace=False, p=Dream11.getSoftmaxProbabilities(sampledTeamSoftmax, toneDownMultiplier=0.75))   
            
        return [c, vc]

    def updateSelectedTeams(self, sampledTeam, selectedTeams, selected, captain):
        #Finding the numbers of wks, bats, ar and bowls in the sampled team
        teamDemography = collections.Counter([self.playerTeamMap[player] for player in sampledTeam])
        
        # Finding the total number of points spent in selecting the sampled team and ensuring that it is less than maximum available points
        pointsCriteria = self.checkMaxTeamPointsCriteria(sampledTeam)
        
        # Ensuring that sampled team is not same as one of the previously selected teams
        uniqueTeamCriteria = self.checkUniqueTeamCriteria(sampledTeam, selectedTeams)
        
        # Making sure that minimum required players are selected in sampled team from each of the two parent teams
        minPlayersCriteria = self.checkMinPlayersTeamCriteria(teamDemography)
        
        # Making sure that maximum required players are selected in sampled team from each of the two parent teams
        maxPlayersCriteria = self.checkMaxPlayersTeamCriteria(teamDemography)
        
        # Calculating the similarity index of the sampled team with the already selected teams to ensure dissimilarity
        similarityIndices, similarityIndexCriteria = self.checkSimilarityIndexCriteria(sampledTeam, selectedTeams, selected)
        
        # Choosing a captain and vice captain
        [c, vc] = self.chooseCaptain(sampledTeam, captain)
        
        if  pointsCriteria and uniqueTeamCriteria and minPlayersCriteria and maxPlayersCriteria and similarityIndexCriteria:                
            
            # When all criterias are fulfilled by the team, append the sampled team to list of already selected teams
            selectedTeams.append(sampledTeam)                                
            selected = selected + 1
            
            self.printTeamDetails(sampledTeam, selected, c, vc, similarityIndices)
            
            # Finding the attributes of the selected team
            
        return selectedTeams, selected
    
    
    def printTeamDetails(self, sampledTeam, index, c, vc, similarityIndices):
        
        selectedPlayersNames = [name.upper() for name in sampledTeam]
        selectedPlayersPoints = [[p for p in self.players if p['name']==name][0]['points'] for name in sampledTeam]
        selectedPlayersTeams = [[p for p in self.players if p['name']==name][0]['team'].upper() for name in sampledTeam]
        selectedPlayersTypes = [[p for p in self.players if p['name']==name][0]['type'] for name in sampledTeam]
        selectedPlayersCVC = ['c' if name==c else 'vc' if name==vc else ' ' for name in sampledTeam ]
        selectedPlayersTypesCounter = collections.Counter(selectedPlayersTypes)
        selectedPlayersTeamsCounter = collections.Counter(selectedPlayersTeams)
            
        # Defining a dataframe containing the details of sampled team
        teamDf = pd.DataFrame({'Player': selectedPlayersNames, 'C/VC': selectedPlayersCVC, 'Points':selectedPlayersPoints, 'Team':selectedPlayersTeams, 'Type':selectedPlayersTypes}, index=range(1,12))[['Player', 'C/VC', 'Team', 'Type', 'Points']]
        teamDf = pd.concat([teamDf[teamDf['Type']==playType].sort_values(['Points'], ascending=False) for playType in ['wk', 'bat', 'ar', 'bowl']])
        teamDf.index = range(1,12)
            
        # Printing the team on console
        print("------------ Team", index, "------------\n")
        print(teamDf)
        print("\nTotal points invested:", np.sum(teamDf['Points']))
        print("Wicket-keepers:", selectedPlayersTypesCounter['wk'], ", Batsman:", selectedPlayersTypesCounter['bat'], ", All-rounders:", selectedPlayersTypesCounter['ar'], " Bowlers:", selectedPlayersTypesCounter['bowl'])
        print(self.team1.upper(), ":", selectedPlayersTeamsCounter[self.team1.upper()], self.team2.upper(), ":", selectedPlayersTeamsCounter[self.team2.upper()])
        print("Similarity indices:", similarityIndices)
        print('\n')
        
    
    
    
    def generateTeams(self, numTeams, captain=False):
        selectedTeams = []
        selected = 0
        
        while selected < numTeams:
            # Choose a random combination of number of wicket-keepers, batsman, all-rounders and bowlers
            while True:
                [numWks, numBats, numArs, numBowls] = self.combinations[np.random.choice(len(self.combinations), size=1)[0]]
                if (numWks <= self.playerTypeCount['wk']) and (numBats <=self.playerTypeCount['bat']) and (numArs <=self.playerTypeCount['ar']) and (numBowls<=self.playerTypeCount['bowl']):
                    break
            
            # Choose Keepers
            wks = self.sample([p for p in self.players if p['type']=='wk'], numWks)
            
            # Choose batsman
            bats = self.sample([p for p in self.players if p['type']=='bat'], numBats)
            
            # Choose all-rounders
            ars = self.sample([p for p in self.players if p['type']=='ar'], numArs)
            
            # Choose bowlers
            bowls = self.sample([p for p in self.players if p['type']=='bowl'], numBowls)
            
            # Chosen team
            sampledTeam = wks + bats + ars + bowls
            
            # Update selected teams list based on whether the sampled team fulfills all eligibility criteria
            selectedTeams, selected = self.updateSelectedTeams(sampledTeam, selectedTeams, selected, captain)
                            
            
                
                
                
                
        
    
    
