# -*- coding: utf-8 -*-
"""
Created on January 9 2019

@author: Alexi
"""

###This class contains backend information for the game

#The universe (known and unknown) consists of systems
#  Each system has a unique numeric ID
#  The starting sector "Sol" has the numeric ID 0
#  Each system has a randomly generated resource value, indicating the amount and type of resources it can produce each turn.

#The universe is inhabited by civilizations
#  With the notable exception of the Terran Federation, players will have the opportunity to provide the English names for
#  civilizations they encounter.

#Systems are connected by warp gates
#  At the start of the game, no warp gates exist. Players may build them.
#  A newly built warp gate connects to a random system - the system is more likely to be close in system number to the
#  system the gate is built from, but longer jumps are certainly possible.
#
#  In order to traverse a new warp gate, it must first be "charted". Each gate requires a sequence of material inputs.
#  These inputs are not revealed in advance, and may include any materials - including materials players cannot yet access.
#  The longer the jump and the higher the system number (in absolute value), the likelier it is that higher value resources,
#  more complex combinations of resources, or simply more sequential inputs might be required.
#
#  Once a player has charted a warp gate, for the remainder of the game they know the set of required inputs to traverse that
#  gate, even if the set of required inputs changes. (Players may potentially add or remove inputs.)
#
#  It is expensive to open additional warp gates out of the same system. Any resources may be used to create a new warp gate,
#  but the total resource cost is equal to the number of extant gates connected to that system. This includes
#    Any gates *from* that system (charted or uncharted)
#    Any gates *to* that system which have been charted by at least one player
#  A gate to system X that has not been charted by the current player will appear to that player as an uncharted gate from
#  system X.

from numpy import random #Used for random.geometric(p=?,size=?)
from numpy import log2 #Used for randomization
from collections import defaultdict

class Civilization():
  def __init__(self,idnum,name):
    self.idnum = idnum
    self.name = name

class System():
  def __init__(self,idnum,name):
    self.idnum = idnum
    self.name = name

    #Generate system resource potential
    #Number of rolls equal to abs(idnum)
    self.resources = defaultdict(int)
    draws = random.geometric(p=0.5,size=int(log2(abs(idnum))))
    for x in draws:
      if x>1:
        self.resources[x-1]+=1

    #Generate gates list
    self.gates = []

class WarpGate():
  def __init__(self,source):
    self.source = source #System idnum
    distance = random.geometric(p=0.2,size=1) #At present, all warp gates go FORWARD
    self.destination = source+distance[0]

    #Determine the initial sequence
    self.chart_sequence = []
    draws = random.geometric(p=0.5,size=int(log2(distance)+log2(abs(self.destination))))
    #TODO

class Shard():
  def __init__(self):
    self.universe = {}
    self.universe[0] = System(0,"Sol")
    self.civs = []
    self.civs.append(Civilization(0,"Terran Federation"))
