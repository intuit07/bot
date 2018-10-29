import requests
import misc

from time import sleep

from yobit import get_btc

token = misc.token

# https://api.telegram.org/bot716310445:AAEHoOyWSyOBWcbZdiD6c5LEESxKD8Z3_fA/sendmessage?chat_id=275330781&text=test
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0




def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    #отвечать только на новые сообщения
    # получаем update_id, каждого обновления
    # записываем в переменную, а затем сравнить
    # с update_id последнего елемента в списке result

    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        chat_id = data['result'][-1]['message']['chat']['id']
        message_text = data['result'][-1]['message']['text']
        message = {'chat_id': chat_id,
                   'text': message_text}
        return message
    return None


def send_message(chat_id, text='Подождите секундочку пожалуйста...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():

    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue

            sleep(3)

if __name__ == '__main__':
    main()
