import os
import random
import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import otvity as ot

# проверка на выигрыш

def isWin(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False

#пересчет пустых клеток
def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == ot.SYMBOL_UNDEF:
            counter += 1
    return counter

def gameX(callBackData):
    message = ot.ANSW_YOUR_TURN  
    alert = None

    buttonNumber = int(callBackData[0])  
    if not buttonNumber == 9: 
        charList = list(callBackData)  
        charList.pop(0)  
        if charList[buttonNumber] == ot.SYMBOL_UNDEF:  
            charList[buttonNumber] = ot.SYMBOL_X  
            if isWin(charList, ot.SYMBOL_X):  
                message = ot.ANSW_YOU_WIN
            else:  
                if countUndefinedCells(charList) != 0: 
                    isCycleContinue = True
                    while (isCycleContinue):
                        rand = random.randint(0, 8)
                        #бот занимает первым ходом середину если она
                        if   charList[rand] == ot.SYMBOL_UNDEF:
                            if charList[4] ==ot.SYMBOL_UNDEF  :
                                    charList[4]= ot.SYMBOL_O
                                    isCycleContinue = False
                            else:
                                    charList[rand] = ot.SYMBOL_O
                                    isCycleContinue = False  
                            if isWin(charList, ot.SYMBOL_O):  
                                    message = ot.ANSW_BOT_WIN
        else:
            alert = ot.ALERT_CANNOT_MOVE_TO_THIS_CELL

        if countUndefinedCells(charList) == 0 and message == ot.ANSW_YOUR_TURN:
            message = ot.ANSW_DRAW

        callBackData = ''
        for c in charList:
            callBackData += c

    if message == ot.ANSW_YOU_WIN or message == ot.ANSW_BOT_WIN or message == ot.ANSW_DRAW:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  

    return message, callBackData, alert

def getKeyboard(callBackData):
    keyboard = [[], [], []]  

    if callBackData != None:  
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))

    return keyboard


def newGame(update, _):
    data = ''
    for i in range(0, 9):
        data += ot.SYMBOL_UNDEF

    update.message.reply_text(ot.ANSW_YOUR_TURN, reply_markup=InlineKeyboardMarkup(getKeyboard(data)))


def button(update, _):
    query = update.callback_query
    callbackData = query.data 

    message, callbackData, alert = gameX(callbackData)  # игра
    if alert is None:  
        query.answer()  
        query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    else: 
        query.answer(text=alert, show_alert=True)


def help_command(update, _):
    update.message.reply_text(ot.ANSW_HELP)


if __name__ == '__main__':
    updater = Updater('5513051245:AAFvnniswYH4Z6Idong-weopDsAasoADS1Y')
    dispatcher=updater.dispatcher  
    dispatcher.add_handler(CommandHandler('start', newGame))
    dispatcher.add_handler(CommandHandler('new_game', newGame))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, help_command))  
    dispatcher.add_handler(CallbackQueryHandler(button))
    

    

    print('server start')
    updater.start_polling()
    updater.idle()