import json
import requests
 
api = 'http://www.tuling123.com/openapi/api?key=067ba9cdb58d48679ad776bc566141d0&info='
 
def getHtml(quesion):
    url = api + quesion
    r = requests.get(url)
    r.encoding = 'utf8'
    return r.text
 
def onQQMessage(bot, contact, member, content):
    response = getHtml(content)
	print(response)
    dic_json = json.loads(response)
    answer = dic_json['text']
	print(answer)
	bot.SendTo(contact, answer)

