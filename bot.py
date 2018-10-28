import requests
import misc
import json

token = misc.token

# https://api.telegram.org/bot716310445:AAEHoOyWSyOBWcbZdiD6c5LEESxKD8Z3_fA/sendmessage?chat_id=275330781&text=test
URL = 'https://api.telegram.org/bot' + token + '/'
# print('URL -->', URL)


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'message_text': message_text}
    return message


def send_message(chat_id, text='Подождите секундочку пожалуйста...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)
    print(url)


def main():
    # d = get_updates()

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    # print(send_message(13))
    answer = get_message()
    chat_id = answer['chat_id']

    send_message(chat_id, 'Что ты хочешь на ужин?')



if __name__ == '__main__':
    main()
