from highrise.__main__ import *
import time


bot_file_name = "vip"
bot_class_name = "Bot"
room_id = "659cdef101602e72c92bbd5a"
bot_token = "04809b05cb717d3d4051c7cc7750032dd4a902e2956ad775e31ae6d4a7ee4464"


my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occourred: {e}")
        time.sleep(5)
