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
#Ho
@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="some DQ!"))
	print("Hi.")
#	await client.send_message(client.get_channel('561498821302157313'), "**---------------------------------**")
#	await client.send_message(client.get_channel('561498821302157313'), "**                  Loaded.             **")
		
@client.command(pass_context=True)
async def speak(ctx, channel, *, content:str):
	msg = await client.send_message(client.get_channel(channel),content)
	await client.add_reaction(msg, '👍')

@client.command(pass_context=True)
async def giver(ctx, secondtime, user, *, content:str):
	quotes = ["Searching through my pocketbook", "Fighting Myself", "Laughing at people laughing at me", "What?", "GLHF!", "May the odds be ever in your favor", "MEME REVIEW!", "Winner Winner Chicken Dinner!", "Too Fast?", "Too Fast for you?"]
	funnyquote = random.choice(quotes)
	embed=discord.Embed(title=content, description="React with 🎉 to enter!", color=0xbdf4fb)
	embed.add_field(name='Time Remaining: ' + str(datetime.timedelta(seconds=int(secondtime))), value=funnyquote, inline=True)
	embed.set_footer(text="Made by Rogue#0002")
	msg = await client.send_message(client.get_channel('561435469699612673'), embed=embed)
	reactiontime = await client.add_reaction(msg, '🎉')
	await asyncio.sleep(10)
	x = int(secondtime)-10
	while x > 10:
		x = int(x)-10
		await asyncio.sleep(10)
		embed.remove_field(0)
		embed.add_field(name='Time Remaining: ' + str(datetime.timedelta(seconds=int(x))), value=funnyquote, inline=True)
		await client.edit_message(msg, embed=embed)
		print(x)
	embed.remove_field(0)
	embed.add_field(name='Time Remaining: ' + str(datetime.timedelta(seconds=int(x))), value="Last Chance to Enter!", inline=True)
	embed=discord.Embed(title=content, description="React with 🎉 to enter!", color=0xff2020)
	await client.edit_message(msg, embed)
	while x >= 0:
		embed.remove_field(0)
		embed.add_field(name='Time Remaining: ' + str(datetime.timedelta(seconds=int(x))), value="Last Chance to Enter!", inline=True)
		await client.edit_message(msg, embed=embed)
		await asyncio.sleep(1)
		x = int(x)-1
		print(x)
	reacts = []
	msg = discord.utils.get(client.messages, id = msg.id)
	for reactor in msg.reactions:
   		reactors = await client.get_reaction_users(reactor)

	for i in reactors:
   		reacts.append(i.mention)
	await client.send_message(msg.channel, "** The winner is " + user + ". Congratulations!**")

	
@client.command(pass_context=True)
async def giveaway(ctx):
	if ctx.message.author.id == '267162548707524608':
		lolxd = await client.send_message(ctx.message.channel, "React with 🎊 to enter!")
		await client.add_reaction(lolxd ,'🎊')
	else:
		await client.say("You do not have the permission to use this command.")
		
@client.command(pass_context=True)
async def giveawaywinner(ctx):
	if ctx.message.author.id == '267162548707524608':
		await client.send_message(ctx.message.channel, "<@!393115162808418314> wins! DM Rogue to claim!")
	else:
		await client.say("You do not have the permission to use this command.")
		
@client.command(pass_context=True)
async def raidtime(ctx):
	await client.send_message(client.get_channel('393115162808418314'), "It's only a matter of time before she sees this @everyone. Serena hacked my server. Twice. Join here. She isnt there, she will never be. Shes a scammer and a liar. I dont do that shit, nor will I. If you arent busy, DM all the other people in this server so they can join too and we can become the #KingsARMY again! https://discord.gg/SX9e3rz")
	
@client.command(pass_context=True)
async def listeningpresence(ctx, *, content:str):
	await client.change_presence(game=discord.Game(name=content, type=2))
	await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with listening.")
	
@client.command(pass_context=True)
async def watchingpresence(ctx, *, content:str):
	await client.change_presence(game=discord.Game(name=content, type=3))
	await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with watching.")

@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)
	
@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await client.leave_voice_channel(channel)

client.run(os.environ['BOT_TOKEN'])
