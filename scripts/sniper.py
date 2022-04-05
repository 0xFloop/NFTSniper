from brownie import Contract,accounts
from brownie.network.gas.strategies import GasNowStrategy
import json, requests, time


def main():
    #input metadata URI link from contract
    metadataAPI = ""

    contractAddress = ""

    #input max collection supply
    MAX_SUPPLY = 

    #input desireable trait names
    rareTraits = ["","",""]

    #input array of desireable number of traits EX. [4, 11, 12]
    desireableNumOfTraits = [] 

    contractABI = json.load(open("interfaces/contractABI.json"))

    #input nft price in wei
    price = 

    contract = Contract.from_abi("Contract",contractAddress, contractABI)

    dev = accounts.load('dev')
    
    nextNFTNumber = contract.totalSupply()+1

    desireableNFTs = []



    for i in range(nextNFTNumber, MAX_SUPPLY):
        try:
            response_API_1 = requests.get(metadataAPI+str(i)).json()["attributes"]

            numOfTraits = len(response_API_1) 

            if numOfTraits in desireableNumOfTraits:
                desireableNFTs.append(i)
            else:
                for j in range(0, numOfTraits):
                    if all(response_API_1[j]['value'] in x for x in rareTraits):
                        desireableNFTs.append(i)
        except Exception as error:
            print(error)

    print(desireableNFTs)


    while True:
        gas_strategy = GasNowStrategy("fast")

        nextNFTNumber = contract.totalSupply()+1


        try:

            if(nextNFTNumber in desireableNFTs):
                contract.mint(1, {"from": dev, "amount": price, "gas_price": gas_strategy})
                print("minting 1")
            
            if(nextNFTNumber+1 in desireableNFTs):
                contract.mint(2,{"from": dev, "amount": price*2, "gas_price": gas_strategy})
                print("minting 2")

            if(nextNFTNumber+2 in desireableNFTs):
                contract.mint(3,{"from": dev, "amount": price*3, "gas_price": gas_strategy})
                print("minting 3")

            if(nextNFTNumber+3 in desireableNFTs):
                contract.mint(4,{"from": dev, "amount": price*4, "gas_price": gas_strategy})
                print("minting 4")
            
            if(nextNFTNumber+4 in desireableNFTs):
                contract.mint(5,{"from": dev, "amount": price*5, "gas_price": gas_strategy})
                print("minting 5")

        except Exception as error:
            print(error)
        time.sleep(1)




