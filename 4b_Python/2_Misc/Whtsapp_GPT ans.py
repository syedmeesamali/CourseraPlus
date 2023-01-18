import pywhatkit

time = "16:37:15"
phone_number = "123456789"
message = "This is a message from Whatsapp BOT via Python"
#pywhatkit.sendwhatmsg(time, phone_number, message)
pywhatkit.sendwhatmsg(phone_number, message, 16, 43)