#spark-submit --packages com.databricks:spark-csv_2.10:1.2.0 --jars /usr/share/java/postgresql-jdbc4.jar  test.py

import pandas as pd
import numpy as np
import requests
import sys
import json
from pyspark import  SparkContext
from pyspark.sql import HiveContext
import os
import os.path

from sqlalchemy import create_engine
from string import Template
sc = SparkContext()
sqlContext = HiveContext(sc)
timeout = 3
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
allBoxScore = './output/allBoxScore.csv'
allTeamInfo = './output/allTeamInfo.csv'
allPlayerSeasonInfo = './output/allPlayerSeasonInfo.csv'
allPlayerInfo = './output/allPlayerInfo.csv'
teamColor = './output/teamColor.csv'
allGameLog = 'output/allGameLog.csv'
try:
    os.remove(allBoxScore)
except OSError:
    pass

regularGameList = np.array([])
teamList = np.array([])
playerList = np.array([])

leagueID = '00'
seasons = ['2018-19', '2017-18', '2016-17']
gametype = ['Regular Season', 'All Star', 'Playoffs']
currentSeason= '1'

def request(url):
    try:
        data = requests.get(url = url, timeout= timeout, headers = HEADERS).json()['resultSets'][0]
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        sys.exit(1)
    return data

def request2(url):
    try:
        data = requests.get(url = url, timeout= timeout, headers = HEADERS).json()['league']
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        sys.exit(1)
    return data

def gameInfos():
    global regularGameList
    global allGameLog
    gl = pd.DataFrame()
    for type in gametype:
        for season in seasons:
            filepath = './output/csv/gamelog/gamelog_' + season + '_' + type.replace(" ", "_") + '.csv'
            if os.path.isfile(filepath) and season != '2018-19':
                df = pd.read_csv(filepath)
                gl = gl.append(df)
                regularGameList = np.append(regularGameList, df['GAME_ID'].unique(), axis=0)
            else:
                url = 'https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=' + season + '&SeasonType=' + type + '&Sorter=DATE'
                data = request(url)
                if len(data['rowSet']) > 0:
                    df = pd.DataFrame.from_dict(data['rowSet'])
                    df.columns = data['headers']
                    if type == 'Regular Season':
                        df['game_type'] = 'Regular'
                    elif type == 'All Star':
                        df['game_type'] = 'AllStar'
                    else:
                        df['game_type'] = 'Playoffs'
                    df.to_csv(filepath)
                    gl = gl.append(df)
                    regularGameList = np.append(regularGameList, df['GAME_ID'].unique(), axis=0)
                else:
                    print(type)
    gl.to_csv(allGameLog)

def boxScores():
    bs = pd.DataFrame()
    for game in regularGameList:
        game = str(game)
        if len(game) == 8:
            game = '00' + game
        filepath = './output/csv/boxscore/boxscore_' + game + '.csv'
        print(game)
        exist = os.path.isfile(filepath)
        if not exist:
            url = 'https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=0&EndRange=0&GameID=' + game + '&RangeType=0&StartPeriod=0&StartRange=0'
            data = request(url)
            df = pd.DataFrame.from_dict(data['rowSet'])
            df.columns = data['headers']
            df.to_csv(filepath)
            bs = bs.append(df)
        else:
            df = pd.read_csv(filepath)
            bs = bs.append(df)
    bs.to_csv(allBoxScore)

def teamInfos():
    teamlistpath = './output/teamlist.csv'
    global teamList
    if not os.path.isfile(teamlistpath):
        url = 'https://stats.nba.com/stats/commonteamyears?LeagueID=00'
        data = request(url)
        df = pd.DataFrame.from_dict(data['rowSet'])
        df.columns = data['headers']
        df.to_csv(teamlistpath)
    tl = pd.read_csv(teamlistpath)
    teamList = tl['TEAM_ID'].unique()
    at = pd.DataFrame()
    for team in teamList:
        team = str(team)
        filepath = './output/csv/teaminfo/teaminfo_' + team + '.csv'
        if not os.path.isfile(filepath):
            url = 'https://stats.nba.com/stats/teamdetails?TeamID=' + team
            data = request(url)
            df = pd.DataFrame.from_dict(data['rowSet'])
            if not df.empty:
                df.columns = data['headers']
                df.to_csv(filepath)
        df = pd.read_csv(filepath)
        at = at.append(df)
    at.to_csv(allTeamInfo)
    print('Team Info Complete')

