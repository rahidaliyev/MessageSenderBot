import pywhatkit as pwk
def send_message(link):
    try:
        pwk.sendwhatmsg_instantly('+994703558057',link,5,tab_close=True);
        print("Message sent!");
    except:
        print("Error in sending message!")