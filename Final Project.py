"""
Jasmandeep Kaur
COMP 162 - Final Project
Final Project.py
"""

"""
Columns in the Data:
    Name - name of each video game
    Platform - the console(Xbox, PS, PC, Nintendo, etc.) the game is played on
    Year_of_Release - the year the game  was released
    Genre - the genre of the game
    Publisher - the publisher of the game
    NA_Sales - sales made in North America
    EU_Sales - sales made in the European Union
    JP_Sales - sales made in Japan
    Other_Sales - sales made in all other regions that do not include North America, the European Union, and Japan
    Global_Sales - total number of sales or sales made globally, covering all regions
    Critic_Score - average of scores given by critics (source:MetaCritic)
    Critic_Count - the number of critics that gave the game a score (source:MetaCritic)
    User_Score - average of scores given by users (source:MetaCritic)
    User_Count - the number of users that gave the game a score (source:MetaCritic)
    Developer - the developer of the game
    Rating - the rating given by the Entertainment Software Rating Board (ESRB) 
    Average_Score - the critic and user score are added and divided by 2 for each game
"""
"""
In this project, I used Decision Trees where the outcome was determined through the probabiliy of 
an outcome over the totale number of outcomes. 
"""
import pandas as pd
from prettytable import PrettyTable

def computingProbs(Data):
    countNA = 0
    countEU = 0
    countJP = 0
    countOthers = 0
    NA = []
    EU = []
    JP = []
    Others = []
    for valueNA in Data["NA_Sales"]:
        NA.append(valueNA)
    for valueEU in Data["EU_Sales"]:
        EU.append(valueEU)
    for valueJP in Data["JP_Sales"]:
        JP.append(valueJP)
    for valueOthers in Data["Other_Sales"]:
        Others.append(valueOthers)
    for i in range(0, len(NA)):
        if NA[i] > EU[i] and NA[i] > JP[i] and NA[i] > Others[i]:
            countNA = countNA +1
        elif EU[i] > NA[i] and EU[i] > JP[i] and EU[i] > Others[i]:
            countEU = countEU +1
        elif JP[i] > NA[i] and JP[i] > EU[i] and JP[i] > Others[i]:
            countJP = countJP +1
        elif Others[i] > NA[i] and Others[i] > EU[i] and Others[i] > JP[i]:
            countOthers = countOthers +1
    if countNA > countEU and countNA > countJP and countNA > countOthers:
        return "North America"
    elif countEU > countNA and countEU > countJP and countEU > countOthers:
        return "European Union"
    elif countJP > countNA and countJP > countEU and countJP > countOthers:
        return "Japan"
    elif countOthers > countNA and countOthers > countEU and countOthers > countJP:
        return "Other Regions"
     
def cleaningData(Data):
    Data = Data[Data.Year_of_Release > 2010]
    Data = Data.dropna(how='any')
    indexNames = Data[Data['User_Score'] == 'tbd' ].index
    Data.drop(indexNames , inplace=True)
    indexNames = Data[Data['Rating'] == 'RP' ].index
    Data.drop(indexNames , inplace=True)
    Data['User_Score'] = (Data['User_Score']).astype(float)
    Data['Critic_Score'] = (Data['Critic_Score']/10)
    sumof2 = (Data['Critic_Score'] + Data['User_Score'])
    averages = ((sumof2) /2)
    Data['Average_Score'] = averages
    return Data

    
