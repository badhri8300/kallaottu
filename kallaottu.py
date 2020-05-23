import subprocess
import re
import os
import time
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
os.system("clear")

def intro():



    prGreen("Starting TOR service") 
    
    time.sleep(2)



    prGreen("**CONNECTED TO A SECURE NETWORK**")


    time.sleep(3)
intro()

os.system("clear")


def banner():
 prRed("		 ____  __.   _____   .____     .____        _____   _______ ______________________ ____ ___  ")
prRed("			|    |/ _|  /  _  \  |    |    |    |      /  _  \  \   _  \\__    ___/\__    ___/|    |   \ ")
prRed("			|      <   /  /_\  \ |    |    |    |     /  /_\  \ /  /_\  \ |    |     |    |   |    |   / ")
prRed("			|    |  \ /    |    \|    |___ |    |___ /    |    \\  \_/   \|    |     |    |   |    |  /  ")
prRed("			|____|__ \\____|__  /|_______ \|_______ \\____|__  / \_____  /|____|     |____|   |______/   ")
prGreen("        		\/        \/         \/        \/        \/        \/                                ")

def user_input_clear():
    banner()
    user_input = str(input("\n\nCurl Wanted -- "))
    subprocess.call("clear", shell=True)
    banner()
    count = int(input("\n\nNumber of Votes -- "))
    subprocess.call("clear", shell=True)
    return user_input, count


def code_statement(user_input_first, count):
    i = 1
    c = 1
    b = 0
    banner()
    while i < count:
        i = i + 1
        print("Tor Service starting...")
        subprocess.call("service tor start", shell=True)
        subprocess.call("service tor reload", shell=True)
        user_input = subprocess.check_output("torsocks " + user_input_first, shell=True, stderr=subprocess.DEVNULL)
        checker = re.search(rb"\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w", user_input)
        checker_group = checker.group(0)
        choice_id = checker_group.decode("utf-8")
        status = '{"status"' + ":200," + '"data"' + ":{" + '"vote"' + ":true," + '"choiceIds"' + ":["'"' + choice_id + '"' + "]}}"
        decode_user_input = user_input.decode("utf-8")

        if decode_user_input == status:
            prGreen("Successful Votes -- " + str(c))
            c = c + 1

        elif decode_user_input != status:
            b = b + 1
            failed = "Failed Votes -- " + str(b)
            prRed(failed)




try:
    user_input, count = user_input_clear()
    code_statement(user_input, count)
except KeyboardInterrupt:
    prYellow("\nTor is stoping Service...")
    subprocess.call("service tor stop", shell=True)
