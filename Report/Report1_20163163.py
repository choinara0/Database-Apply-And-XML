import pymysql
from PyQt5.QtWidgets import *
import sys, datetime
import csv
import json
import xml.etree.ElementTree as ET


class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(sql)
            print(e)
            print(type(e))
        finally:
            conn.close()

    def updateExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의

    def selectTeam(self):
        sql = "SELECT DISTINCT team_name FROM TEAM"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples


    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerNation(self):
        sql = "SELECT DISTINCT nation FROM player"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    # def selectPlayerUsingPosition(self, value):
    #     if value == '없음':
    #         sql = "SELECT * FROM player WHERE position IS NULL"
    #         params = ()
    #     else:
    #         sql = "SELECT * FROM player WHERE position = %s"
    #         params = (value)         # SQL문의 실제 파라미터 값의 튜플
    #
    #     util = DB_Utils()
    #     tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
    #     return tuples

    def selectPlayer(self, tValue, pValue, nValue, height, weight, heightCheck, weightCheck):
        if height == str(-1) and weight == str(-1):
            if tValue == "ALL" and pValue == "ALL" and nValue == "ALL":
                sql = "SELECT * FROM player"
                params = ()

            elif tValue == "ALL" and nValue == "ALL":
                sql = "SELECT * FROM player WHERE position = %s"
                params = (pValue)

            elif pValue == "ALL" and nValue == "ALL":
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s"
                params = (tValue)

            elif tValue == "ALL" and pValue == "ALL":
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL"
                    params = ()
                else:
                    sql = "SELECT * FROM player WHERE nation = %s"
                    params = (nValue)

            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL":
                sql = "SELECT * FROM player WHERE position IS NULL"
                params = ()

            elif tValue == "ALL" and pValue == "미정":
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL"
                    params = ()
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s"
                    params = (nValue)

            elif pValue == "미정" and nValue == "ALL":
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL"
                params = (tValue)

            elif pValue == "미정":
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL"
                    params = (tValue)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s"
                    params = (tValue, nValue)

            elif tValue == "ALL":
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL"
                    params = (pValue)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s"
                    params = (pValue, nValue)

            elif pValue == "ALL":
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL"
                    params = (tValue)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s"
                    params = (tValue, nValue)

            elif nValue == "ALL":
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s"
                params = (tValue, pValue)

            else:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL"
                    params = (tValue, pValue)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s"
                    params = (tValue, pValue, nValue)
        else:
            if tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and heightCheck == True and weightCheck == True:
                sql = "SELECT * FROM player WHERE height >= %s AND weight >= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and heightCheck == False and weightCheck == False:
                sql = "SELECT * FROM player WHERE height <= %s AND weight <= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and heightCheck == True and weightCheck == False:
                sql = "SELECT * FROM player WHERE height >= %s AND weight <= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and heightCheck == False and weightCheck == True:
                sql = "SELECT * FROM player WHERE height <= %s AND weight >= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and heightCheck == True:
                sql = "SELECT * FROM player WHERE height >= %s"
                params = (height)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and heightCheck == False:
                sql = "SELECT * FROM player WHERE height <= %s"
                params = (height)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and weightCheck == True:
                sql = "SELECT * FROM player WHERE weight >= %s"
                params = (weight)
            elif tValue == "ALL" and pValue == "ALL" and nValue == "ALL" and weightCheck == False:
                sql = "SELECT * FROM player WHERE weight <= %s"
                params = (weight)

            elif tValue == "ALL" and nValue == "ALL" and heightCheck == True and weightCheck == True:
                sql = "SELECT * FROM player WHERE position = %s AND height >= %s AND weight >= %s"
                params = (pValue, height, weight)
            elif tValue == "ALL" and nValue == "ALL" and heightCheck == False and weightCheck == False:
                sql = "SELECT * FROM player WHERE position = %s AND height <= %s AND weight <= %s"
                params = (pValue, height, weight)
            elif tValue == "ALL" and nValue == "ALL" and heightCheck == True and weightCheck == False:
                sql = "SELECT * FROM player WHERE position = %s AND height >= %s AND weight <= %s"
                params = (pValue, height, weight)
            elif tValue == "ALL" and nValue == "ALL" and heightCheck == False and weightCheck == True:
                sql = "SELECT * FROM player WHERE position = %s AND height <= %s AND weight >= %s"
                params = (pValue, height, weight)
            elif tValue == "ALL" and nValue == "ALL" and heightCheck == True:
                sql = "SELECT * FROM player WHERE position = %s AND height >= %s"
                params = (pValue, height)
            elif tValue == "ALL" and nValue == "ALL" and heightCheck == False:
                sql = "SELECT * FROM player WHERE position = %s AND height <= %s"
                params = (pValue, height)
            elif tValue == "ALL" and nValue == "ALL" and weightCheck == True:
                sql = "SELECT * FROM player WHERE position = %s AND weight >= %s"
                params = (pValue, weight)
            elif tValue == "ALL" and nValue == "ALL" and weightCheck == False:
                sql = "SELECT * FROM player WHERE position = %s AND weight <= %s"
                params = (pValue, weight)

            elif pValue == "ALL" and nValue == "ALL" and heightCheck == True and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND height >= %s AND weight >= %s"
                params = (tValue, height, weight)
            elif pValue == "ALL" and nValue == "ALL" and heightCheck == False and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND height <= %s AND weight <= %s"
                params = (tValue, height, weight)
            elif pValue == "ALL" and nValue == "ALL" and heightCheck == True and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND height >= %s AND weight <= %s"
                params = (tValue, height, weight)
            elif pValue == "ALL" and nValue == "ALL" and heightCheck == False and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND height <= %s AND weight >= %s"
                params = (tValue, height, weight)
            elif pValue == "ALL" and nValue == "ALL" and heightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND height >= %s"
                params = (tValue, height)
            elif pValue == "ALL" and nValue == "ALL" and heightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND height <= %s"
                params = (tValue, height)
            elif pValue == "ALL" and nValue == "ALL" and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND weight >= %s"
                params = (tValue, weight)
            elif pValue == "ALL" and nValue == "ALL" and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND weight <= %s"
                params = (tValue, weight)

            elif tValue == "ALL" and pValue == "ALL" and heightCheck == True and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND height >= %s AND weight >= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND height >= %s AND weight >= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "ALL" and heightCheck == False and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND height <= %s AND weight <= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND height <= %s AND weight <= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "ALL" and heightCheck == True and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND height >= %s AND weight <= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND height >= %s AND weight <= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "ALL" and heightCheck == False and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND height <= %s AND weight >= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND height <= %s AND weight >= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "ALL" and heightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND height >= %s"
                    params = (height)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND height >= %s"
                    params = (nValue, height)
            elif tValue == "ALL" and pValue == "ALL" and heightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND height <= %s"
                    params = (height)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND height <= %s"
                    params = (nValue, height)
            elif tValue == "ALL" and pValue == "ALL" and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND weight >= %s"
                    params = (weight)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND weight >= %s"
                    params = (nValue, weight)
            elif tValue == "ALL" and pValue == "ALL" and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE nation IS NULL AND weight <= %s"
                    params = (weight)
                else:
                    sql = "SELECT * FROM player WHERE nation = %s AND weight <= %s"
                    params = (nValue, weight)

            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and heightCheck == True and weightCheck == True:
                sql = "SELECT * FROM player WHERE position IS NULL AND height >= %s AND weight >= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and heightCheck == False and weightCheck == False:
                sql = "SELECT * FROM player WHERE position IS NULL AND height <= %s AND weight <= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and heightCheck == True and weightCheck == False:
                sql = "SELECT * FROM player WHERE position IS NULL AND height >= %s AND weight <= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and heightCheck == False and weightCheck == True:
                sql = "SELECT * FROM player WHERE position IS NULL AND height <= %s AND weight >= %s"
                params = (height, weight)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and heightCheck == True:
                sql = "SELECT * FROM player WHERE position IS NULL AND height >= %s"
                params = (height)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and heightCheck == False:
                sql = "SELECT * FROM player WHERE position IS NULL AND height <= %s"
                params = (height)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and weightCheck == True:
                sql = "SELECT * FROM player WHERE position IS NULL AND weight >= %s"
                params = (weight)
            elif tValue == "ALL" and pValue == "미정" and nValue == "ALL" and weightCheck == False:
                sql = "SELECT * FROM player WHERE position IS NULL AND weight <= %s"
                params = (weight)


            elif tValue == "ALL" and pValue == "미정" and heightCheck == True and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height >= %s AND weight >= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s AND weight >= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "미정" and heightCheck == False and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height <= %s AND weight <= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s AND weight <= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "미정" and heightCheck == True and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height >= %s AND weight <= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s AND weight <= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "미정" and heightCheck == False and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height <= %s AND weight >= %s"
                    params = (height, weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s AND weight >= %s"
                    params = (nValue, height, weight)
            elif tValue == "ALL" and pValue == "미정" and heightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height >= %s"
                    params = (height)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height >= %s"
                    params = (nValue, height)
            elif tValue == "ALL" and pValue == "미정" and heightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND height <= %s"
                    params = (weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND height <= %s"
                    params = (nValue, weight)
            elif tValue == "ALL" and pValue == "미정" and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND weight >= %s"
                    params = (weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND weight >= %s"
                    params = (nValue, weight)
            elif tValue == "ALL" and pValue == "미정" and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation IS NULL AND weight <= %s"
                    params = (weight)
                else:
                    sql = "SELECT * FROM player WHERE position IS NULL AND nation = %s AND weight <= %s"
                    params = (nValue, weight)



            elif pValue == "미정" and nValue == "ALL" and heightCheck == True and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND height >= %s AND weight >= %s"
                params = (tValue, height, weight)
            elif pValue == "미정" and nValue == "ALL" and heightCheck == False and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND height <= %s AND weight <= %s"
                params = (tValue, height, weight)
            elif pValue == "미정" and nValue == "ALL" and heightCheck == True and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND height >= %s AND weight <= %s"
                params = (tValue, height, weight)
            elif pValue == "미정" and nValue == "ALL" and heightCheck == False and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND height <= %s AND weight >= %s"
                params = (tValue, height, weight)
            elif pValue == "미정" and nValue == "ALL" and heightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND height >= %s"
                params = (tValue, height)
            elif pValue == "미정" and nValue == "ALL" and heightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND height <= %s"
                params = (tValue, height)
            elif pValue == "미정" and nValue == "ALL" and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND weight >= %s"
                params = (tValue, weight)
            elif pValue == "미정" and nValue == "ALL" and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND weight <= %s"
                params = (tValue, weight)

            elif pValue == "미정" and heightCheck == True and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND height >= %s AND weight >= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND height >= %s AND weight >= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "미정" and heightCheck == False and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND height <= %s AND weight <= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND height <= %s AND weight <= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "미정" and heightCheck == True and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND height >= %s AND weight <= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND height >= %s AND weight <= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "미정" and heightCheck == False and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND height <= %s AND weight >= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND height <= %s AND weight >= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "미정" and heightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND height >= %s"
                    params = (tValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND height >= %s"
                    params = (tValue, nValue, height)
            elif pValue == "미정" and heightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND height <= %s"
                    params = (tValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND height <= %s"
                    params = (tValue, nValue, height)
            elif pValue == "미정" and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND weight >= %s"
                    params = (tValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND weight >= %s"
                    params = (tValue, nValue, weight)
            elif pValue == "미정" and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation IS NULL AND weight <= %s"
                    params = (tValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position IS NULL AND nation = %s AND weight <= %s"
                    params = (tValue, nValue, weight)


            elif tValue == "ALL" and heightCheck == True and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND height >= %s AND weight >= %s"
                    params = (pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND height >= %s AND weight >= %s"
                    params = (pValue, nValue, height, weight)
            elif tValue == "ALL" and heightCheck == False and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND height <= %s AND weight <= %s"
                    params = (pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND height <= %s AND weight <= %s"
                    params = (pValue, nValue, height, weight)
            elif tValue == "ALL" and heightCheck == True and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND height >= %s AND weight <= %s"
                    params = (pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND height >= %s AND weight <= %s"
                    params = (pValue, nValue, height, weight)
            elif tValue == "ALL" and heightCheck == False and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND height <= %s AND weight >= %s"
                    params = (pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND height <= %s AND weight >= %s"
                    params = (pValue, nValue, height, weight)
            elif tValue == "ALL" and heightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND height >= %s"
                    params = (pValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND height >= %s"
                    params = (pValue, nValue, height)
            elif tValue == "ALL" and heightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND height <= %s"
                    params = (pValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND height <= %s"
                    params = (pValue, nValue, height)
            elif tValue == "ALL" and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND weight >= %s"
                    params = (pValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND weight >= %s"
                    params = (pValue, nValue, weight)
            elif tValue == "ALL" and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation IS NULL AND weight <= %s"
                    params = (pValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND position = %s AND nation = %s AND weight <= %s"
                    params = (pValue, nValue, weight)


            elif pValue == "ALL" and heightCheck == True and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND height >= %s AND weight >= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND height >= %s AND weight >= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "ALL" and heightCheck == False and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND height <= %s AND weight <= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND height <= %s AND weight <= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "ALL" and heightCheck == True and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND height >= %s AND weight <= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND height >= %s AND weight <= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "ALL" and heightCheck == False and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND height <= %s AND weight >= %s"
                    params = (tValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND height <= %s AND weight >= %s"
                    params = (tValue, nValue, height, weight)
            elif pValue == "ALL" and heightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND height >= %s"
                    params = (tValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND height >= %s"
                    params = (tValue, nValue, height)
            elif pValue == "ALL" and heightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND height <= %s"
                    params = (tValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND height <= %s"
                    params = (tValue, nValue, height)
            elif pValue == "ALL" and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND weight >= %s"
                    params = (tValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND weight >= %s"
                    params = (tValue, nValue, weight)
            elif pValue == "ALL" and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation IS NULL AND weight <= %s"
                    params = (tValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND nation = %s AND weight <= %s"
                    params = (tValue, nValue, weight)


            elif nValue == "ALL" and heightCheck == True and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND height >= %s AND weight >= %s"
                params = (tValue, pValue, height, weight)
            elif nValue == "ALL" and heightCheck == False and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND height <= %s AND weight <= %s"
                params = (tValue, pValue, height, weight)
            elif nValue == "ALL" and heightCheck == True and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND height >= %s AND weight <= %s"
                params = (tValue, pValue, height, weight)
            elif nValue == "ALL" and heightCheck == False and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND height <= %s AND weight >= %s"
                params = (tValue, pValue, height, weight)
            elif nValue == "ALL" and heightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND height >= %s"
                params = (tValue, pValue, height)
            elif nValue == "ALL" and heightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND height <= %s"
                params = (tValue, pValue, height)
            elif nValue == "ALL" and weightCheck == True:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND weight >= %s"
                params = (tValue, pValue, weight)
            elif nValue == "ALL" and weightCheck == False:
                sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND weight <= %s"
                params = (tValue, pValue, weight)

            elif heightCheck == True and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND height >= %s AND weight >= %s"
                    params = (tValue, pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND height >= %s AND weight >= %s"
                    params = (tValue, pValue, nValue, height, weight)
            elif heightCheck == False and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND height <= %s AND weight <= %s"
                    params = (tValue, pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND height <= %s AND weight <= %s"
                    params = (tValue, pValue, nValue, height, weight)
            elif heightCheck == True and weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND height >= %s AND weight <= %s"
                    params = (tValue, pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND height >= %s AND weight <= %s"
                    params = (tValue, pValue, nValue, height, weight)
            elif heightCheck == False and weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND height <= %s AND weight >= %s"
                    params = (tValue, pValue, height, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND height <= %s AND weight >= %s"
                    params = (tValue, pValue, nValue, height, weight)
            elif heightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND height >= %s"
                    params = (tValue, pValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND height >= %s"
                    params = (tValue, pValue, nValue, height)
            elif heightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND height <= %s"
                    params = (tValue, pValue, height)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND height <= %s"
                    params = (tValue, pValue, nValue, height)
            elif weightCheck == True:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND weight >= %s"
                    params = (tValue, pValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND weight >= %s"
                    params = (tValue, pValue, nValue, weight)
            elif weightCheck == False:
                if nValue == "대한민국":
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation IS NULL AND weight <= %s"
                    params = (tValue, pValue, weight)
                else:
                    sql = "SELECT * FROM player INNER JOIN team WHERE player.team_id = team.team_id AND team_name = %s AND position = %s AND nation = %s AND weight <= %s"
                    params = (tValue, pValue, nValue, weight)

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

class DB_Updates:
    # 모든 갱신문은 여기에 각각 하나의 메소드로 정의

    def insertPlayer(self, player_id, player_name, team_id, position):
        sql = "INSERT INTO player (player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
        params = (player_id, player_name, team_id, position)

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

#########################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        # 윈도우 설정
        self.setWindowTitle("Report K-league Search")
        self.setGeometry(0, 0, 1100, 620)

        # 라벨 설정
        self.labelTitle = QLabel("선수 검색", self)
        self.labelTeam = QLabel("팀명: ", self)
        self.labelPosition = QLabel("포지션: ", self)
        self.labelNation = QLabel("출신국: ", self)
        self.labelHeight = QLabel("키: ", self)
        self.labelWeight = QLabel("몸무게: ", self)
        self.labelFile = QLabel("파일 출력", self)

        # 콤보박스 설정
        self.comboBoxTeam = QComboBox(self)
        self.comboBoxPosition = QComboBox(self)
        self.comboBoxNation = QComboBox(self)

        # 라인에디트 설정
        self.lineEditHeight = QLineEdit(self)
        self.lineEditWeight = QLineEdit(self)

        # 라디오버튼 설정
        self.radioButtonHeightAbove = QRadioButton("이상")
        self.radioButtonHeightBelow = QRadioButton("이하")
        self.groupBoxHeight = QGroupBox()
        self.radioButtonHeightAbove.clicked.connect(self.heightIsChecked)
        self.radioButtonHeightBelow.clicked.connect(self.heightIsChecked)
        self.radioButtonWeightAbove = QRadioButton("이상")
        self.radioButtonWeightBelow = QRadioButton("이하")


        self.groupBoxWeight = QGroupBox()
        self.radioButtonxCsv = QRadioButton("CSV")
        self.radioButtonJson = QRadioButton("JSON")
        self.radioButtonXml = QRadioButton("XML")
        self.groupBoxFile = QGroupBox()

        # DB 검색문 실행
        query = DB_Queries()
        teamRows = query.selectTeam()
        postionRows = query.selectPlayerPosition()
        nationRows = query.selectPlayerNation()

        teamColumnName = list(teamRows[0].keys())[0]
        teamItems = [row[teamColumnName] for row in teamRows]
        teamItems.append("ALL")
        self.comboBoxTeam.addItems(teamItems)
        self.comboBoxTeam.setCurrentIndex(15)

        positionColumnName = list(postionRows[0].keys())[0]
        positionItems = ['미정' if row[positionColumnName] == None else row[positionColumnName] for row in postionRows]
        positionItems.append("ALL")
        self.comboBoxPosition.addItems(positionItems)
        self.comboBoxPosition.setCurrentIndex(5)

        nationColumnName = list(nationRows[0].keys())[0]
        nationItems = ['대한민국' if row[nationColumnName] == None else row[nationColumnName] for row in nationRows]
        nationItems.append("ALL")
        self.comboBoxNation.addItems(nationItems)
        self.comboBoxNation.setCurrentIndex(13)


        # 푸쉬버튼 설정
        self.resetButton = QPushButton("초기화", self)
        self.resetButton.clicked.connect(self.resetButton_Clicked)
        self.saveButton = QPushButton("저장", self)
        self.saveButton.clicked.connect(self.saveButton_Clicked)
        self.pushButton = QPushButton("검색", self)
        self.pushButton.clicked.connect(self.pushButton_Clicked)


        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        middleLayout = QGridLayout()
        middleLayout.addWidget(self.tableWidget)

        # 레이아웃 설정
        self.heightLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.weightLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.groupBoxHeight.setLayout(self.heightLayout)
        self.groupBoxWeight.setLayout(self.weightLayout)
        self.heightLayout.addWidget(self.radioButtonHeightAbove)
        self.heightLayout.addWidget(self.radioButtonHeightBelow)
        self.weightLayout.addWidget(self.radioButtonWeightAbove)
        self.weightLayout.addWidget(self.radioButtonWeightBelow)

        toplayout = QGridLayout()
        toplayout.addWidget(self.labelTitle, 0, 0)
        toplayout.addWidget(self.labelTeam, 1, 0)
        toplayout.addWidget(self.comboBoxTeam, 1, 1)
        toplayout.addWidget(self.labelPosition, 1, 5)
        toplayout.addWidget(self.comboBoxPosition, 1, 6)
        toplayout.addWidget(self.labelNation, 1, 9)
        toplayout.addWidget(self.comboBoxNation, 1, 10)
        toplayout.addWidget(self.resetButton, 1, 11)
        toplayout.addWidget(self.labelHeight, 2, 0)
        toplayout.addWidget(self.lineEditHeight, 2, 1)
        toplayout.addWidget(self.groupBoxHeight)
        toplayout.addWidget(self.labelWeight, 2, 5)
        toplayout.addWidget(self.lineEditWeight, 2, 6)
        toplayout.addWidget(self.groupBoxWeight)
        toplayout.addWidget(self.pushButton, 2, 11)

        bottomInnerLayout = QBoxLayout(QBoxLayout.LeftToRight)
        bottomInnerLayout.addWidget(self.radioButtonxCsv)
        bottomInnerLayout.addWidget(self.radioButtonJson)
        bottomInnerLayout.addWidget(self.radioButtonXml)
        self.groupBoxFile.setLayout(bottomInnerLayout)

        bottomLayout = QGridLayout()
        bottomLayout.addWidget(self.labelFile, 0, 0)
        bottomLayout.addWidget(self.groupBoxFile, 1, 0)
        bottomLayout.addWidget(self.saveButton, 1, 11)




        layout = QVBoxLayout()
        layout.addLayout(toplayout)
        layout.addLayout(middleLayout)
        layout.addLayout(bottomLayout)
        self.setLayout(layout)


    def comboBoxTeam_Activated(self):

        self.teamValue = self.comboBoxTeam.currentText()

    def comboBoxPosition_Activated(self):

        self.positionValue = self.comboBoxPosition.currentText()  # positionValue를 통해 선택한 포지션 값을 전달

    def comboBoxNation_Activated(self):

        self.nationValue = self.comboBoxNation.currentText()

    def lineEditHeight_Activated(self):
        text = self.lineEditHeight.text()
        if len(text) == 0 and self.heightCheck == True:
            self.height = str(-1)
        elif len(text) == 0 and self.heightCheck == False:
            self.height = str(float('inf'))
        elif len(text) == 0 and self.heightCheck == None:
            self.height = str(-1)
        else:
            self.height = text

    def lineEditWeight_Activated(self):
        text = self.lineEditWeight.text()
        if len(text) == 0 and self.weightCheck == True:
            self.weight = str(-1)
        elif len(text) == 0 and self.weightCheck == False:
            self.weight = str(float('inf'))
        elif len(text) == 0 and self.weightCheck == None:
            self.weight = str(-1)
        else:
            self.weight = self.lineEditWeight.text()

    def heightIsChecked(self):
        if self.radioButtonHeightAbove.isChecked():
            self.heightCheck = True
        elif self.radioButtonHeightBelow.isChecked():
            self.heightCheck = False
        else:
            self.heightCheck = None

    def weightIsChecked(self):
        if self.radioButtonWeightAbove.isChecked():
            self.weightCheck = True
        elif self.radioButtonWeightBelow.isChecked():
            self.weightCheck = False
        else:
            self.weightCheck = None

    def pushButton_Clicked(self):

        self.comboBoxTeam_Activated()
        self.comboBoxPosition_Activated()
        self.comboBoxNation_Activated()
        self.heightIsChecked()
        self.weightIsChecked()
        self.lineEditHeight_Activated()
        self.lineEditWeight_Activated()


        try:
            # DB 검색문 실행
            print(self.teamValue, self.positionValue, self.nationValue, self.height, self.weight, self.heightCheck,
                  self.weightCheck)
            query = DB_Queries()
            players = query.selectPlayer(self.teamValue, self.positionValue, self.nationValue, self.height, self.weight,
                                         self.heightCheck, self.weightCheck)

            if players:
                self.tableWidget.clearContents()  # 테이블을 지움
                self.tableWidget.setRowCount(len(players))
                self.tableWidget.setColumnCount(len(players[0]))
                columnNames = list(players[0].keys())
                self.tableWidget.setHorizontalHeaderLabels(columnNames)
                self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

                for player in players:  # player는 딕셔너리임.
                    rowIDX = players.index(player)  # 테이블 위젯의 row index 할당

                    for k, v in player.items():
                        columnIDX = list(player.keys()).index(k)  # 테이블 위젯의 column index 할당

                        if k == "NATION" and v == None:
                            item = QTableWidgetItem("대한민국")
                        elif k == "POSITION" and v == None:
                            item = QTableWidgetItem("미정")
                        elif v == None:
                            continue
                        elif isinstance(v, datetime.date):  # QTableWidgetItem 객체 생성
                            item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                        else:
                            item = QTableWidgetItem(str(v))

                        self.tableWidget.setItem(rowIDX, columnIDX, item)

                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()

        except Exception as e:
            QMessageBox.about(self, "메시지 박스", "정수를 입력해주세요 ")
            self.lineEditHeight.setText("")
            self.lineEditWeight.setText("")
            return

        return players

    def saveButton_Clicked(self):
        if self.radioButtonxCsv.isChecked():
            self.readDB_writeCSV()
        elif self.radioButtonJson.isChecked():
            self.readDB_writeJSON()
        else:
            self.readDB_writeXML()
        return

    def resetButton_Clicked(self):
        self.comboBoxTeam.setCurrentIndex(15)
        self.comboBoxPosition.setCurrentIndex(5)
        self.comboBoxNation.setCurrentIndex(13)
        self.lineEditHeight.setText("")
        self.lineEditWeight.setText("")
        return

    def readDB_writeCSV(self):
        self.players = self.pushButton_Clicked()
        # CSV 화일을 쓰기 모드로 생성
        with open('playerGK.csv', 'w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f)

            columnNames = list(self.players[0].keys())
            print(columnNames)
            print()

            wr.writerow(columnNames)

            for player in self.players:
                row = list(player.values())
                print(row)
                wr.writerow(row)

    def readDB_writeJSON(self):
        self.players = self.pushButton_Clicked()
        for player in self.players:
            for k, v in player.items():
                if k == 'POSITION' and v == None:
                    player[k] = '미정'
                elif k== 'NATION' and v == None:
                    player[k] = '대한민국'
                elif isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')
                    print(player[k])

        newDict = dict(selectPlayer=self.players)  # playerGK(파일명)을 Key값으로, 파일내용 전체를 Value로
        # JSON 화일에 쓰기
        # dump()에 의해 모든 작은 따옴표('')는 큰 따옴표("")로 변환됨
        with open('selectPlayer.json', 'w', encoding='utf-8') as f:
            json.dump(newDict, f, ensure_ascii=False)

        with open('selectPlayer.json', 'w', encoding='utf-8') as f:
            json.dump(newDict, f, indent=4, ensure_ascii=False)

    def readDB_writeXML(self):
        self.players = self.pushButton_Clicked()
        for player in self.players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')  # 키가 k인 item의 값 v를 수정

        newDict = dict(selectPlayer=self.players)

        tableName = list(newDict.keys())[0]
        tableRows = list(newDict.values())[0]

        rootElement = ET.Element('Table')
        rootElement.attrib['name'] = tableName

        for row in tableRows:
            rowElement = ET.Element('Row')
            rootElement.append(rowElement)

            for columnName in list(row.keys()):
                if columnName == 'POSITION' and row[columnName] == None:
                    rowElement.attrib[columnName] = '미정'
                elif columnName == 'NATION' and row[columnName] == None:
                    rowElement.attrib[columnName] = '대한민국'
                elif row[columnName] == None:  # NICKNAME, JOIN_YYYY 처리
                    rowElement.attrib[columnName] = ''
                else:
                    rowElement.attrib[columnName] = row[columnName]

                if type(row[columnName]) == int:  # BACK_NO, HEIGHT, WEIGHT 처리
                    rowElement.attrib[columnName] = str(row[columnName])

        ET.ElementTree(rootElement).write('selectPlayer.xml', encoding='utf-8', xml_declaration=True)

#########################################

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()