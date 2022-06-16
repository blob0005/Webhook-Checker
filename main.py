error = False
try:
    from os import system
    system("title " + "Webhook Checker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import requests
    import colorama
except:
    error = True
if error == True:
    while True:
        fix = input("Missing Module, Wanna Try Auto Fix (y/n): ")
        if fix == "y" or fix == "n":
            break
        else:
            print("Enter A Valid Choice")
    if fix == "n":
        exit()
    if fix == "y":
        try:
            import os
            os.system("pip install requests")
            os.system("pip install colorama")
            print("Problem May Be Fixed Now, Restart Prgoram")
            input("")
            exit()
        except:
            print("Error Fixing Error")
            input("")
            exit()
colorama.init(autoreset=True)
while True:
    type = input("""
1. Check Specific Webhook
2. Check Webhook(s) In Webhooks.txt
> """)
    if type == "1" or type == "2":
        break
    else:
        print("Enter A Valid Choice")
if type == "2":
    file = open("webhooks.txt", "r")
    webhooks = file.readlines()
    checked = []
    print("Press Enter To Start Checking")
    input("")
    for web in webhooks:
        try:
            if "\n" in web:
                web = web[:-1]
            r = requests.get(web)
            r = str(r)
            if "200" in r:
                print(colorama.Fore.GREEN + "Webhook Valid")
                checked.append(web)
            else:
                print(colorama.Fore.RED + "Webhook Invalid")
        except:
            print(colorama.Fore.RED + "Webhook Invalid")
    while True:
        save = input("Wanna Save Valid Webhooks To An Txt File (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    if save == "n":
        exit()
    if save == "y":
        for webik in checked:
            file = open("checked_webhooks.txt", "a")
            file.write(webik+"\n")
            file.close()
        print("Done Saving Webhook(s)")
        input("")
        exit()
if type == "1":
    while True:
            try:
                webhook = input("Enter Webhook: ")
                r_check = requests.get(webhook).json
                r_check = str(r_check)
                if "200" in r_check:
                    print(colorama.Fore.GREEN + "Webhook Valid")
                    while True:
                        main = input("Wanna Check Another Webhook (y/n): ")
                        if main == "y" or main == "n":
                            break
                        else:
                            print("Enter A Valid Choice")
                    if main == "y":
                        pass
                    if main == "n":
                        exit()
                if "200" not in r_check:
                    print(colorama.Fore.RED + "Webhook Invalid")
                    while True:
                        main = input("Wanna Check Another Webhook (y/n): ")
                        if main == "y" or main == "n":
                            break
                        else:
                            print("Enter A Valid Choice")
                    if main == "y":
                        pass
                    if main == "n":
                        exit()
            except Exception:
                print(colorama.Fore.RED + "Webhook Invalid")
                while True:
                    main = input("Wanna Check Another Webhook (y/n): ")
                    if main == "y" or main == "n":
                        break
                    else:
                        print("Enter A Valid Choice")
                if main == "y":
                    pass
                if main == "n":
                    exit()
