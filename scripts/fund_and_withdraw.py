# this has been created to interact with the smart contract
# added getEntrance() function in FundMe2.sol
from brownie import FundMe2
from scripts.helpful_scripts import get_account

# for funding...
def fund():
    fundMe2= FundMe2[-1]
    account= get_account()
    entrance_fee= fundMe2.getEntranceFee()    #since here calling a function with a return value so need not to deploy because i have made no change to smartcontract so what is have to deploy nothing!
    print("the fee to be payed for participation is: "+ str(entrance_fee))
    print("now funding...")
    fundMe2.fund({"from":account,"value":entrance_fee})    # since calling a function which is going to make a change in the state variable thus need to deploy this change to the blockchain so told the contract from which it has to be deployed

# first ran this command - 'brownie run scripts/deploy.py --network ganache-local'
# this was done because we changed our smartContract so we have to deploy the same change to testnet using ganache which will get stored on brownie since ganache-local is there in Ethereum network

# now to run the fund function we run command- 'brownie run scripts/fund_and_withdraw.py --network ganache-local'
# 
# for withdrawing...
def withdraw():
    fundMe2= FundMe2[-1]
    account= get_account()
    fundMe2.withdraw({"from":account})

def main():
    fund()
    withdraw()

# now to run the script we run command- 'brownie run scripts/fund_and_withdraw.py --network ganache-local'
# same Three line transaction information for both transactions were seen in terminal 

# made test_fund_me.py
