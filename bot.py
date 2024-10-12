from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

TOKEN:Final ="7159800649:AAFhQHVQ05rM5LSIyFOTI8murbOHswXm56w"
BOT_USERNAME:Final="@FirsstTrybot"

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):  #menu wale option me use karne ke liye 
    await update.message.reply_text("Hello world")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm here to help you,what is your problem")

async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is a custom command")

def handle_response(text:str)->str:  
    processed:str=text.lower()  #jo bhi message aayega usko lowercase me dalenge aur fir process aage jayega
    if 'hello' in processed:
        return "hey there"
    if 'how are you' in processed:
        return 'i am good'
    if 'i love python' in processed:
        return 'remember to subscribe'
    return 'i do not understand what you wrote'

async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str=update.message.chat.type   #group hai ya individual
    text:str=update.message.text  #jo message chat me user likhanga

    print(f'User ({update.message.chat.id}) in {message_type} : {text}')  #console meoutput aayega info ke sath

    if message_type=='group':
        if BOT_USERNAME in text:
            new_text:str=text.replace(BOT_USERNAME,'').strip() #@FirsstTry hello isko todenge botname ko replace karenge khali jagah se fir extra jitni bhi space hogi wo nikal denge
            response:str=handle_response(new_text)
        else:
            return
    else:
        response:str=handle_response(text)

    print('Bot:',response)
    await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=='__main__':
    app=Application.builder().token(TOKEN).build

    print("program start...")
    app.add_handlers(CommandHandler('start',start_command))
    app.add_handlers(CommandHandler('help',help_command))
    app.add_handlers(CommandHandler('custom',custom_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print("polling....")
    app.run_polling(poll_interval=3)