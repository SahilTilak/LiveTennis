import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_live_scores(url):
    scores = pd.DataFrame()
    gamescore =[]
    name = []
    set1 = []
    set2 = []
    set3 = []
    set4 = []
    set5 = []
    set1tb = []
    set2tb =[]
    set3tb = []
    set4tb = []
    set5tb = []
    server =[]
    response = requests.get(url)
    data = response.json()
    for tourn in data['liveScores']['Tournaments']:
        tourn_name = tourn['Name']
        for match in tourn['Matches']:
            if(match['TeamOne']['PlayerTwoName'] == " "):
                if(match['Status'] == "F"):
                    continue
                best_of = match['NumberOfSets']
                match_time = match['MatchTime']
                status = match['MatchInfo']
                name.append((match['TeamOne']['PlayerNameForUrl'].split("-")[0] + " " + match['TeamOne']['PlayerNameForUrl'].split("-")[1]))
                name.append((match['TeamTwo']['PlayerNameForUrl'].split("-")[0] + " " + match['TeamTwo']['PlayerNameForUrl'].split("-")[1]))
                round_num = match['RoundTitle'].split("-")[0].strip()
                court = match['RoundTitle'].split("-")[1].strip()
                p1_totalset = 0
                p2_totalset =0 
                if(match['LastServer'] == "0"):
                    server.append('0')
                    server.append('1')
                else:
                    server.append('1')
                    server.append('0')
                gamescore.append(match['TeamOne']['Scores']['CurrentScore'])
                gamescore.append(match['TeamTwo']['Scores']['CurrentScore'])
                set1.append(match['TeamOne']['Scores']['SetOne'])
                set1.append(match['TeamTwo']['Scores']['SetOne'])
                set2.append(match['TeamOne']['Scores']['SetTwo'])
                set2.append(match['TeamTwo']['Scores']['SetTwo'])
                set3.append(match['TeamOne']['Scores']['SetThree'])
                set3.append(match['TeamTwo']['Scores']['SetThree'])
                if(match['TeamOne']['Scores']['SetOneTiebreak'] != None):
                    set1tb.append("(" + str(int(match['TeamOne']['Scores']['SetOneTiebreak'])) + ")")
                    set1tb.append("(" + str(int(match['TeamOne']['Scores']['SetOneTiebreak']) + 2) + ")")
                elif(match['TeamTwo']['Scores']['SetOneTiebreak'] != None):
                    set1tb.append("(" + str(int(match['TeamTwo']['Scores']['SetOneTiebreak']) + 2) + ")")
                    set1tb.append("(" + str(int(match['TeamTwo']['Scores']['SetOneTiebreak'])) + ")")
                else:
                    set1tb.append(match['TeamOne']['Scores']['SetOneTiebreak'])
                    set1tb.append(match['TeamTwo']['Scores']['SetOneTiebreak'])
                if(match['TeamOne']['Scores']['SetTwoTiebreak'] != None):
                    set2tb.append("(" + str(int(match['TeamOne']['Scores']['SetTwoTiebreak'])) + ")")
                    set2tb.append("(" + str(int(match['TeamOne']['Scores']['SetTwoTiebreak']) + 2) + ")")
                elif(match['TeamTwo']['Scores']['SetTwoTiebreak'] != None):
                    set2tb.append("(" + str(int(match['TeamTwo']['Scores']['SetTwoTiebreak']) + 2) + ")")
                    set2tb.append("(" + str(int(match['TeamTwo']['Scores']['SetTwoTiebreak'])) + ")")
                else:
                    set2tb.append(match['TeamOne']['Scores']['SetTwoTiebreak'])
                    set2tb.append(match['TeamTwo']['Scores']['SetTwoTiebreak'])
                if(match['TeamOne']['Scores']['SetThreeTiebreak'] != None):
                    set3tb.append("(" + str(int(match['TeamOne']['Scores']['SetThreeTiebreak'])) + ")")
                    set3tb.append("(" + str(int(match['TeamOne']['Scores']['SetThreeTiebreak']) + 2) + ")")
                elif(match['TeamTwo']['Scores']['SetTwoTiebreak'] != None):
                    set3tb.append("(" + str(int(match['TeamTwo']['Scores']['SetThreeTiebreak']) + 2) + ")")
                    set3tb.append("(" + str(int(match['TeamTwo']['Scores']['SetThreeTiebreak'])) + ")")
                else:
                    set3tb.append(match['TeamOne']['Scores']['SetThreeTiebreak'])
                    set3tb.append(match['TeamTwo']['Scores']['SetThreeTiebreak'])
                if(best_of == 3):
                    set4.append(None)
                    set4.append(None)
                    set4tb.append(None)
                    set4tb.append(None)
                    set5.append(None)
                    set5.append(None)
                    set5tb.append(None)
                    set5tb.append(None)
                    continue
                set4.append(match['TeamOne']['Scores']['SetFour'])
                set4.append(match['TeamTwo']['Scores']['SetFour'])
                set5.append(match['TeamOne']['Scores']['SetFive'])
                set5.append(match['TeamTwo']['Scores']['SetFive'])
                if(match['TeamOne']['Scores']['SetFourTiebreak'] != None):
                    set4tb.append("(" + str(int(match['TeamOne']['Scores']['SetFourTiebreak'])) + ")")
                    set4tb.append("(" + str(int(match['TeamOne']['Scores']['SetFourTiebreak']) + 2) + ")")
                elif(match['TeamTwo']['Scores']['SetTwoTiebreak'] != None):
                    set4tb.append("(" + str(int(match['TeamTwo']['Scores']['SetFourTiebreak']) + 2) + ")")
                    set4tb.append("(" + str(int(match['TeamTwo']['Scores']['SetFourTiebreak'])) + ")")
                else:
                    set4tb.append(match['TeamOne']['Scores']['SetFourTiebreak'])
                    set4tb.append(match['TeamTwo']['Scores']['SetFourTiebreak'])
                if(match['TeamOne']['Scores']['SetFiveTiebreak'] != None):
                    set5tb.append("(" + str(int(match['TeamOne']['Scores']['SetFiveTiebreak'])) + ")")
                    set5tb.append("(" + str(int(match['TeamOne']['Scores']['SetFiveTiebreak']) + 2) + ")")
                elif(match['TeamTwo']['Scores']['SetFiveTiebreak'] != None):
                    set5tb.append("(" + str(int(match['TeamTwo']['Scores']['SetFiveTiebreak']) + 2) + ")")
                    set5tb.append("(" + str(int(match['TeamTwo']['Scores']['SetFiveTiebreak'])) + ")")
                else:
                    set5tb.append(match['TeamOne']['Scores']['SetFiveTiebreak'])
                    set5tb.append(match['TeamTwo']['Scores']['SetFiveTiebreak'])



                
                
