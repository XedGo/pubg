# import json
# import moud as gl
# import requests
# import re
#
#
# class APIException(Exception):
#     """Generic exception class for raising errors"""
#     pass
#
# class PUBGAPI:
#
#     userid = gl.get_value('name')
#     server = gl.get_value('server1')
#     url = 'http://192.168.0.94:8000/v2/profile/pc/' + userid + '?region=' + server + '&season=2017-pre4'
#
#     headers = {
#         'content-type': "application/json",
#         'trn-api-key': "f4717924-90de-4983-919c-985a36ddd30e",
#     }
#     r = requests.get(url, headers=headers)
#     sr = str(r.json())
#
#     ##用户头像
#     av_img = r.json()['avatar']
#     gl.set_value('img', av_img)
#
#     ## 获取游戏总时长
#     pubg_time1 = r.json()['timePlayed']
#     pubg_time = int(pubg_time1/60)
#
#     test = re.sub('\'', '\"', sr)
#     test = json.loads(test)
#
#
# #############################SOLO########################################
#     #1.打印KDA
#     solo_kda = test['stats'][0]['stats'][0]['displayValue']
#     gl.set_value('solo_kda',solo_kda)
#     print (solo_kda)
#
#     #2.最远击杀距离
#     solo_lang=test['stats'][0]['stats'][45]['displayValue']
#     gl.set_value('solo_lang', solo_lang)
#     print(solo_lang)
#
#     #3.打印存活时间
#     # s = test['stats'][0]['stats'][2]['value']
#     # t = int((round(float(s))/60)/60)
#     # print(t)
#
#     #4.打印回合数
#     solo_Rounds = test['stats'][0]['stats'][3]['displayValue']
#     gl.set_value('solo_rounds',solo_Rounds)
#     # print(Rounds)
#
#
#     #5.打印吃鸡数
#     solo_wins = test['stats'][0]['stats'][4]['displayValue']
#     gl.set_value('solo_wins',solo_wins)
#     print(solo_wins)
#
#     #6.打印进前十次数
#     solo_Top10 = test['stats'][0]['stats'][6]['displayValue']
#     gl.set_value('solo_top10',solo_Top10)
#     print(solo_Top10)
#
#     #7.打印评分
#     solo_Rting = test['stats'][0]['stats'][9]['displayValue']
#     gl.set_value('solo_rting',solo_Rting)
#     print(solo_Rting)
#
#     #8.打印最佳评分
#     solo_BestRting = test['stats'][0]['stats'][10]['displayValue']
#     gl.set_value('solo_bestrting', solo_BestRting)
#     print(solo_BestRting)
#
#     #9.打印最佳排名
#     solo_BestRank = test['stats'][0]['stats'][11]['value']
#     gl.set_value('solo_bestrank', solo_BestRank)
#     print(solo_BestRank)
#
#
#     #10.场均输出
#     solo_Dmg = test['stats'][0]['stats'][12]['value']
#     gl.set_value('solo_dmg', solo_Dmg)
#     print(solo_Dmg)
#
#
#     #11.爆头击杀
#     solo_Headshot = test['stats'][0]['stats'][26]['value']
#     gl.set_value('solo_headshot',solo_Headshot)
#     print(solo_Headshot)
#
#
#
#     #12.杀敌总数
#     solo_Kills = test['stats'][0]['stats'][22]['value']
#     gl.set_value('solo_kills',solo_Kills)
#     print(solo_Kills)
#     print('--------------------------------')
#
# #############################DUO#######################################
#     # 1.打印KDA
#     print(test['stats'][1]['stats'][0]['displayValue'])
#
#     # 2.打印吃鸡率
#     print(test['stats'][1]['stats'][1]['displayValue'])
#
#     # 3.打印存活时间
#     s = test['stats'][1]['stats'][2]['value']
#     t = int((round(float(s)) / 60) / 60)
#     print(t)
#
#     # 4.打印回合数
#     Rounds = test['stats'][1]['stats'][3]['displayValue']
#     print(Rounds)
#
#     # 5.打印吃鸡数
#     wins = test['stats'][1]['stats'][4]['displayValue']
#     print(wins)
#
#     # 6.打印进前十次数
#     Top10 = test['stats'][1]['stats'][6]['displayValue']
#     print(Top10)
#
#     # 7.打印评分
#     Rting = test['stats'][1]['stats'][9]['displayValue']
#     print(Rting)
#
#     # 8.打印最佳评分
#     BestRting = test['stats'][1]['stats'][10]['displayValue']
#     print(BestRting)
#
#     # 9.打印最佳排名
#     BestRank = test['stats'][1]['stats'][11]['value']
#     print(BestRank)
#
#     # 10.场均输出
#     Dmg = test['stats'][1]['stats'][12]['value']
#     print(Dmg)
#
#     # 11.爆头击杀
#     Headshot = test['stats'][1]['stats'][26]['value']
#     print(Headshot)
#
#     # 12.杀敌总数
#     Kills = test['stats'][1]['stats'][22]['value']
#     print(Kills)
#     print('----------------------')
#
# #############################SQUAD#######################################
#     # 1.打印KDA
#     print(test['stats'][2]['stats'][0]['displayValue'])
#
#     # 2.打印吃鸡率
#     print(test['stats'][2]['stats'][1]['displayValue'])
#
#     # 3.打印存活时间
#     s = test['stats'][2]['stats'][2]['value']
#     t = int((round(float(s)) / 60) / 60)
#     print(t)
#
#     # 4.打印回合数
#     Rounds = test['stats'][2]['stats'][3]['displayValue']
#     print(Rounds)
#
#     # 5.打印吃鸡数
#     wins = test['stats'][2]['stats'][4]['displayValue']
#     print(wins)
#
#     # 6.打印进前十次数
#     Top10 = test['stats'][2]['stats'][6]['displayValue']
#     print(Top10)
#
#     # 7.打印评分
#     Rting = test['stats'][2]['stats'][9]['displayValue']
#     print(Rting)
#
#     # 8.打印最佳评分
#     BestRting = test['stats'][2]['stats'][10]['displayValue']
#     print(BestRting)
#
#     # 9.打印最佳排名
#     BestRank = test['stats'][2]['stats'][11]['value']
#     print(BestRank)
#
#     # 10.场均输出
#     Dmg = test['stats'][2]['stats'][12]['value']
#     print(Dmg)
#
#     # 11.爆头击杀
#     Headshot = test['stats'][2]['stats'][26]['value']
#     print(Headshot)
#
#     # 12.杀敌总数
#     Kills = test['stats'][2]['stats'][22]['value']
#     print(Kills)
#
#     #############################SQUAD#######################################
#     # 1.打印KDA
#     print(test['stats'][2]['stats'][0]['displayValue'])
#
#     # 2.打印吃鸡率
#     print(test['stats'][2]['stats'][1]['displayValue'])
#
#     # 3.打印存活时间
#     s = test['stats'][2]['stats'][2]['value']
#     t = int((round(float(s)) / 60) / 60)
#     print(t)
#
#     # 4.打印回合数
#     Rounds = test['stats'][2]['stats'][3]['displayValue']
#     print(Rounds)
#
#     # 5.打印吃鸡数
#     wins = test['stats'][2]['stats'][4]['displayValue']
#     print(wins)
#
#     # 6.打印进前十次数
#     Top10 = test['stats'][2]['stats'][6]['displayValue']
#     print(Top10)
#
#     # 7.打印评分
#     Rting = test['stats'][2]['stats'][9]['displayValue']
#     print(Rting)
#
#     # 8.打印最佳评分
#     BestRting = test['stats'][2]['stats'][10]['displayValue']
#     print(BestRting)
#
#     # 9.打印最佳排名
#     BestRank = test['stats'][2]['stats'][11]['value']
#     print(BestRank)
#
#     # 10.场均输出
#     Dmg = test['stats'][2]['stats'][12]['value']
#     print(Dmg)
#
#     # 11.爆头击杀
#     Headshot = test['stats'][2]['stats'][26]['value']
#     print(Headshot)
#
#     # 12.杀敌总数
#     Kills = test['stats'][2]['stats'][22]['value']
#     print(Kills)
#
# #############################SQUAD FPP#######################################
#     # 1.打印KDA
#     print(test['stats'][2]['stats'][0]['displayValue'])
#
#     # 2.打印吃鸡率
#     print(test['stats'][2]['stats'][1]['displayValue'])
#
#     # 3.打印存活时间
#     s = test['stats'][2]['stats'][2]['value']
#     t = int((round(float(s)) / 60) / 60)
#     print(t)
#
#     # 4.打印回合数
#     Rounds = test['stats'][2]['stats'][3]['displayValue']
#     print(Rounds)
#
#     # 5.打印吃鸡数
#     wins = test['stats'][2]['stats'][4]['displayValue']
#     print(wins)
#
#     # 6.打印进前十次数
#     Top10 = test['stats'][2]['stats'][6]['displayValue']
#     print(Top10)
#
#     # 7.打印评分
#     Rting = test['stats'][2]['stats'][9]['displayValue']
#     print(Rting)
#
#     # 8.打印最佳评分
#     BestRting = test['stats'][2]['stats'][10]['displayValue']
#     print(BestRting)
#
#     # 9.打印最佳排名
#     BestRank = test['stats'][2]['stats'][11]['value']
#     print(BestRank)
#
#     # 10.场均输出
#     Dmg = test['stats'][2]['stats'][12]['value']
#     print(Dmg)
#
#     # 11.爆头击杀
#     Headshot = test['stats'][2]['stats'][26]['value']
#     print(Headshot)
#
#     # 12.杀敌总数
#     Kills = test['stats'][2]['stats'][22]['value']
#     print(Kills)
#
#
# #####################################################################
#
#
#
#     r.close()