def computingScoreGenreProb(Data,salesType, genre):
    countYes = 0
    countNo = 0
    genrecount = 0
    sales = []
    genres = []
    score = []
    NA = []
    EU = []
    JP = []
    Others = []
    
    for valueNA in Data["NA_Sales"]:
        NA.append(valueNA)
    for valueEU in Data["EU_Sales"]:
        EU.append(valueEU)
    for valueJP in Data["JP_Sales"]:
        JP.append(valueJP)
    for valueOthers in Data["Other_Sales"]:
        Others.append(valueOthers)
    for value in Data[salesType]:
        sales.append(value)
    for value in Data["Genre"]:
        genres.append(value)
    for value in Data["Average_Score"]:
        score.append(value)
    if salesType == "NA_Sales":
        for i in range(0, len(sales)):
            if genres[i] == genre and score[i] >= 7 and NA[i] > EU[i] and NA[i] > JP[i] and NA[i] > Others[i]:
                countYes = countYes +1
                genrecount = genrecount +1
            elif genres[i] == genre and score[i] < 7 and NA[i] > EU[i] and NA[i] > JP[i] and NA[i] > Others[i]:
                countNo = countNo +1
                genrecount = genrecount +1
    elif salesType == "EU_Sales":
        for i in range(0, len(sales)):
            if genres[i] == genre and score[i] >= 7 and EU[i] > NA[i] and EU[i] > JP[i] and EU[i] > Others[i]:
                countYes = countYes +1
                genrecount = genrecount +1
            elif genres[i] == genre and score[i] < 7 and EU[i] > NA[i] and EU[i] > JP[i] and EU[i] > Others[i]:
                countNo = countNo +1
                genrecount = genrecount +1
    elif salesType == "JP_Sales":
        for i in range(0, len(sales)):
            if genres[i] == genre and score[i] >= 7 and JP[i] > NA[i] and JP[i] > EU[i] and JP[i] > Others[i]:
                countYes = countYes +1
                genrecount = genrecount +1
            elif genres[i] == genre and score[i] < 7 and JP[i] > NA[i] and JP[i] > EU[i] and JP[i] > Others[i]:
                countNo = countNo +1
                genrecount = genrecount +1
    elif salesType == "Other_Sales":
        for i in range(0, len(sales)):
            if genres[i] == genre and score[i] >= 7 and Others[i] > NA[i] and Others[i] > EU[i] and Others[i] > JP[i]:
                countYes = countYes +1
                genrecount = genrecount +1
            elif genres[i] == genre and score[i] < 7 and Others[i] > NA[i] and Others[i] > EU[i] and Others[i] > JP[i]:
                countNo = countNo +1
                genrecount = genrecount +1
    if countYes > countNo:
        return ("Yes: " + str(countYes) +"/" + str(genrecount))
    elif countYes < countNo:
        return ("No: " +str(countNo) +"/" +str(genrecount))
    
def computingScoreRatingProb(Data,salesType, rating):
    countYes = 0
    countNo = 0
    sales = []
    ratings = []
    score = []
    ratingcount = 0
    NA = []
    EU = []
    JP = []
    Others = []
    for valueNA in Data["NA_Sales"]:
        NA.append(valueNA)
    for valueEU in Data["EU_Sales"]:
        EU.append(valueEU)
    for valueJP in Data["JP_Sales"]:
        JP.append(valueJP)
    for valueOthers in Data["Other_Sales"]:
        Others.append(valueOthers)
    for value in Data[salesType]:
        sales.append(value)
    for value in Data["Rating"]:
        ratings.append(value)
    for value in Data["Average_Score"]:
        score.append(value)
    if salesType == "NA_Sales":
        for i in range(0, len(sales)):
            if ratings[i] == rating and score[i] >= 7 and NA[i] > EU[i] and NA[i] > JP[i] and NA[i] > Others[i]:
                countYes = countYes +1
                ratingcount = ratingcount +1
            elif ratings[i] == rating and score[i] < 7 and NA[i] > EU[i] and NA[i] > JP[i] and NA[i] > Others[i]:
                countNo = countNo +1
                ratingcount = ratingcount +1
    elif salesType == "EU_Sales":
        for i in range(0, len(sales)):
            if ratings[i] == rating and score[i] >= 7 and EU[i] > NA[i] and EU[i] > JP[i] and EU[i] > Others[i]:
                countYes = countYes +1
                ratingcount = ratingcount +1
            elif ratings[i] == rating and score[i] < 7 and EU[i] > NA[i] and EU[i] > JP[i] and EU[i] > Others[i]:
                countNo = countNo +1
                ratingcount = ratingcount +1
    elif salesType == "JP_Sales":
        for i in range(0, len(sales)):
            if ratings[i] == rating and score[i] >= 7 and JP[i] > NA[i] and JP[i] > EU[i] and JP[i] > Others[i]:
                countYes = countYes +1
                ratingcount = ratingcount +1
            elif ratings[i] == rating and score[i] < 7 and JP[i] > NA[i] and JP[i] > EU[i] and JP[i] > Others[i]:
                countNo = countNo +1
                ratingcount = ratingcount +1
    elif salesType == "Other_Sales":
        for i in range(0, len(sales)):
            if ratings[i] == rating and score[i] >= 7 and Others[i] > NA[i] and Others[i] > EU[i] and Others[i] > JP[i]:
                countYes = countYes +1
                ratingcount = ratingcount +1
            elif ratings[i] == rating and score[i] < 7 and Others[i] > NA[i] and Others[i] > EU[i] and Others[i] > JP[i]:
                countNo = countNo +1
                ratingcount = ratingcount +1
    if countYes > countNo:
        return ("Yes: " + str(countYes) +"/" + str(ratingcount))
    elif countYes < countNo:
        return ("No: " +str(countNo) +"/" +str(ratingcount))
    
