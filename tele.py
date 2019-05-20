#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
import redis
import telebot

bot = telebot.TeleBot("862223389:AAGA76iwm7ZgdBKCHvOUnu2gjL2rwYfVYXA")

pool = redis.ConnectionPool(host='149.129.115.88',
                            port=6379,
                            db=0,
                            password='foobared')

r = redis.Redis(connection_pool=pool)


@bot.message_handler(commands=['init'])
def _init(message):
    for i in [
            'payload', 'temperature', 'humidity', 'concentration', 'brightness'
    ]:
        r.set(i, 0)
    bot.reply_to(message, '初始化完成')


@bot.message_handler(commands=['open'])
def _open(message):
    r.set('payload', 1)
    bot.reply_to(message, 'payload == 1')


@bot.message_handler(commands=['close'])
def _close(message):
    r.set('payload', 0)
    bot.reply_to(message, 'payload == 0')


@bot.message_handler(commands=['check'])
def _check(message):
    bot.reply_to(
        message, '温度:' + str(float(r.get('temperature'))) + '\n' + '湿度:' +
        str(float(r.get('humidity'))) + '\n' + 'co浓度:' +
        str(float(r.get('concentration'))) + '\n' + '火光强度:' +
        str(float(r.get('brightness'))) + '\n' + 'payload:' +
        str(float(r.get('payload'))))


bot.polling()
