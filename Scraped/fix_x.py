import json
import os

files = os.listdir("gamedata")
gameData = {}

for file in files:
    jsonText = open("gamedata/"+file, "rb").read()
    jdata = json.loads(jsonText)
    name = list(jdata.keys())[0]
    gameData[name] = jdata[name]

for i in range(0,len(gameData["places"]["towns"])):
    gameData["places"]["towns"][i]["start_x"] -= 4
    gameData["places"]["towns"][i]["start_y"] -= 1
    gameData["places"]["towns"][i]["end_x"] -= 4
    gameData["places"]["towns"][i]["end_y"] -= 1

for i in range(0,len(gameData["places"]["zones"])):
    gameData["places"]["zones"][i]["start_x"] -= 4
    gameData["places"]["zones"][i]["start_y"] -= 1
    gameData["places"]["zones"][i]["end_x"] -= 4
    gameData["places"]["zones"][i]["end_y"] -= 1   
    
for i in range(0,len(gameData["places"]["areas"])):
    gameData["places"]["areas"][i]["start_x"] -= 4
    gameData["places"]["areas"][i]["start_y"] -= 1
    gameData["places"]["areas"][i]["end_x"] -= 4
    gameData["places"]["areas"][i]["end_y"] -= 1
    
for i in range(0,len(gameData["places"]["isles"])):
    gameData["places"]["isles"][i]["start_x"] -= 4
    gameData["places"]["isles"][i]["start_y"] -= 1
    gameData["places"]["isles"][i]["end_x"] -= 4
    gameData["places"]["isles"][i]["end_y"] -= 1
    
for i in range(0,len(gameData["places"]["waypoints"])):
    gameData["places"]["waypoints"][i]["pos_x"] -= 4
    gameData["places"]["waypoints"][i]["pos_y"] -= 1
    
for i in range(0,len(gameData["places"]["special_tiles"])):
    gameData["places"]["special_tiles"][i]["x"] -= 4
    gameData["places"]["special_tiles"][i]["y"] -= 1
    if gameData["places"]["special_tiles"][i]["code"] != None:
        kvp = gameData["places"]["special_tiles"][i]["code"].split("-")
        if len(kvp) >= 2:
            k = kvp[1].split(",")
            if len(k) == 2:
                code = "-".join([ kvp[0], ",".join([ str(int(k[0]) - 4), str(int(k[1]) - 1)]) ])
                gameData["places"]["special_tiles"][i]["code"] = code
    if gameData["places"]["special_tiles"][i]["exit_x"] != None:
        gameData["places"]["special_tiles"][i]["exit_x"] -= 4
    if gameData["places"]["special_tiles"][i]["exit_y"] != None:
        gameData["places"]["special_tiles"][i]["exit_y"] -= 1

for i in range(0,len(gameData["transport"]["transport_points"])):
    gameData["transport"]["transport_points"][i]["x"] -= 4
    gameData["transport"]["transport_points"][i]["y"] -= 1

for i in range(0,len(gameData["transport"]["transport_places"])):
    gameData["transport"]["transport_places"][i]["goto_x"] -= 4
    gameData["transport"]["transport_places"][i]["goto_y"] -= 1

for i in range(0,len(gameData["npc_list"])):
    gameData["npc_list"][i]["x"] -= 4
    gameData["npc_list"][i]["y"] -= 1
    if gameData["npc_list"][i]["udlr_start_x"] != None:
        gameData["npc_list"][i]["udlr_start_x"] -= 4
    if gameData["npc_list"][i]["udlr_start_y"] != None:
        gameData["npc_list"][i]["udlr_start_y"] -= 1
        
for i in range(0,len(gameData["quest_list"])):
    if gameData["quest_list"][i]["alt_activation"] != None:
        gameData["quest_list"][i]["alt_activation"]["x"] -= 4
        gameData["quest_list"][i]["alt_activation"]["y"] -= 1
    if gameData["quest_list"][i]["warp_x"] != None:
        gameData["quest_list"][i]["warp_x"] -= 4
    if gameData["quest_list"][i]["warp_y"] != None:
        gameData["quest_list"][i]["warp_y"] -= 1
        
for i in range(0,len(gameData["workshop"])):
    gameData["workshop"][i]["pos_x"] -= 4
    gameData["workshop"][i]["pos_y"] -= 1

for i in range(0,len(gameData["ranch"]["ranch_locations"])):
    gameData["ranch"]["ranch_locations"][i]["x"] -= 4
    gameData["ranch"]["ranch_locations"][i]["y"] -= 1

for i in range(0,len(gameData["ranch"]["ranch_locations"])):
    gameData["ranch"]["ranch_locations"][i]["x"] -= 4
    gameData["ranch"]["ranch_locations"][i]["y"] -= 1
    
gameData["messages"]["new_user"]["starting_x"] -= 4
gameData["messages"]["new_user"]["starting_y"] -= 1

gameData["messages"]["commands"]["mod_isle"]["x"] -= 4
gameData["messages"]["commands"]["mod_isle"]["y"] -= 1

gameData["messages"]["commands"]["rules_isle"]["x"] -= 4
gameData["messages"]["commands"]["rules_isle"]["y"] -= 1

gameData["messages"]["commands"]["prison_isle"]["x"] -= 4
gameData["messages"]["commands"]["prison_isle"]["y"] -= 1


for key in gameData.keys():
    os.makedirs("transrights", exist_ok=True)
    part = {}
    part[key] = gameData[key]
    open("transrights/" + key+".json", "w").write(json.dumps(part, indent=4))

#open("gamedata.json", "w").write(json.dumps(gameData))