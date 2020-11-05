  #installing module pywin32
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)  #this is the exact code from pywin32

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')  #apikey

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])
