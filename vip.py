import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise.models import Item, SessionMetadata, User, CurrencyItem
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from webserver import keep_alive
import os
from datetime import datetime, timedelta
import json


moderators = ['RONY.28','Lara__a','WEGZ_kr','YZAM','ABO_3LI','X_BERO','N5B','Is1am',"zilo9","_M_11","zilo9","chillari_","FIRE_ON_PC"]
moderator = ['RONY.28','Lara__a','WEGZ_kr','YZAM','ABO_3LI','X_BERO','N5B','Is1am',"zilo9","_M_11","zilo9","chillari_","FIRE_ON_PC"]

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token




class Bot(BaseBot):
    cooldowns = {}  # Class-level variable to store cooldown timestamps

    def __init__(self):
        super().__init__()
        self.load_moderators()
        self.load_moderator()
        self.load_temporary_vips()
        self.load_1week_vips()
        self.load_1month_vips()

    def load_moderator(self):
        try:
            with open("moderator.json", "r") as file:
                self.moderator = json.load(file)
        except FileNotFoundError:
            self.moderator = []

        # Add default moderators here
        default_moderator = ['RONY.28','Lara__a','WEGZ_kr','YZAM','ABO_3LI','X_BERO','N5B','Is1am',"zilo9","_M_11","zilo9","chillari_","FIRE_ON_PC"]
        for mod in default_moderator:
            if mod.lower() not in self.moderator:
                self.moderator.append(mod.lower())
    def save_moderator(self):
        with open("moderator.json", "w") as file:
            json.dump(self.moderators, file) 

    def load_1week_vips(self):
        try:
            with open("1week.json", "r") as file:
                self.weekly_vips = json.load(file)
        except FileNotFoundError:
            self.weekly_vips = {}

    def save_1week_vips(self):
        with open("1week.json", "w") as file:
            json.dump(self.weekly_vips, file)

    def load_1month_vips(self):
        try:
            with open("1month.json", "r") as file:
                self.monthly_vips = json.load(file)
        except FileNotFoundError:
            self.monthly_vips = {}
    def save_1month_vips(self):
        with open("1month.json", "w") as file:
            json.dump(self.monthly_vips, file)

    def load_temporary_vips(self):
        try:
            with open("temporary.json", "r") as file:
                self.temporary_vips = json.load(file)
        except FileNotFoundError:
            self.temporary_vips = {}

    def save_temporary_vips(self):
        with open("temporary.json", "w") as file:
            json.dump(self.temporary_vips, file)

    def load_moderators(self):
        try:
            with open("moderators.json", "r") as file:
                self.moderators = json.load(file)
        except FileNotFoundError:
            self.moderators = []


        # Add default moderators here
        default_moderators = ['RONY.28','Lara__a','WEGZ_kr','YZAM','ABO_3LI','X_BERO','N5B','Is1am',"zilo9","_M_11","zilo9","chillari_","FIRE_ON_PC"]
        for mod in default_moderators:
            if mod.lower() not in self.moderators:
                self.moderators.append(mod.lower())

    def save_moderators(self):
        with open("moderators.json", "w") as file:
            json.dump(self.moderators, file) 

    def remaining_time(self, username):
        if username in self.temporary_vips:
            remaining_seconds = self.temporary_vips[username] - int(time.time())
            if remaining_seconds > 0:
                return str(timedelta(seconds=remaining_seconds))
        return "Not a temporary VIP."

    def rmaining_time(self, username):
        if username in self.weekly_vips:
            remaining_seconds = self.weekly_vips[username] - int(time.time())
            if remaining_seconds > 0:
                return str(timedelta(seconds=remaining_seconds))
        return "Not a weekly VIP."
    def raining_time(self, username):
        if username in self.monthly_vips:
            remaining_seconds = self.monthly_vips[username] - int(time.time())
            if remaining_seconds > 0:
                return str(timedelta(seconds=remaining_seconds))
        return "Not a monthly VIP."



    async def on_start(self, session_metadata: SessionMetadata) -> None: 
        print("vip neww is Booting...") 
        self.highrise.tg.create_task(self.highrise.teleport(session_metadata.user_id, Position(x=9.5, y=5.75, z=5.5, facing='FrontRight')))




    async def on_user_join(self, user: User, position: Position  | AnchorPosition) -> None: 

     try:

        await self.highrise.react("heart", user.id)
        emotes_list = ["emote-kiss","emote-no","emote-sad","emote-yes","emote-laughing","emote-hello","emote-wave","emote-shy","emote-tired","emoji-angry","idle-loop-sitfloor","emoji-thumbsup","emote-lust","emoji-cursing","emote-greedy","emoji-flex","emoji-gagging","emoji-celebrate","dance-macarena","dance-tiktok8","dance-blackpink","emote-model","dance-tiktok2","dance-pennywise","emote-bow","dance-russian","emote-curtsy","emote-snowball","emote-hot","emote-snowangel","emote-charging","dance-shoppingcart","emote-confused","idle-enthusiastic","emote-telekinesis","emote-float","emote-teleporting","emote-swordfight","emote-maniac","emote-energyball","emote-snake","idle_singing","emote-superpose","emote-cute","dance-tiktok9","dance-weird","dance-tiktok10","emote-pose7","emote-pose8","idle-dance-casual","emote-pose1","emote-pose3","emote-pose5","emote-cutey"]
        random_emote = random.choice(emotes_list)

        await self.highrise.send_emote(random_emote)
        await self.highrise.send_whisper(user.id, f"ابعتلي 10 تاخد 24 ساعه اكتب فيها Vip وهدخلك Vip جرب مش هتخس حاجه وابقى بص عالبايو بتاعي وهتفهم احسن{user.username}")
     except Exception as e:
            print(f"An exception occured: {e}") 
    async def on_chat(self, user: User, message: str) -> None:
     try:


        if message.startswith("اسعار"):
                await self.highrise.send_whisper(user.id,"اسعار Vip اتبرع للبوت واحصل عليها:\n"
                                         "Vip - 1g لمره واحده Vip\n"
                                         "Vip - 10g مقابل 24 ساعه Vip\n"
                                         "Vip - 50g مقابل 1 اسبوع Vip\n"
                                         "Vip - 500g مقابل 1 شهر Vip\n"
                                         "Vip - 1000g مقابل  Vip لا محدوده")

        if message.startswith("mod"):
                if user.username.lower() in self.moderator:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                   await self.highrise.teleport(user.id,Position(x=12.5, y=15.25, z=18.5, facing='FrontRight'))                                    
                                   break
                        except:
                            pass
                    else:
                     await self.highrise.teleport(user.id,Position(x=12.5, y=15.25, z=18.5, facing='FrontRight')) 
        if message.startswith("Mod"):
                if user.username.lower() in self.moderator:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                   await self.highrise.teleport(user.id,Position(x=12.5, y=15.25, z=18.5, facing='FrontRight'))                                    
                                   break
                        except:
                            pass
                    else:
                     await self.highrise.teleport(user.id,Position(x=12.5, y=15.25, z=18.5, facing='FrontRight'))

        if message.startswith("Vip"):
                if user.username.lower() in self.temporary_vips:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    if int(time.time()) - self.temporary_vips[user.username.lower()] < 2:
                                        await self.highrise.teleport(u.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                        break
                        except:
                            pass
                    else:
                        if int(time.time()) - self.temporary_vips[user.username.lower()] < 2:
                            await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))


        if message.startswith("vip"):
                if user.username.lower() in self.temporary_vips:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    if int(time.time()) - self.temporary_vips[user.username.lower()] < 2:
                                        await self.highrise.teleport(u.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                        break
                        except:
                            pass
                    else:
                        if int(time.time()) - self.temporary_vips[user.username.lower()] < 2:
                            await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))




        if message.startswith("vip"):
                if user.username.lower() in self.moderators:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    await self.highrise.teleport(u.id,  Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                    break
                        except:
                            pass
                    else:
                     await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
        if message.startswith("Vip"):
                if user.username.lower() in self.moderators:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    await self.highrise.teleport(u.id,  Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                    break
                        except:
                            pass
                    else:
                     await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))





        if message.startswith("vip"):
                if user.username.lower() in self.monthly_vips:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    if int(time.time()) - self.monthly_vips[user.username.lower()] < 2:
                                        await self.highrise.teleport(u.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                        break
                        except:
                            pass
                    else:
                        if int(time.time()) - self.monthly_vips[user.username.lower()] < 2:
                            await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))

        if message.startswith("Vip"):
                if user.username.lower() in self.monthly_vips:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    if int(time.time()) - self.monthly_vips[user.username.lower()] < 2:
                                        await self.highrise.teleport(u.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                        break
                        except:
                            pass
                    else:
                        if int(time.time()) - self.monthly_vips[user.username.lower()] < 2:
                            await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))


        if message.startswith("vip"):
                if user.username.lower() in self.weekly_vips:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    if int(time.time()) - self.weekly_vips[user.username.lower()] < 2:
                                        await self.highrise.teleport(u.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                        break
                        except:
                            pass
                    else:
                        if int(time.time()) - self.weekly_vips[user.username.lower()] < 2:
                            await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))

        if message.startswith("Vip"):
                if user.username.lower() in self.weekly_vips:
                    split = message.split()
                    if len(split) == 2:
                        name = split[1].lower()
                        response = await self.highrise.get_room_users()
                        users = [content[0] for content in response.content]
                        try:
                            for u in users:
                                u_give = str("@") + str((u.username).lower())
                                if str((u_give).lower()).strip() == str(name).strip():
                                    if int(time.time()) - self.weekly_vips[user.username.lower()] < 2:
                                        await self.highrise.teleport(u.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))
                                        break
                        except:
                            pass
                    else:
                        if int(time.time()) - self.weekly_vips[user.username.lower()] < 2:
                            await self.highrise.teleport(user.id, Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))


        if message.startswith("وقت"):
                if user.username.lower() in self.temporary_vips:
                    parts = message.split()
                    if len(parts) == 2:
                        target_mention = parts[1]

                # Remove the "@" symbol if present
                        target_user = target_mention.lstrip('@')

                # Check if the target user has temporary VIP status
                        remaining_time = self.remaining_time(target_user.lower())
                        await self.highrise.send_whisper(user.id, f"{remaining_time} - {target_mention}")

                    else:
                        await self.highrise.send_whisper(user.id, "الاستخدام: وقت @اليوزر")
        if message.startswith("وقت"):
                if user.username.lower() in self.weekly_vips:

                    parts = message.split()
                    if len(parts) == 2:
                        target_mention = parts[1]

                        # Remove the "@" symbol if present
                        target_user = target_mention.lstrip('@')

                        # Check if the target user has temporary VIP status
                        rmaining_time = self.rmaining_time(target_user.lower())
                        await self.highrise.send_whisper(user.id, f"{rmaining_time} - {target_mention}")

                    else:
                        await self.highrise.send_whisper(user.id, "الاستخدام: وقت @اليوزر")
        if message.startswith("وقت"):
                if user.username.lower() in self.monthly_vips:

                    parts = message.split()
                    if len(parts) == 2:
                        target_mention = parts[1]

                        # Remove the "@" symbol if present
                        target_user = target_mention.lstrip('@')

                        # Check if the target user has temporary VIP status
                        raining_time = self.raining_time(target_user.lower())
                        await self.highrise.send_whisper(user.id, f"{raining_time} - {target_mention}")


                    else:
                        await self.highrise.send_whisper(user.id, "الاستخدام: وقت @اليوزر")


        if  message.startswith("Wallet"):
            if user.username in moderators :

                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.send_whisper(user.id, f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

            else: 
                await  self.highrise.send_whisper(user.id, f"Only Moderators Can View the Wallet")
     except Exception as e:
            print(f"An exception occured: {e}")





    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem) -> None:
        try:
           if receiver.username == "VIPDISCO" and tip.amount == 1000:
                        await self.highrise.chat(f"اشتريت 👑واحده👑 VIP كامله {sender.username} \nقول vip عشان تطلع")
                        sender_username = sender.username.lower()
                        if sender_username in self.moderators:
                            self.moderators.append(sender_username)
                            self.save_moderators()

           elif receiver.username == "VIPDISCO" and tip.amount == 10:
                        await self.highrise.chat(f" اشتريت 🎩واحده🎩 VIP, لمده  24h {sender.username} \nقول vip عشان تطلع")           
                        sender_username = sender.username.lower()
                        self.temporary_vips[sender_username] = int(time.time()) + 24 * 60 * 60  # VIP for 24 hours
                        self.save_temporary_vips()


           elif receiver.username == "VIPDISCO" and tip.amount == 50:  # Assuming tip.amount is in gold for 1 week
                    await self.highrise.chat(f"اشتريت 🌟1-اسبوع VIP {sender.username} \nقول vip عشان تطلع")
                    sender_username = sender.username.lower()
                    self.weekly_vips[sender_username] = int(time.time()) + 7 * 24 * 60 * 60  # VIP for 1 week
                    self.save_1week_vips()
           elif receiver.username == "VIPDISCO" and tip.amount == 500:  # Assuming tip.amount is in gold for 1 month
                    await self.highrise.chat(f"اشتريت 🌟1-شهر🌟 VIP {sender.username} \nقول vip عشان تطلع")
                    sender_username = sender.username.lower()
                    self.monthly_vips[sender_username] = int(time.time()) + 30 * 24 * 60 * 60  # VIP for 1 month
                    self.save_1month_vips()
           elif receiver.username == "VIPDISCO" and tip.amount == 1:
                    await self.highrise.chat(f"دخلت VIP 🎩 لمره واحده {sender.username}")
                    await self.highrise.teleport(sender.id,Position(x=10.5, y=5.75, z=6.5, facing='FrontLeft'))                                 


        except Exception as e:
            print(f"An exception occured: {e}") 




    async def on_user_move(self, user: User, pos: Position) -> None:
        try:

            if user.username == "FIRE_ON_PC":
                print(pos)

        except Exception as e:
            print(f"An error on_user_move: {e}")









    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)





keep_alive()
if __name__ == "__main__":
    room_id = "659cdef101602e72c92bbd5a"
    token = "04809b05cb717d3d4051c7cc7750032dd4a902e2956ad775e31ae6d4a7ee4464"
    arun(Bot().run(room_id, token))
