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
            'npayload', 'temperature', 'humidity', 'concentration',
            'brightness', 'payload'
    ]:
        r.set(i, 0)
    bot.reply_to(message, '初始化完成')


@bot.message_handler(commands=['open'])
def _open(message):
    r.set('npayload', 1)
    bot.reply_to(message, 'npayload == 1,已启动')


@bot.message_handler(commands=['close'])
def _close(message):
    r.set('npayload', 0)
    bot.reply_to(message, 'npayload == 0,已关闭')


@bot.message_handler(commands=['check'])
def _check(message):
    bot.reply_to(
        message, '温度:' + str(float(r.get('temperature'))) + '\n' + '湿度:' +
        str(float(r.get('humidity'))) + '\n' + 'co浓度:' +
        str(float(r.get('concentration'))) + '\n' + '火光触发:' +
        str(float(r.get('brightness'))) + '\n' + 'npayload:' +
        str(int(r.get('npayload'))) + '\n' + 'payload:' +
        str(int(r.get('payload'))))


@bot.message_handler(commands=['monitor'])
def _monior(message):
    bot.send_message(message.chat.id, '监控已开启')
    for i in range(0, 3):
        if (int(r.get('payload'))):
            bot.send_message(533370918, '警告！！！')


bot.polling()