#                 if(((p1_set1 == 6) & (p1_set1 - p2_set1 > 1)) | p1_set1 == 7):
#                     p1_totalset = p1_totalset + 1
#                 if(((p2_set1 == 6) & (p2_set1 - p1_set1 > 1)) | p2_set1 == 7):
#                     p2_totalset = p2_totalset + 1
#                 if(((p1_set2 == 6) & (p1_set2 - p2_set2 > 1)) | p1_set2 == 7):
#                     p1_totalset = p1_totalset + 1
#                 if(((p1_set2 == 6) & (p1_set2 - p2_set2 > 1)) | p1_set2 == 7):
#                     p1_totalset = p1_totalset + 1
#                 if(((p2_set2 == 6) & (p2_set2 - p1_set2 > 1)) | p2_set2 == 7):
#                     p2_totalset = p2_totalset + 1
#                 if(((p1_set3 == 6) & (p1_set3 - p2_set3 > 1)) | p1_set3 == 7):
#                     p1_totalset = p1_totalset + 1
#                 if(((p2_set3 == 6) & (p2_set3 - p1_set3 > 1)) | p2_set3 == 7):
#                     p2_totalset = p2_totalset + 1
#                 if(((p1_set4 == 6) & (p1_set4 - p2_set4 > 1)) | p1_set4 == 7):
#                     p1_totalset = p1_totalset + 1
#                 if(((p2_set4 == 6) & (p2_set4 - p1_set4 > 1)) | p2_set4 == 7):
#                     p2_totalset = p2_totalset + 1
#                 if(((p1_set5 == 6) & (p1_set5 - p2_set5 > 1)) | p1_set5 == 7):
#                     p1_totalset = p1_totalset + 1
#                 if(((p2_set5 == 6) & (p2_set5 - p1_set5 > 1)) | p2_set5 == 7):
#                     p2_totalset = p2_totalset + 1)

    scores['gamescore'] = gamescore
    scores['server'] = server
    scores['name'] = name
    scores['set1'] = set1
    scores['set2'] = set2
    scores['set3'] = set3
    scores['set4'] = set4
    scores['set5'] = set5
    scores['set1tb'] = set1tb
    scores['set2tb'] = set2tb
    scores['set3tb'] = set3tb
    scores['set4tb'] = set4tb
    scores['set5tb'] = set5tb

    scores= scores.fillna(value="")
    scores = scores.astype(str)
    return(scores)
     
    
        