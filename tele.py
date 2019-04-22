#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
import formaters
import telebot
from telebot import types

bot = telebot.TeleBot("786276948:AAEwplAQNpcEF5BtObF4dQ6_gnh7gADjJ4w")

vara = "tempature(C)"
varb = "humidity(RH%)"
varc = "concentration(PPM)"


def echoString(var):
    return var + str(formaters.readJson('data.json')[var])


def echoParmers(var):
    return str(formaters.readJson('data.json')[var])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        echoString(vara) + '\n' + echoString(varb) + '\n' + echoString(varc))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if (message == "open"):
        formaters.writeJson('data.json', echoParmers(vara), echoParmers(varb),echoParmers(varc), "1")
    else if(message == "close"):
        formaters.writeJson('data.json', echoParmers(vara), echoParmers(varb),echoParmers(varc), "0")
    else:
        bot.reply_to(message, message.text)


bot.polling()
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('open')
itembtn2 = types.KeyboardButton('close')
markup.add(itembtn1, itembtn2)
tb.send_message(chat_id, "Choose the open or close", reply_markup=markup)
