# This module is imported so that we can  
# play the converted audio 

import os 
import requests

## Get Telegram API Token
token = os.environ.get('TELEGRAM_API_TOKEN')


## Function to sendMessage to Telegram
def sendTTS(chat_id='509161525', text='Hello', token=token, lang='en', url=''):  ## Specify chat_id and text message
    
    params = {
        'api_url':"https://api.telegram.org",
        'action':'sendAudio',
        'token': token,
        'chat_id': chat_id,
        'tts_url': f'https://translate.google.com/translate_tts?tl={lang}&q={text}&client=tw-ob',
        #'tts_url': "https://www.myinstants.com/media/sounds/gta-v-death-sound-effect-102.mp3",
        #'tts_url': "https://www.myinstants.com/media/sounds/nouveau-jingle-netflix.mp3",
        'caption' : ''
        #'tts_url': "https://www.myinstants.com/media/sounds/la-boule-noire-de-motus.mp3"
        #play('/media/sounds/crazy-realistic-knocking-sound-trim.mp3')

    }
    print(params['tts_url'])
    req = requests.get(f"{params['api_url']}/bot{params['token']}/{params['action']}?chat_id={params['chat_id']}&audio={params['tts_url']}")
    return req.json()

if __name__ == '__main__':
    print(sendTTS(text="Tout est beau", token=token, lang="fr"))