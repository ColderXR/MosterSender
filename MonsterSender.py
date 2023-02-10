from aminofix import *
from webbrowser import *
from requests import *
from colorama import Fore as Fe
from pyfiglet import figlet_format as ft
from random import choice
from getpass import getpass
Input = getpass
# =========== Start Code =========== #
Names = ['هلا','مستر سلطع','هكر رهيب','سفاح المصري هو امنجس','سفاح العرب هو البعبع','كينج مدارا']
print(Fe.RED+ft('NotEver','small'))
Email = Input(Fe.LIGHTRED_EX+'[=] Email ? : ')
Password = Input(Fe.LIGHTRED_EX+'[=] Password : ')
MyClient = Client()
MyClient.login(Email,Password)
ChatLink = MyClient.get_from_code(input(Fe.LIGHTRED_EX+'[=] ChatLink ? : '))
MyLocal = SubClient(ChatLink.comId,profile=MyClient.profile)
# =========== Start Attack  =========== #
while True: MyLocal.edit_profile(choice(Names));MyLocal.join_chat(ChatLink.objectId);MyLocal.leave_chat(ChatLink.objectId);print('Done Spam !')
