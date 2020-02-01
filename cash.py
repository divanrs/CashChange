"""
    ******************************************************************************
    Decriptive Name: Cash Change Coints Calcultator 
    File Name: cash.py

    Autor: Diego Ivan Rodriguez Sanchez
    Created at: 01/02/2020

    Description:
        Source code program for that calculates the minimum number of coins 
        required to give a user change.

    Classes:
        - cashOperations()
            Functions:
                - __init__(self, availableCoins)
                    class contructor that get by parameter availableCoins set types
                    for operations
                - getChange(self, itemCost, changeCash)
                    proccess section that get by parameter itemCost and changeCash
                    for calculate in set of coins to return change to client
               
    Functions:
        - main():
            Entry point of execution application, Get Input From Keyboard Section
            and Instance cashOperations class and Call Mathod Function to getChange

    Relevant Modifications:
        Autor:
        Date:
        Details:

"""

import os

#----------------------------------------------------------cashOperations() Class
class cashOperations():
    availableCoins = []
  
    def __init__(self, availableCoins):
        self.availableCoins = availableCoins

    def getChange(self, itemCost, changeCash):     
       
        self.availableCoins.sort()
        self.availableCoins.reverse()

        #----------------------------------------------Proccess Section
        changeCoins = []
        for availableCoin in self.availableCoins:
            while( changeCash.__round__(4) - availableCoin >= 0 ):
                changeCoins.append(availableCoin)
                changeCash -= availableCoin
            
        return changeCoins

#-----------------------------------------------------------main() Function
def main():
    availableCoins = [0.10, 0.05, 0.25, 0.01]
    itemCost = 0.25

    #----------------------------------------------Get Input From Keyboard Section
    while(True):
        try:
            changeCash = float(input())
            while( changeCash - itemCost < 0 ):
                changeCash = float(input())
            break
        except:
            None
        
    #-------------------Instance cashOperations class and Call Mathod Function to getChange
    cashOperationObject = cashOperations(availableCoins)
    changeCoins = cashOperationObject.getChange(itemCost, changeCash)
    print( len(changeCoins) )

if __name__ == '__main__':
    main()
