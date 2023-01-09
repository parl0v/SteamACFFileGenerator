import os
import re
import requests

start = 100
getGames = requests.get("https://store.steampowered.com/search/results/?query&count=100&dynamic_data=&sort_by=_ASC&ignore_preferences=1&category1=998&filter=topsellers&infinite=1")
gamesRegex = re.findall('https://store.steampowered.com/([^"]*)', getGames.text.replace("\\/", "/"))

try:
    os.mkdir(os.getcwd() + "/files/")
except:
    pass
    
def infinite(owner = None):
    global start
    global getGames
    global gamesRegex
    
    if owner != None:
        while True:
            for game in gamesRegex:
                try:
                    gameLink = game.strip().replace("apps/", "app/").split("app/")[1][:-1].split("/")
                except:
                    pass
                
                accountID = owner
                gameID = gameLink[0]
                gameName = gameLink[1].replace("_", " ")

                with open("files/appmanifest_" + gameID + ".acf", "w", encoding = "utf8", errors = "ignore") as file:
                    file.write('"AppState"\n{\n	"appid"		"' + gameID + '"\n	"Universe"		"1"\n	"LauncherPath"		"C:\\\Program Files (x86)\\\Steam\\\steam.exe"\n	"name"		"' + gameName + '"\n	"StateFlags"		"4"\n	"installdir"		"' + gameName + '"\n	"LastUpdated"		"0"\n	"SizeOnDisk"		"0"\n	"StagingSize"		"0"\n	"buildid"		"0"\n	"LastOwner"		"' + accountID + '"\n	"UpdateResult"		"0"\n	"BytesToDownload"		"0"\n	"BytesDownloaded"		"0"\n	"BytesToStage"		"0"\n	"BytesStaged"		"0"\n	"TargetBuildID"		"0"\n	"AutoUpdateBehavior"		"0"\n	"AllowOtherDownloadsWhileRunning"		"0"\n	"ScheduledAutoUpdate"		"0"\n	"InstalledDepots"\n	{\n		"' + str(int(gameID) + 1) + '"\n		{\n			"manifest"		"0"\n			"size"		"0"\n		}\n	}\n	"UserConfig"\n	{\n		"language"		"english"\n	}\n	"MountedConfig"\n	{\n		"language"		"english"\n	}\n}')
                print("done | " + gameName)
            start = start + 100
            getGames = requests.get("https://store.steampowered.com/search/results/?query&start=" + str(start) + "&count=100&dynamic_data=&sort_by=_ASC&ignore_preferences=1&category1=998&filter=topsellers&infinite=1")
            gamesRegex = re.findall('https://store.steampowered.com/([^"]*)', getGames.text.replace("\\/", "/"))
    
    elif owner == None:
        while True:
            for game in gamesRegex:
                try:
                    gameLink = game.strip().replace("apps/", "app/").split("app/")[1][:-1].split("/")
                except:
                    pass
                gameID = gameLink[0]
                gameName = gameLink[1].replace("_", " ")

                with open("files/appmanifest_" + gameID + ".acf", "w", encoding = "utf8", errors = "ignore") as file:
                    file.write('"AppState"\n{\n	"appid"		"' + gameID + '"\n	"Universe"		"1"\n	"LauncherPath"		"C:\\\Program Files (x86)\\\Steam\\\steam.exe"\n	"name"		"' + gameName + '"\n	"StateFlags"		"4"\n	"installdir"		"' + gameName + '"\n	"LastUpdated"		"0"\n	"SizeOnDisk"		"0"\n	"StagingSize"		"0"\n	"buildid"		"0"\n	"LastOwner"		"0"\n	"UpdateResult"		"0"\n	"BytesToDownload"		"0"\n	"BytesDownloaded"		"0"\n	"BytesToStage"		"0"\n	"BytesStaged"		"0"\n	"TargetBuildID"		"0"\n	"AutoUpdateBehavior"		"0"\n	"AllowOtherDownloadsWhileRunning"		"0"\n	"ScheduledAutoUpdate"		"0"\n	"InstalledDepots"\n	{\n		"' + str(int(gameID) + 1) + '"\n		{\n			"manifest"		"0"\n			"size"		"0"\n		}\n	}\n	"UserConfig"\n	{\n		"language"		"english"\n	}\n	"MountedConfig"\n	{\n		"language"		"english"\n	}\n}')
                print("done | " + gameName)
            start = start + 100
            getGames = requests.get("https://store.steampowered.com/search/results/?query&start=" + str(start) + "&count=100&dynamic_data=&sort_by=_ASC&ignore_preferences=1&category1=998&filter=topsellers&infinite=1")
            gamesRegex = re.findall('https://store.steampowered.com/([^"]*)', getGames.text.replace("\\/", "/"))
         
