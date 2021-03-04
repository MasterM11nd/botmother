from example.keyboards import *


def start(chat, redirect, **kwargs):
    chat.send_message('Hi {name}'.format(name=chat.first_name))
    kwargs['extra'] = {}
    redirect(menu, **kwargs)


def menu(chat, **kwargs):
    chat.send_message('I am a BotMother for creating telegram bots')
    response = chat.send_message('How are you?', reply_markup=inline_menu('is-chosen'))
    chat.last_data = {'message_id': response.get('result', {}).get('message_id')}


def last(chat, callback_data, *args, **kwargs):
    if callback_data:
        chat.delete_message(message_id=chat.last_data.get('message_id'))
        chat.send_message('Cool!' if callback_data.get('value') else 'Why so sad?')


def unknown(chat, *args, **kwargs):
    chat.send_message('{name}, I do not understand you!'.format(name=chat.first_name))
