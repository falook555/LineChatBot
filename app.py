from flask import Flask , request

app  = Flask(__name__)
line_access_token = 'VOen3avsKzvA/CdQlf6NiDPDPNzUW6LyEs4aoii4eF3MlOKgQa6ApZwzFMMcvXt2lVo6NDv9n8tw6ZOFM9/kyvyQ8XcnBk1ykV9oskL9/xxNBSRKi2ZAob32fDkkLskIfVrUW2NKQ5kwabWFOIibFwdB04t89/1O/w1cDnyilFU='

@app.route('/')

def home():
    return 'Hello This is Get Method By Konthorn Thonsap'

@app.route('/webhook',methods=['POST','GET'])
def webhook():
    if request.method == 'GET':      # check method
        return 'Your aer in Method'

    elif request.method == 'POST':   # check method
        data = request.get_json()    # รับข้อมูลรูปแบบ Json
        text = data['events'][0]['message']['text']  
        reply_token = data['events'][0]['replyToken']
        print('text :' + text)
        print('reply_token' + reply_token)
        from Resource.wolf import search_wiki
        reply_msg = search_wiki(keyword='ff')

        from Resource.reply import ReplyMessage
        ReplyMessage(Reply_token = reply_token , TextMessage = reply_msg , Line_Access_Token = line_access_token)

        print(data)
        return 'OK'

if __name__ == '__main__':
    app.run(port=8000)
    