def playerInfos():
    global playerList
    playerInfo = pd.read_csv(allPlayerSeasonInfo)
    playerList = playerInfo['PERSON_ID'].unique()
    players_2018 = 'http://data.nba.net/data/10s/prod/v1/2018/players.json'
    if not os.path.isfile(allPlayerInfo):
        data = request2(players_2018)
        data = data['standard']
        #print(json.dumps(data, indent=4, sort_keys=True))
        df = pd.io.json.json_normalize(data, sep ='_')
        #df = pd.DataFrame.from_dict(data, orient='columns')
        df.drop('teams', axis=1, inplace=True)
        print(df.head())
        df.to_csv(allPlayerInfo)

    # for player in playerList:
    #     player = str(player)
    #         filepath = './output/csv/player_info/player_info_' + player + '.csv'
    #     if not os.path.isfile(filepath):
    #         url = 'https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=' + player
    #         print("REQUESTING PLAYER: " + player)
    #         data = request(url)
    #         df = pd.DataFrame.from_dict(data['rowSet'])
    #         df.columns = data['headers']
    #         df.to_csv(filepath)
    #     df = pd.read_csv(filepath)
    #     df.to_csv(allPlayerInfo, mode='a')
    print('Player Info Complete')

def playerSeason():

    dfs = {}
    for season in seasons:
        filepath = './output/csv/player_season/player_season_' + season + '.csv'
        if not season == '2018-19temp':
            if not os.path.isfile(filepath):
                url = 'https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=' + currentSeason + '&LeagueID=' + leagueID + '&Season=' + season
                data = request(url)
                df = pd.DataFrame.from_dict(data['rowSet'])
                df.columns = data['headers']
                df['season'] = season
                df.to_csv(filepath)
                dfs[season] = df
            else:
                df = pd.read_csv(filepath)
                dfs[season] = df
        else:
            url = 'https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=' + currentSeason + '&LeagueID=' + leagueID + '&Season=' + season
            data = request(url)
            df = pd.DataFrame.from_dict(data['rowSet'])
            df.columns = data['headers']
            df['season'] = season
            df.to_csv(filepath)
            dfs[season] = df
    sr = pd.concat(dfs)
    sr.to_csv(allPlayerSeasonInfo)
    print('Season Roster: Retieved ' + str(len(sr)) + ' rows from ' + str(len(seasons)) + ' seasons')
    return sr

