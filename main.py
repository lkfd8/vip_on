from highrise.__main__ import *
import time


bot_file_name = "vip"
bot_class_name = "Bot"
room_id = "654b2ec6c001073820d9bbef"
bot_token = ""


my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occourred: {e}")
        time.sleep(5)