# This bot was created by Rogue#7720. Everything was typed by me :D.
                                                                                                               
                                                                                                               
# ,-.----.                                                   ,----..       ,----..       ,----..        ,----,   
# \    /  \                                                 /   /   \     /   /   \     /   /   \     .'   .' \  
# ;   :    \   ,---.                      ,--,             /   .     :   /   .     :   /   .     :  ,----,'    | 
# |   | .\ :  '   ,'\   ,----._,.       ,'_ /|            .   /   ;.  \ .   /   ;.  \ .   /   ;.  \ |    :  .  ; 
# .   : |: | /   /   | /   /  ' /  .--. |  | :    ,---.  .   ;   /  ` ;.   ;   /  ` ;.   ;   /  ` ; ;    |.'  /  
# |   |  \ :.   ; ,. :|   :     |,'_ /| :  . |   /     \ ;   |  ; \ ; |;   |  ; \ ; |;   |  ; \ ; | `----'/  ;   
# |   : .  /'   | |: :|   | .\  .|  ' | |  . .  /    /  ||   :  | ; | '|   :  | ; | '|   :  | ; | '   /  ;  /    
# ;   | |  \'   | .; :.   ; ';  ||  | ' |  | | .    ' / |.   |  ' ' ' :.   |  ' ' ' :.   |  ' ' ' :  ;  /  /-,   
# |   | ;\  \   :    |'   .   . |:  | : ;  ; | '   ;   /|'   ;  \; /  |'   ;  \; /  |'   ;  \; /  | /  /  /.`|   
# :   ' | \.'\   \  /  `---`-'| |'  :  `--'   \'   |  / | \   \  ',  /  \   \  ',  /  \   \  ',  /./__;      :   
# :   : :-'   `----'   .'__/\_: |:  ,      .-./|   :    |  ;   :    /    ;   :    /    ;   :    / |   :    .'    
# |   |.'              |   :    : `--`----'     \   \  /    \   \ .'      \   \ .'      \   \ .'  ;   | .'       
# `---'                 \   \  /                 `----'      `---`         `---`         `---`    `---'          
# b                       `--`-'                                                                                  
 #Yeet
 #All items taken MUST Be given credit, or I will press charges. Depending on what you do with it I might still press charges.
 #This was meant for RubyRealms.. Anyone using this without permission or edits without permission from me will be punished.
 
from discord.ext import commands
import discord
import requests
import os
import random
import datetime
import json
import time
import asyncio

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="some DQ!"))
	print("Hi.")
	await client.send_message(client.get_channel('561498821302157313'), "**---------------------------------**")
	await client.send_message(client.get_channel('561498821302157313'), "**                  Loaded.             **")
	
@client.event
async def on_member_join(member):
	roles = discord.utils.get(member.server.roles, name="Not Verified")
	await client.add_roles(member, roles)
	await client.send_message(member, "Welcome to Ruby Realms! Make sure to read the rules! The website link is https://www.rubyrealms.com if you didn't know!")
	await client.send_message(client.get_channel('526619228803956736'), member.name + " joined. ID: " + member.id)
	
@client.command(pass_context=True)
async def speak(ctx, channel, *, content:str):
	await client.send_message(client.get_channel(channel),content)

@client.command(pass_context=True)
async def giveaway(ctx, secondtime, *, content:str):
	embed=discord.Embed(title=content, description="React with 🎉 to enter!", color=0xbdf4fb)
	embed.add_field(name='Time Remaining: ' + str(datetime.timedelta(seconds=int(secondtime))), value="Who's hyped!?", inline=True)
	embed.set_footer(text="Made by Rogue#0002")
	msg = await client.send_message(client.get_channel('561435469699612673'), embed=embed)
	reactiontime = await client.add_reaction(msg, '🎉')
	await asyncio.sleep(10)
	x = int(secondtime)-10
	reacts = []
	msg = discord.utils.get(client.messages, id = msg.id)
	for reactor in msg.reactions:
   		reactors = await client.get_reaction_users(reactor)

	for i in reactors:
   		reacts.append(i.mention)
	await client.send_message(msg.channel, reacts)
	await client.send_message(msg.channel, "** The winner is @" + random.choice(reacts)) + ". congratulations!**"
		
@client.command(pass_context=True)
async def listeningpresence(ctx, *, content:str):
	await client.change_presence(game=discord.Game(name=content, type=2))
	await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with listening.")
	
@client.command(pass_context=True)
async def watchingpresence(ctx, *, content:str):
	await client.change_presence(game=discord.Game(name=content, type=3))
	await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with watching.")

client.run(os.environ['BOT_TOKEN'])
