# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.speak(str)


if __name__ == '__main__':
    from pip._vendor import requests
    import json

    url = "https://newsapi.org/v2/everything?q=+'linux'&apiKey=e153b64d6ea64ee8b31b8b770e34e7c9"
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)

    for i in range(0, 11):
        print(my_json['articles'][i]['description'])
        print('\n')
