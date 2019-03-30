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
async def giveaway(ctx, *, content:str):
	embed=discord.Embed(title="TITLE", description="React with 🎉 to enter!", color=0xbdf4fb)
	embed.add_field(name='Time Remaining: 10 hours', value="Who's hyped!?", inline=True)
	embed.set_footer(text="Ends at • Today at 3:04 PM")
	await client.send_message(client.get_channel('561435469699612673'), embed=embed)
		
@client.command(pass_context=True)
async def listeningpresence(ctx, *, content:str):
	await client.change_presence(game=discord.Game(name=content, type=2))
	await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with listening.")
	
@client.command(pass_context=True)
async def watchingpresence(ctx, *, content:str):
	await client.change_presence(game=discord.Game(name=content, type=3))
	await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with watching.")

client.run(os.environ['BOT_TOKEN'])
