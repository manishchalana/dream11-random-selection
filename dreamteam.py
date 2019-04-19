#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 02:58:47 2019

@author: ManishChalana
"""

import numpy as np
import random as rnd
import collections


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
        self.combinations = [[1,3,2,5], [1,3,3,4], [1,3,4,3], [1,4,1,5], [1,4,2,4], [1,4,3,3], [1,5,1,4], [1,5,2,3]]
        self.playerPointMap = {p['name']:p['points'] for p in self.players}
        self.playerTeamMap = {p['name']:p['team'] for p in self.players}
        self.playerTypeMap = {p['name']:p['type'] for p in self.players}
        self.playerTypeCount = collections.Counter(self.playerTypeMap.values())
        
        
    @staticmethod
    def sample(players, req):
        
        numStars = np.sum([p['star'] for p in players])

        availableStars = [p['name'] for p in players if p['star']==1]

        availableNonStars = [p['name'] for p in players if not(p['star']==1)]
    
        if numStars >= req:
            return ([] if len(availableStars)==0 else rnd.sample(availableStars, req))
        else:
            return availableStars + rnd.sample(availableNonStars, req - numStars)
        
    
    def generateTeams(self, numTeams, captain=False):
        selectedTeams = []
        selected = 0
        
        while selected < numTeams:
            while True:
                [numWks, numBats, numArs, numBowls] = rnd.sample(self.combinations, 1)[0]
                if (numWks <= self.playerTypeCount['wk']) and (numBats <=self.playerTypeCount['bat']) and (numArs <=self.playerTypeCount['ar']) and (numArs<=self.playerTypeCount['bowl']):
                    break
                
                
            wks = Dream11.sample([p for p in self.players if p['type']=='wk'], numWks)
            assert len(wks) == numWks, "Fail! Selected: " + str(wks)
            
            bats = Dream11.sample([p for p in self.players if p['type']=='bat'], numBats)
            assert len(bats) == numBats, "Fail! Selected: " + str(numBats)
            
            ars = Dream11.sample([p for p in self.players if p['type']=='ar'], numArs)
            assert len(ars) == numArs, "Fail! Selected: " + str(numArs)
            
            bowls = Dream11.sample([p for p in self.players if p['type']=='bowl'], numBowls)
            assert len(bowls) == numBowls, "Fail! Selected: " + str(numBowls)
            
            selectedTeam = wks + bats + ars + bowls
 
            
            teamDemography = collections.Counter([self.playerTeamMap[player] for player in selectedTeam])
            
            totalPoints = np.sum([self.playerPointMap[player] for player in selectedTeam])
            pointsCriteria = (totalPoints <= self.maxPoints)
            
            uniqueTeamCriteria = (np.sum([set(team)==set(selectedTeam) for team in selectedTeams]) == 0)
            
            minPlayersCriteria = (teamDemography[self.team1]>=self.teamParams['min']) and (teamDemography[self.team2]>=self.teamParams['min']) 
            
            maxPlayersCriteria = (teamDemography[self.team1]<=self.teamParams['max']) and (teamDemography[self.team2]<=self.teamParams['max'])
            
            if captain:
                [c, vc] = rnd.sample(selectedTeam, 2)   
                selectedTeam = [player + " (c)" if player==c else player + " (vc)" if player==vc else player for player in selectedTeam]
                
            
            if  pointsCriteria and uniqueTeamCriteria and minPlayersCriteria and maxPlayersCriteria:
                
                selectedTeams.append(selectedTeam)
                
                
                selected = selected + 1
                
                print("------------ Team", selected, "------------")
                for i in range(11):
                    print(str(i+1) +  '.', selectedTeam[i])
                
        return selectedTeams
    
    
