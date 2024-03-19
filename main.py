from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import os
from findImage import get_image
from typing import List

load_dotenv()
TOKEN = os.getenv("TOKEN")
processed_list = []


#Commands
async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")
    
async def help_command(update:Update,context: ContextTypes.DEFAULT_TYPE,):
    await update.message.reply_text("HELP me!")


async def custom_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("GOODBYE!!!")  
    
async def button_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    back_btn = InlineKeyboardButton("Download image!", callback_data='button_click')
    search_btn = InlineKeyboardButton("Search again!", callback_data='button_click')
    markup = InlineKeyboardMarkup([[back_btn,search_btn]])
    await update.message.reply_text('Please choose:', reply_markup=markup)
    
#Responses 
#Handle Response must change
def handle_response(text:str,update:Update,processed_list: List[str])->str or InlineKeyboardMarkup: # type: ignore
    processed: str = text.lower()
    processed_list.append(text.lower())
    cmd_exists = "find image" in processed_list
    if 'find image' in processed:
        return "Write a picture name: "
    if cmd_exists:
        return get_image(update.message.text)
    return 'I dont understand the command!!!'  

async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        return
    else:
        response: str= handle_response(text,update,processed_list)
    print('Bot:',response)
    await update.message.reply_text(response)
    
    
async def error_handler(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error } ')
    
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    
    
    #Commands
    app.add_handler(CommandHandler('button',button_command))
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    
    
    
    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    
    
    #Errors
    app.add_error_handler(error_handler)
    
    print("Polling....")
    app.run_polling(poll_interval=3)
    
        