def main():
    data = pd.read_csv("vgs1.csv")
    data = cleaningData(data)
    
    table = PrettyTable()
    table.field_names = ["Region with Most Sales", "Genre", "Decision: Is the Average Score greater than or equal to 7?"]
    table.add_row(["North America","Sports", computingScoreGenreProb(data, "NA_Sales","Sports")])
    table.add_row(["","Misc", computingScoreGenreProb(data,"NA_Sales", "Misc")])
    table.add_row(["","Puzzle", computingScoreGenreProb(data, "NA_Sales","Puzzle")])
    table.add_row(["","Platform", computingScoreGenreProb(data,"NA_Sales", "Platform")])
    table.add_row(["","Adventure", computingScoreGenreProb(data,"NA_Sales", "Adventure")])
    table.add_row(["","Action", computingScoreGenreProb(data, "NA_Sales","Action")])
    table.add_row(["","Role-Playing", computingScoreGenreProb(data, "NA_Sales","Role-Playing")])
    table.add_row(["","Shooter", computingScoreGenreProb(data, "NA_Sales","Shooter")])
    table.add_row(["","Fighting",  computingScoreGenreProb(data,"NA_Sales", "Fighting")])
    table.add_row(["","Racing", computingScoreGenreProb(data, "NA_Sales","Racing")])
    table.add_row(["","Strategy",  computingScoreGenreProb(data,"NA_Sales", "Strategy")])
    table.add_row(["","Simulation",  computingScoreGenreProb(data,"NA_Sales", "Simulation")])
    table.add_row(["","",""])
    table.add_row(["","",""])
    
    table.add_row(["European Union","Sports", computingScoreGenreProb(data, "EU_Sales","Sports")])
    table.add_row(["","Misc", computingScoreGenreProb(data,"EU_Sales", "Misc")])
    table.add_row(["","Puzzle", computingScoreGenreProb(data, "EU_Sales","Puzzle")])
    table.add_row(["","Platform", computingScoreGenreProb(data,"EU_Sales", "Platform")])
    table.add_row(["","Adventure", computingScoreGenreProb(data,"EU_Sales", "Adventure")])
    table.add_row(["","Action", computingScoreGenreProb(data, "EU_Sales","Action")])
    table.add_row(["","Role-Playing", computingScoreGenreProb(data, "EU_Sales","Role-Playing")])
    table.add_row(["","Shooter", computingScoreGenreProb(data, "EU_Sales","Shooter")])
    table.add_row(["","Fighting",  computingScoreGenreProb(data,"EU_Sales", "Fighting")])
    table.add_row(["","Racing", computingScoreGenreProb(data, "EU_Sales","Racing")])
    table.add_row(["","Strategy",  computingScoreGenreProb(data,"EU_Sales", "Strategy")])
    table.add_row(["","Simulation",  computingScoreGenreProb(data,"EU_Sales", "Simulation")])
    table.add_row(["","",""])
    table.add_row(["","",""])
    
    table.add_row(["Japan","Sports", computingScoreGenreProb(data, "JP_Sales","Sports")])
    table.add_row(["","Misc", computingScoreGenreProb(data,"JP_Sales", "Misc")])
    table.add_row(["","Puzzle", computingScoreGenreProb(data, "JP_Sales","Puzzle")])
    table.add_row(["","Platform", computingScoreGenreProb(data,"JP_Sales", "Platform")])
    table.add_row(["","Adventure", computingScoreGenreProb(data,"JP_Sales", "Adventure")])
    table.add_row(["","Action", computingScoreGenreProb(data, "JP_Sales","Action")])
    table.add_row(["","Role-Playing", computingScoreGenreProb(data, "JP_Sales","Role-Playing")])
    table.add_row(["","Shooter", computingScoreGenreProb(data, "JP_Sales","Shooter")])
    table.add_row(["","Fighting",  computingScoreGenreProb(data,"JP_Sales", "Fighting")])
    table.add_row(["","Racing", computingScoreGenreProb(data, "JP_Sales","Racing")])
    table.add_row(["","Strategy",  computingScoreGenreProb(data,"JP_Sales", "Strategy")])
    table.add_row(["","Simulation",  computingScoreGenreProb(data,"JP_Sales", "Simulation")])
    table.add_row(["","",""])
    table.add_row(["","",""])
    
    table.add_row(["All Other Regions","Sports", computingScoreGenreProb(data,"Other_Sales", "Sports")])
    table.add_row(["","Misc", computingScoreGenreProb(data,"Other_Sales", "Misc")])
    table.add_row(["","Puzzle", computingScoreGenreProb(data, "Other_Sales","Puzzle")])
    table.add_row(["","Platform", computingScoreGenreProb(data,"Other_Sales", "Platform")])
    table.add_row(["","Adventure", computingScoreGenreProb(data,"Other_Sales", "Adventure")])
    table.add_row(["","Action", computingScoreGenreProb(data, "Other_Sales","Action")])
    table.add_row(["","Role-Playing", computingScoreGenreProb(data, "Other_Sales","Role-Playing")])
    table.add_row(["","Shooter", computingScoreGenreProb(data, "Other_Sales","Shooter")])
    table.add_row(["","Fighting",  computingScoreGenreProb(data,"Other_Sales", "Fighting")])
    table.add_row(["","Racing", computingScoreGenreProb(data, "Other_Sales","Racing")])
    table.add_row(["","Strategy",  computingScoreGenreProb(data,"Other_Sales", "Strategy")])
    table.add_row(["","Simulation",  computingScoreGenreProb(data,"Other_Sales", "Simulation")])
    print(table)
    
    table = PrettyTable()
    table.field_names = ["Region with Most Sales", "ERSB Rating", "Decision: Is the Average Score greater than or equal to 7?"]
    table.add_row(["North America","E10+", computingScoreRatingProb(data, "NA_Sales","E10+")])
    table.add_row(["","E", computingScoreRatingProb(data,"NA_Sales", "E")])
    table.add_row(["","T", computingScoreRatingProb(data, "NA_Sales","T")])
    table.add_row(["","M", computingScoreRatingProb(data,"NA_Sales", "M")])
    table.add_row(["","",""])
    
    table.add_row(["European Union","E10+", computingScoreRatingProb(data, "EU_Sales","E10+")])
    table.add_row(["","E", computingScoreRatingProb(data,"EU_Sales", "E")])
    table.add_row(["","T", computingScoreRatingProb(data, "EU_Sales","T")])
    table.add_row(["","M", computingScoreRatingProb(data,"EU_Sales", "M")])
    table.add_row(["","",""])
    
    table.add_row(["Japan","E10+", computingScoreRatingProb(data, "JP_Sales","E10+")])
    table.add_row(["","E", computingScoreRatingProb(data,"JP_Sales", "E")])
    table.add_row(["","T", computingScoreRatingProb(data, "JP_Sales","T")])
    table.add_row(["","M", computingScoreRatingProb(data,"JP_Sales", "M")])
    table.add_row(["","",""])
    
    table.add_row(["All Other Regions","E10+", computingScoreRatingProb(data, "Other_Sales","E10+")])
    table.add_row(["","E", computingScoreRatingProb(data,"Other_Sales", "E")])
    table.add_row(["","T", computingScoreRatingProb(data, "Other_Sales","T")])
    table.add_row(["","M", computingScoreRatingProb(data,"Other_Sales", "M")])
    print(table)
    
if __name__=="__main__":
    main()