def map():
    ti_output_file = './output/teamInfo.parquet'
    teamInfos()
    teamInfo_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', comment="N").load(allTeamInfo).cache()
    teamInfo_df.registerTempTable("teamInfo")

    ti = sqlContext.sql(""" SELECT
        TEAM_ID as id,
        ABBREVIATION as abv,
        NICKNAME as name,
        CITY as city,
        ARENA as arena,
        ARENACAPACITY as arena_capacity,
        YEARFOUNDED as year_founded,
        OWNER as owner,
        GENERALMANAGER as gm,
        HEADCOACH as head_coach,
        DLEAGUEAFFILIATION as dleague
        FROM teamInfo
        """)
    ti.registerTempTable('ti')

    ti.write.save(ti_output_file, mode = 'overwrite')
    sqlContext.dropTempTable('gameInfo')

    gi_output_file = './output/gameInfo.parquet'
    gameInfos()
    gameInfo_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', comment="N").load(allGameLog).cache()
    gameInfo_df.registerTempTable("gameInfo")

    gi = sqlContext.sql(""" SELECT
        id,
        MAX(date) as date,
        MAX(CASE WHEN matchup LIKE '%vs%' THEN team ELSE 0 END) as home,
        MAX(CASE WHEN matchup LIKE '%@%' THEN team ELSE 0 END) as away,
        MAX(CASE WHEN outcome = 'W' THEN team ELSE 0 END) as win,
        MAX(CASE WHEN matchup LIKE '%vs%' THEN pts ELSE 0 END) as home_points,
        MAX(CASE WHEN matchup LIKE '%@%' THEN pts ELSE 0 END) as away_points,
        MAX(season) as season,
        MAX(game_type) as game_type
        FROM (SELECT
        GAME_ID as id,
        GAME_DATE as date,
        TEAM_ID as team,
        MATCHUP as matchup,
        WL as outcome,
        PTS as pts,
        SEASON_ID as season,
        game_type
        FROM gameInfo) a GROUP BY id
        """)
    gi.registerTempTable('gi')

    gi.write.save(gi_output_file, mode = 'overwrite')
    sqlContext.dropTempTable('gameInfo')

    bs_output_file = './output/boxScore.parquet'
    boxScore = boxScores()
    boxScore_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', comment="N").load(allBoxScore).cache()
    boxScore_df.registerTempTable("boxScore")

    bs = sqlContext.sql(""" SELECT
        GAME_ID as game_id,
        PLAYER_ID as player_id,
        TEAM_ID as team_id,
        START_POSITION as start_position,
        MIN as min,
        FGM as fgm,
        FGA as fga,
        FG_PCT as fg_pct,
        FG3M as fg3m,
        FG3A as fg3a,
        FG3_PCT as fg3_pct,
        FTM as ftm,
        FTA as fta,
        FT_PCT as ft_pct,
        OREB as oreb,
        DREB as dreb,
        REB as reb,
        AST as ast,
        STL as stl,
        BLK as blk,
        TO as to,
        PF as pf,
        PTS as points,
        PLUS_MINUS as pm
        FROM boxScore
        """)
    bs.registerTempTable('bs')

    bs.write.save(bs_output_file, mode = 'overwrite')
    sqlContext.dropTempTable('boxScore')

    playerSeason()
    sp_output_file = './output/player_season.parquet'

    sp = sqlContext.sql(""" SELECT
        c.player_id,
        d.season,
        c.team_id,
        SUM(CASE WHEN start_position IS NOT NULL THEN 1 ELSE 0 END) as games_started,
        COUNT(*) as games_played,
        SUM(min) as total_min,
        SUM(fgm) as total_fgm,
        SUM(fga) as total_fga,
        SUM(fg3m) as total_fg3m,
        SUM(fg3a) as total_fg3a,
        SUM(ftm) as total_ftm,
        SUM(fta) as total_fta,
        SUM(oreb) as total_oreb,
        SUM(dreb) as total_dreb,
        SUM(reb) as total_reb,
        SUM(ast) as total_ast,
        SUM(stl) as total_stl,
        SUM(blk) as total_blk,
        SUM(to) as total_to,
        SUM(points) as total_points
        from bs c LEFT JOIN gi d ON c.game_id = d.id GROUP BY c.player_id, d.season, c.team_id
        """)
    sp.registerTempTable('sp')

    sp.write.save(sp_output_file, mode = 'overwrite')
    sqlContext.dropTempTable('season_player')

    pi_output_file = './output/playerInfo.parquet'
    playerInfos()
    playerInfo_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', comment="N").load(allPlayerInfo).cache()
    playerInfo_df.registerTempTable("playerInfo")

    pi = sqlContext.sql(""" SELECT
        personId as id,
        firstName as fname,
        lastName as lname,
        dateOfBirthUTC as birthdate,
        collegeName as school,
        country as country,
        heightFeet * 12 + heightInches  as height,
        weightPounds as weight,
        yearsPro as season_exp,
        jersey as jersey,
        pos as position,
        isActive as roster_status,
        teamId as team_id,
        nbaDebutYear as start_year,
        nbaDebutYear + yearsPro as end_year,
        draft_seasonYear as draft_year,
        draft_roundNum as draft_round,
        draft_pickNum as draft_number,
        CURRENT_TIMESTAMP as update_date
        FROM playerInfo
        """)
    pi.registerTempTable('pi')

    pi.write.save(pi_output_file, mode = 'overwrite')
    sqlContext.dropTempTable('playerInfo')

    tc_output_file = './output/teamColor.parquet'
    teamColor_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', comment="N").load(teamColor).cache()
    teamColor_df.registerTempTable("teamColor")

    tc = sqlContext.sql(""" SELECT
        *
        FROM teamColor
        """)
    tc.registerTempTable('tc')

    tc.write.save(tc_output_file, mode = 'overwrite')
    sqlContext.dropTempTable('teamColor')
    print("Map Completed")

def upload():
    target_schema ='nba'
    write_mode='overwrite'
    basepath='./output/'
    map = { basepath+"player_season.parquet":"player_season",
            basepath+"gameInfo.parquet":"game_info",
            basepath+"boxScore.parquet":"boxscore",
            basepath+"teamInfo.parquet":"team_info",
            basepath+"playerInfo.parquet":"player_bio",
            basepath+"teamColor.parquet":"team_color"
            }
    #class QueryException(BaseException):
    #    pass
    engine = ""
    name = os.environ.get('DB_NAME')
    key = os.environ.get('DB_PASSWORD')

    Properties = {'user':name,'password':key, "driver": 'org.postgresql.Driver' }
    URL = 'jdbc:postgresql://23.226.138.66:5432/prod'
    for filename in map.keys ():
        tablename = target_schema + '.' + map [ filename ]
        data_object = sqlContext.read.parquet(filename)
        data_object.write.jdbc(url=URL, table = tablename , properties = Properties, mode= write_mode )

    print ('Uplaod Completed')


map()
upload()