def specific(owner = None):
    if owner != None:
        gameLink = input("game link: ").strip().split("app/")[1][:-1].split("/") # example: https://store.steampowered.com/app/629760/MORDHAU/
        accountID = ownerID
        gameID = gameLink[0]
        gameName = gameLink[1].replace("_", " ")

        with open("files/appmanifest_" + gameID + ".acf", "a", encoding = "utf8", errors = "ignore") as file:
            file.write('"AppState"\n{\n	"appid"		"' + gameID + '"\n	"Universe"		"1"\n	"LauncherPath"		"C:\\\Program Files (x86)\\\Steam\\\steam.exe"\n	"name"		"' + gameName + '"\n	"StateFlags"		"4"\n	"installdir"		"' + gameName + '"\n	"LastUpdated"		"0"\n	"SizeOnDisk"		"0"\n	"StagingSize"		"0"\n	"buildid"		"0"\n	"LastOwner"		"' + accountID + '"\n	"UpdateResult"		"0"\n	"BytesToDownload"		"0"\n	"BytesDownloaded"		"0"\n	"BytesToStage"		"0"\n	"BytesStaged"		"0"\n	"TargetBuildID"		"0"\n	"AutoUpdateBehavior"		"0"\n	"AllowOtherDownloadsWhileRunning"		"0"\n	"ScheduledAutoUpdate"		"0"\n	"InstalledDepots"\n	{\n		"' + str(int(gameID) + 1) + '"\n		{\n			"manifest"		"0"\n			"size"		"0"\n		}\n	}\n	"UserConfig"\n	{\n		"language"		"english"\n	}\n	"MountedConfig"\n	{\n		"language"		"english"\n	}\n}')
        print("done generating")
    
    elif owner == None:
        gameLink = input("game link: ").strip().split("app/")[1][:-1].split("/") # example: https://store.steampowered.com/app/629760/MORDHAU/
        gameID = gameLink[0]
        gameName = gameLink[1].replace("_", " ")

        with open("files/appmanifest_" + gameID + ".acf", "a", encoding = "utf8", errors = "ignore") as file:
            file.write('"AppState"\n{\n	"appid"		"' + gameID + '"\n	"Universe"		"1"\n	"LauncherPath"		"C:\\\Program Files (x86)\\\Steam\\\steam.exe"\n	"name"		"' + gameName + '"\n	"StateFlags"		"4"\n	"installdir"		"' + gameName + '"\n	"LastUpdated"		"0"\n	"SizeOnDisk"		"0"\n	"StagingSize"		"0"\n	"buildid"		"0"\n	"LastOwner"		"0"\n	"UpdateResult"		"0"\n	"BytesToDownload"		"0"\n	"BytesDownloaded"		"0"\n	"BytesToStage"		"0"\n	"BytesStaged"		"0"\n	"TargetBuildID"		"0"\n	"AutoUpdateBehavior"		"0"\n	"AllowOtherDownloadsWhileRunning"		"0"\n	"ScheduledAutoUpdate"		"0"\n	"InstalledDepots"\n	{\n		"' + str(int(gameID) + 1) + '"\n		{\n			"manifest"		"0"\n			"size"		"0"\n		}\n	}\n	"UserConfig"\n	{\n		"language"		"english"\n	}\n	"MountedConfig"\n	{\n		"language"		"english"\n	}\n}')
        print("done generating")

try:
    print("\n[ https://github.com/parl0v | Steam .acf file generator ]")
    print("place the files into your steamapps folder and relaunch steam\n")

    print("options: infinite, specific")
    options = ["infinite", "specific"]
    selectedOption = input("option:  ").strip()  

    if selectedOption not in options:
        print("not an option")
        exit()
        
    else:
        print("\ninclude/spoof owner? (y/n)")
        includeOwner = input("have owner: ").strip()
        print()

        if includeOwner == "y":
            ownerID = input("owner id: ").strip()
            if selectedOption == "infinite":
                infinite(ownerID)
            
            elif selectedOption == "specific":
                specific(ownerID)
            
            else:
                print("not an option")
                exit()
            
        elif includeOwner == "n":
            if selectedOption == "infinite":
                infinite()
            
            elif selectedOption == "specific":
                specific()
            
            else:
                print("not an option")
                exit()

        else:
            print("not an option")
            exit()
            
except KeyboardInterrupt:
    print("\nthanks for using the script, goodbye.")
    exit()