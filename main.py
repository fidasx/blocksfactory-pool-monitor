import time
import os
from datetime import datetime
import requests
from termcolor import colored


os.system("cls")



def result():
    
    url = 'https://dgb-'+userinput.algo+'.theblocksfactory.com/api.php?api_key='
    r = requests.get(url+userinput.key)

    data = r.json()
    #time.sleep(0.1)

    red("---------------------------------------WORKERS-----------------------------------------------")

    for key, val in data["workers"].items():
        timestamp = datetime.fromtimestamp(int(val["last_share_timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
        result.worker = print(key.upper() + " |HASHRATE| " + colored(float(val["hashrate"])/1000, "green") +" |LAST SHARE| "+ colored(timestamp, 'green'))

    result.username = "USER: " + colored(data["username"], "green")
    result.confirmed = "CONFIRMED: " + colored(round(float(data["confirmed_rewards"])), "green")
    result.total = "TOTAL EARNED: " + colored(round(float(data["payout_history"])), "green")
    result.round_shares = "ROUND SHARES: " + colored(int(data["round_shares"]), "green")
    result.hashrate = "HASHRATE: " + colored(int(data["total_hashrate"])/1000, "green")

    red("---------------------------------------------------------------------------------------------")
    print("")

def red(text):
    return print(colored(text, "red"))


def printstats():
    red("----------------------------------------STATUS-----------------------------------------------")
    print(result.username)
    print(result.confirmed)
    print(result.hashrate)
    print(result.total)
    print(result.round_shares)
    red("---------------------------------------------------------------------------------------------")



def userinput():
    
    print(" please insert your api key from https://dgb-groestl.theblocksfactory.com/accountdetails \n" + "APIKEY:")
    userinput.key = input()
    
    if len(userinput.key) == 64:
        pass
    else:
        print("wrong key")
        quit()

    print("algorithm? example skein, groestl, qubit   etc...\n" +"ALGO:")
    userinput.algo = input() 

    algos=["skein", "groestl", "qubit"]
        
    if userinput.algo in algos:
        os.system("cls")
    else:
        print("wrong algo")
        quit()
       

    

userinput()




def update():

    while True:
        result()
        printstats()
        time.sleep(15)
        os.system("cls")

update()


