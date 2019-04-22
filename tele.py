#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
import formaters
import telebot

bot = telebot.TeleBot("786276948:AAEwplAQNpcEF5BtObF4dQ6_gnh7gADjJ4w")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, {"te": 35, "sd": 23})


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
