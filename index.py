import json
import re

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_word():
    return render_template('search.html')


@app.route('/search', methods=['GET'])
def s_id():
    if request.method == "GET":
        # userid = request.form.get('id')
        userid = request.args.get('id')
        print(userid)
        # server = request.form.get('server1')
        # sj = request.form.get('sj')
        # print(sj)
        # dq = request.form.get('dq')
        # print(dq)
        # url = 'https://api.pubgtracker.com/v2/profile/pc/' + userid + '?region=' + dq + '&season=' + sj
        url = 'http://192.168.0.94:8000/v2/profile/pc/' + userid + '?region=as&season=2017-pre5'
        # url = 'http://google.com/v2/profile/pc/' + userid + '?region=' + dq + '&season=' + sj
        headers = {
            'content-type': "application/json",
            'trn-api-key': "your-key",
        }
        r = requests.get(url, headers=headers)
        sr = str(r.json())
        test = re.sub('\'', '\"', sr)
        test = json.loads(test)
    return render_template('so.html',
                           pubg_img=r.json()['avatar'],
                           update=r.json()['lastUpdated'],
                           userid=userid,
                           ##########solo#########
                           #游戏时长
                           pubg_solo_time=int(float(test['stats'][0]['stats'][2]['value'])/3600),

                           #KDA和KDA率
                           pubg_solo_kda= test['stats'][0]['stats'][0]['displayValue'],
                           pubg_solo_kda1=float(test['stats'][0]['stats'][0]['displayValue'])*3,

                           #胜率和胜率排名
                           pubg_solo_sl=test['stats'][0]['stats'][1]['displayValue'],
                           pubg_solo_sl1=int(100-(100/(float(test['stats'][0]['stats'][1]['value'])))),



                           pubg_solo_lang=test['stats'][0]['stats'][45]['displayValue'],
                           pubg_solo_rounds=test['stats'][0]['stats'][3]['displayValue'],
                           pubg_solo_wins=test['stats'][0]['stats'][4]['displayValue'],

                           #前十率
                           pubg_solo_top10=test['stats'][0]['stats'][6]['value'],
                           pubg_solo_top101=int(100 - (100 / (float(test['stats'][0]['stats'][6]['value'])))),


                           pubg_solo_rting=int(test['stats'][0]['stats'][9]['value']),
                           pubg_solo_rting1=(float(test['stats'][0]['stats'][9]['value'])/100)+13,

                           pubg_solo_bestrting=test['stats'][0]['stats'][10]['displayValue'],
                           pubg_solo_bestrank=test['stats'][0]['stats'][11]['value'],
                           pubg_solo_dmg=test['stats'][0]['stats'][12]['value'],
                           pubg_solo_headshot=test['stats'][0]['stats'][26]['value'],
                           pubg_solo_kills=test['stats'][0]['stats'][22]['value'],
                           pubg_solo_assists =test['stats'][0]['stats'][23]['value'],
                           pubg_solo_suicides =test['stats'][0]['stats'][24]['value'],
                           pubg_solo_winb=test['stats'][0]['stats'][1]['displayValue'],
                           ##########duo#########
                           pubg_duo_kda=test['stats'][1]['stats'][0]['displayValue'],
                           pubg_duo_lang=test['stats'][1]['stats'][45]['displayValue'],
                           pubg_duo_rounds=test['stats'][1]['stats'][3]['displayValue'],
                           pubg_duo_wins=test['stats'][1]['stats'][4]['displayValue'],
                           pubg_duo_top10=test['stats'][1]['stats'][6]['displayValue'],
                           pubg_duo_rting=test['stats'][1]['stats'][9]['displayValue'],
                           pubg_duo_bestrting=test['stats'][1]['stats'][10]['displayValue'],
                           pubg_duo_bestrank=test['stats'][1]['stats'][11]['value'],
                           pubg_duo_dmg=test['stats'][1]['stats'][12]['value'],
                           pubg_duo_headshot=test['stats'][1]['stats'][26]['value'],
                           pubg_duo_kills=test['stats'][1]['stats'][22]['value'],
                           pubg_duo_assists=test['stats'][1]['stats'][23]['value'],
                           pubg_duo_suicides=test['stats'][1]['stats'][24]['value'],
                           pubg_duo_winb=test['stats'][1]['stats'][1]['displayValue'],
                           ##########squad#########
                           pubg_squad_kda=test['stats'][2]['stats'][0]['displayValue'],
                           pubg_squad_lang=test['stats'][2]['stats'][45]['displayValue'],
                           pubg_squad_rounds=test['stats'][2]['stats'][3]['displayValue'],
                           pubg_squad_wins=test['stats'][2]['stats'][4]['displayValue'],
                           pubg_squad_top10=test['stats'][2]['stats'][6]['displayValue'],
                           pubg_squad_rting=test['stats'][2]['stats'][9]['displayValue'],
                           pubg_squad_bestrting=test['stats'][2]['stats'][10]['displayValue'],
                           pubg_squad_bestrank=test['stats'][2]['stats'][11]['value'],
                           pubg_squad_dmg=test['stats'][2]['stats'][12]['value'],
                           pubg_squad_headshot=test['stats'][2]['stats'][26]['value'],
                           pubg_squad_kills=test['stats'][2]['stats'][22]['value'],
                           pubg_squad_assists=test['stats'][2]['stats'][23]['value'],
                           pubg_squad_suicides=test['stats'][2]['stats'][24]['value'],
                           pubg_squad_winb=test['stats'][2]['stats'][1]['displayValue'],

                           )

# @app.errorhandler(500)
# def permisson_denied(e):
#     return render_template('500.html'),500

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()