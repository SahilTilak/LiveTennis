from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from func import get_live_scores
from wpmodel import matchProb

scores = get_live_scores("https://www.atptour.com/-/ajax/Scores/GetInitialScores")
scores_challenger = get_live_scores("https://www.atptour.com/-/ajax/Scores/GetInitialChallengerScores")
scores = scores.append(scores_challenger)
print(scores)
scores['Game Score'] = scores['gamescore']
scores['Set 1'] = scores['set1'] + scores['set1tb']
scores['Set 2'] =scores['set2'] + scores['set2tb']
scores['Set 3'] = scores['set3'] + scores['set3tb']
scores['Set 4'] = scores['set4'] + scores['set4tb']
scores['Set 5'] =scores['set5'] + scores['set5tb']
rest = scores[['Game Score', 'Set 1', 'Set 2', 'Set 3', 'Set 4', 'Set 5']]
app = Flask(__name__)

@app.route("/")
def base():
    return render_template("scores.html", len = (len(scores['name'])) // 2, name = scores['name'],server = list(scores['server']), gm = scores['Game Score'], set1 = scores['Set 1'], set2 = scores['Set 2'], set3 = scores['Set 3'], set4 = scores['Set 4'], set5 = scores['Set 5'])

if __name__ == "__main__":
    app.run(port = 10000, debug = True)