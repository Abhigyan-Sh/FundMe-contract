from brownie import network,accounts,config,MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT= ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT= ["development", "ganache-local"]   # development, Ethereum networks

# def get_account():
#     if network.show_active !="development":
#         return accounts[0]
#     else:
#         return accounts.add(config["wallets"]["from_key"])

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]                 # for brownie accounts & the account which we made using ganache rpc server url and rinkeby testnet chainId and added to Ethereum networks of brownie so as brownie remembers it and keeps as control version in chainId folder   --used brownie account
    else:
        return accounts.add(config["wallets"]["from_key"])
# for testnet used rinkneby account


# with deploy3 downwards
DECIMALS= 8
STARTING_PRICE= 200000000000

def deploy_mocks():
    print(f"the active netwokr is {network.show_active()}")
    print("deploying mocks...")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{"from":get_account()}) 
    print("mocks deployed!!!")
