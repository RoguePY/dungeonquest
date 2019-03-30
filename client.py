# This bot was created by Rogue#7720. Everything was typed by me :D.
 #                _,.---._         _,---.                  ,----.       ,--,  ,--,  ,-----,--,,-----,--,,-----,--,     _.---.,_     
 #  .-.,.---.   ,-.' , -  `.   _.='.'-,  \ .--.-. .-.-. ,-.--` , \  __ /-\==\/-\==\_| '-  -\==\ '-  -\==\ '-  -\==\  .'  - , `.-,   
 # /==/  `   \ /==/_,  ,  - \ /==.'-     //==/ -|/=/  ||==|-  _.-`/\_  \'/==/ '/==/_\,--, '/==|,--, '/==|,--, '/==/ / -  ,  ,_\==\  
 #|==|-, .=., |==|   .=.     /==/ -   .-' |==| ,||=| -||==|   `.-.\/================/  /  /==/   /  /==/   /  /==/ |     .=.   |==| 
 #|==|   '='  /==|_ : ;=:  - |==|_   /_,-.|==|- | =/  /==/_ ,    /\__ \/==/  /==/_\/  / -/==/   / -/==/   / -/==/  | -  :=; : _|==| 
 #|==|- ,   .'|==| , '='     |==|  , \_.' )==|,  \/ - |==|    .-'\/===============/  / `/==/   / `/==/   / -/==/   |     `=` , |==| 
 #|==|_  . ,'. \==\ -    ,_ /\==\-  ,    (|==|-   ,   /==|_  ,`-._/ `/==/ `/==/     / -/==/   / -/==/   / `\==\_,--,\ _,    - /==/  
 #/==/  /\ ,  ) '.='. -   .'  /==/ _  ,  //==/ , _  .'/==/ ,     /`--`-`  -`-`     / `/==/   / `/==/   /` -   ,/==/  `.   - .`=.`   
 #`--`-`--`--'    `--`--''    `--`------' `--`..---'  `--`-----``                  `--`-`    `--`-`    `------`--`     ``--'--'    
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

client = commands.Bot(command_prefix = "ruby.")
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="at https://www.rubyrealms.com!"))
	print("Hi.")
	await client.send_message(client.get_channel('526619228803956736'), "**---------------------------------**")
	await client.send_message(client.get_channel('526619228803956736'), "**                  Loaded.             **")
	
@client.event
async def on_member_join(member):
	roles = discord.utils.get(member.server.roles, name="Not Verified")
	await client.add_roles(member, roles)
	await client.send_message(member, "Welcome to Ruby Realms! Make sure to read the rules! The website link is https://www.rubyrealms.com if you didn't know!")
	await client.send_message(client.get_channel('526619228803956736'), member.name + " joined. ID: " + member.id)
	
@client.command(pass_context=True)
async def speak(ctx, channel, *, content:str):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		await client.send_message(client.get_channel(channel),content)
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'speak' command. Check this out immediately.")
		
@client.command(pass_context=True)
async def listeningpresence(ctx, *, content:str):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		await client.change_presence(game=discord.Game(name=content, type=2))
		await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with listening.")
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'listeningpresence' command. Check this out immediately.")
	
@client.command(pass_context=True)
async def watchingpresence(ctx, *, content:str):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		await client.change_presence(game=discord.Game(name=content, type=3))
		await client.send_message(client.get_channel('526619228803956736'), "Presence changed to " + content + " with watching.")
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'watchingpresence' command. Check this out immediately.")

@client.command(pass_context=True)
async def upgrade(ctx):
	await client.send_message(ctx.message.author, 'I see you want to upgrade! Head on over to https://www.rubyrealms.com/upgrade to get started!')
		
@client.command(pass_context=True)
async def bugreport(ctx, *, content:str):
	await client.delete_message(ctx.message)
	embed = discord.Embed(title="Thank you for filing a bug report!", colour=discord.Colour(0x7f0532), description="This bug report has been sent to our staff team over the *airwaves*.", timestamp=datetime.datetime.utcfromtimestamp(time.time()))

	embed.set_image(url="https://cdn.discordapp.com/attachments/530310841279578132/530310894962475018/RedGrayGradientLogo.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_author(name=ctx.message.author.name, icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_footer(text="Bug Report!", icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")

	embed.add_field(name="Your message:", value=content)
	endmsg = await client.send_message(ctx.message.author, embed=embed)
	
	embed = discord.Embed(title="Bug report sent by " + ctx.message.author.name + "!", colour=discord.Colour(0x7f0532), description="Ready for review.", timestamp=datetime.datetime.utcfromtimestamp(time.time()))

	embed.set_author(name=ctx.message.author.name, icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_footer(text="Bug Report!", icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.add_field(name="User information:", value="Name: " + ctx.message.author.name + " | ID: " + ctx.message.author.id + ".")
	embed.add_field(name="**The user's message:**", value=content)
	msg = await client.send_message(client.get_channel('526619228803956736'), embed=embed)
	await client.add_reaction(msg, "👍")
	await client.add_reaction(msg, "👎")
	await asyncio.sleep(1)
	res = await client.wait_for_reaction(['👍', '👎'], message=msg)
	em = embed.add_field(name='New Reaction!', value='{0.user} has reacted with {0.reaction.emoji}.'.format(res))
	await client.edit_message(msg, embed=em)
	res = await client.wait_for_reaction(['👍', '👎'], message=msg)
	em = embed.add_field(name='New Reaction!', value='{0.user} has reacted with {0.reaction.emoji}.'.format(res))
	await client.edit_message(msg, embed=em)
	res = await client.wait_for_reaction(['👍', '👎'], message=msg)
	em = embed.add_field(name='New Reaction!', value='{0.user} has reacted with {0.reaction.emoji}.'.format(res))
	await client.edit_message(msg, embed=em)

@client.command(pass_context=True)
async def report(ctx, *, content:str):
	if '559459137445167144' in [role.id for role in ctx.message.author.roles]:
		await client.add_reaction(ctx.message, "👍")
		msg = await client.send_message(client.get_channel('560587749434851348'), "https://cdn.discordapp.com/attachments/526620228998660099/560332657158782976/PLlTbj.gif")
		msg = await client.send_message(client.get_channel('560587749434851348'), "**New Bug Report by **" + ctx.message.author.display_name + ":")
		msg = await client.send_message(client.get_channel('560587749434851348'), content)
		await client.add_reaction(msg, "👍")
		await client.add_reaction(msg, "👎")
		await asyncio.sleep(1)
	
@client.command(pass_context=True)
async def gshout(ctx, *, content:str):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		msg = await client.send_message(client.get_channel('560301120195657728'), "https://cdn.discordapp.com/attachments/526620228998660099/560332657158782976/PLlTbj.gif")
		msg = await client.send_message(client.get_channel('560301120195657728'), "**New Group Shout Request!**")
		msg = await client.send_message(client.get_channel('560301120195657728'), content)
		await client.add_reaction(msg, "👍")
		await client.add_reaction(msg, "👎")
		await asyncio.sleep(1)
		res = await client.wait_for_reaction(['👍', '👎'], message=msg)
		if res.reaction.emoji ==  '👍':
			await client.send_message(client.get_channel('560301154970632192'), content)
			await client.send_message(ctx.message.author, "Hello ! Your group shoutout request in RubyRealms was accepted! Check for yourself!")
			await client.send_message(ctx.message.author, "Have Fun, and Stay Hyped!")
			await client.send_message(ctx.message.author, "- Ruby Realms.")
		elif res.reaction.emoji ==  '👎':
			await client.send_message(client.get_channel('560301120195657728'), "Group Shoutout from " + ctx.message.author.name + ":")
			await client.send_message(client.get_channel('560301120195657728'), content)
			await client.send_message(client.get_channel('560301120195657728'), "https://ak7.picdn.net/shutterstock/videos/6803257/thumb/5.jpg")
			await client.send_message(client.get_channel('560301120195657728'), )
			await client.send_message(ctx.message.author, "Hello! We are sad to say that your group shout in Ruby Realms discord was denied. Here are some problems you might have had:")
			await client.send_message(ctx.message.author, "**-> Does your shout contain NSFW?**")
			await client.send_message(ctx.message.author, "**-> Was your group not Ruby Realms related?**")
			await client.send_message(ctx.message.author, "**-> Was your group against Ruby Realm's Terms of Service?**")
			await client.send_message(ctx.message.author, "Whatever the problem was, don't be discouraged! Change up the message, and try again! Make sure your promotion is safe for everyone!")
			await client.send_message(ctx.message.author, "Have Fun, and Stay Hyped!")
			await client.send_message(ctx.message.author, "- Ruby Realms.")
			await client.delete_message(msg)
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'gshout' command. Check this out immediately.")
	
@client.command(pass_context=True)
async def suggestion(ctx, *, content:str):
	await client.delete_message(ctx.message)
	embed = discord.Embed(title="Thank you for helping Ruby Realms!", colour=discord.Colour(0xc7ff), description="This suggestion has been sent to our staff team!", timestamp=datetime.datetime.utcfromtimestamp(time.time()))

	embed.set_image(url="https://cdn.discordapp.com/attachments/526456982161588234/530648794887618569/Recieved.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_author(name=ctx.message.author.name, icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_footer(text="Suggestion Sent!", icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")

	embed.add_field(name="Your message:", value=content)
	endmsg = await client.send_message(ctx.message.author, embed=embed)
	
	embed = discord.Embed(title="Suggestion sent by " + ctx.message.author.name + "!", colour=discord.Colour(0xc7ff), description="Ready for review.", timestamp=datetime.datetime.utcfromtimestamp(time.time()))

	embed.set_author(name=ctx.message.author.name, icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_footer(text="Suggestion recieved!!", icon_url="https://cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.add_field(name="User information:", value="Name: " + ctx.message.author.name + " | ID: " + ctx.message.author.id + ".")
	embed.add_field(name="**The User's Suggestion:**", value=content)
	msg = await client.send_message(client.get_channel('526619228803956736'), embed=embed)
	await client.add_reaction(msg, "👍")
	await client.add_reaction(msg, "👎")
	await asyncio.sleep(1)
	res = await client.wait_for_reaction(['👍', '👎'], message=msg)
	em = embed.add_field(name='New Reaction!', value='{0.user} has reacted with {0.reaction.emoji}.'.format(res))
	await client.edit_message(msg, embed=em)
	res = await client.wait_for_reaction(['👍', '👎'], message=msg)
	em = embed.add_field(name='New Reaction!', value='{0.user} has reacted with {0.reaction.emoji}.'.format(res))
	await client.edit_message(msg, embed=em)
	res = await client.wait_for_reaction(['👍', '👎'], message=msg)
	em = embed.add_field(name='New Reaction!', value='{0.user} has reacted with {0.reaction.emoji}.'.format(res))
	await client.edit_message(msg, embed=em)
		
@client.command(pass_context=True)
async def autoupdate(ctx):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		api='https://rubyrealms.com/api/discord/check-data/'
		code = "H39VW4z4EgPjPStz48CyxR"
		url = api+code
		r = requests.get(url)
		lol = json.loads(r.content)
		numlol = len(lol)
		for x in range(0, numlol):
			currentuser = x
			try:
				await client.send_message(client.get_channel('530218589731684373'), '**------------------------**')
				await client.send_message(client.get_channel('530218589731684373'),"**" + lol[currentuser]['CurrentUsername'] + " is testing for autoupdate.**")
				membership = lol[currentuser]['CurrentMembership']
				user = ctx.message.server.get_member_named(lol[currentuser]['CurrentUsername'] + ' 󠀀󠀀')
				role = discord.utils.get(ctx.message.server.roles, name="Visionary")
				rolez = discord.utils.get(ctx.message.server.roles, name="Builder")
				roles = discord.utils.get(ctx.message.server.roles, name="Prime Mover")
				if '526468008852455444' in [role.id for role in user.roles]:
					if membership == '1':
						if '530225776323330068' in [role.id for role in user.roles]: #Prime Mover
							await client.remove_roles(user, roles)
						if '524151823909781515' in [role.id for role in user.roles]: #Builder
							await client.remove_roles(user, rolez)
						if '524151873922662410' in [role.id for role in user.roles]: #Visionary
							await client.remove_roles(user, role)
						await client.add_roles(user, rolez)
					if membership == '2':
						if '530225776323330068' in [role.id for role in user.roles]: #Prime Mover
							await client.remove_roles(user, roles)
						if '524151823909781515' in [role.id for role in user.roles]: #Builder
							await client.remove_roles(user, rolez)
						if '524151873922662410' in [role.id for role in user.roles]: #Visionary
							await client.remove_roles(user, role)
						await client.add_roles(user, role)
					if membership == '3':
						if '530225776323330068' in [role.id for role in user.roles]: #Prime Mover
							await client.remove_roles(user, roles)
						if '524151823909781515' in [role.id for role in user.roles]: #Builder
							await client.remove_roles(user, rolez)
						if '524151873922662410' in [role.id for role in user.roles]: #Visionary
							await client.remove_roles(user, role)
						await client.add_roles(user, roles)
					if membership == '0':
						if '530225776323330068' in [role.id for role in user.roles]: #Prime Mover
							await client.remove_roles(user, roles)
						if '524151823909781515' in [role.id for role in user.roles]: #Builder
							await client.remove_roles(user, rolez)
						if '524151873922662410' in [role.id for role in user.roles]: #Visionary
							await client.remove_roles(user, role)
			except:
				await client.send_message(client.get_channel("530218589731684373"), "** " + lol[currentuser]['CurrentUsername'] + " Not Found.**")
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'autoupdate' command. Check this out immediately.")
	
@client.command(pass_context = True)
async def verify(ctx, code):
	if ctx.message.channel.id == '541809056856145921':
		if '526647078370410497' in [role.id for role in ctx.message.author.roles]:
			api='https://rubyrealms.com/api/discord/load-data/'
		
			url = api+code
			r = requests.get(url)
			try:
				lol = json.loads(r.content)
				await client.send_message(client.get_channel('526619169891024922'), '------------------------')
				await client.send_message(client.get_channel('526619169891024922'),"**" + lol[0]['Username'] + " is Verifying.**")
				await client.change_nickname(ctx.message.author, lol[0]['Username'] + " 󠀀󠀀")
				membership = lol[0]['Membership']
				addmyrole = discord.utils.get(ctx.message.server.roles, name="Verified")
				removemyrole = discord.utils.get(ctx.message.server.roles, name="Not Verified")
				if '526647078370410497' in [role.id for role in ctx.message.author.roles]:
					if '526468008852455444' in [role.id for role in ctx.message.author.roles]:
						await client.send_message(client.get_channel('526619169891024922'), "Somehow " + lol[0]['Username'] + " had the Verified Role....Weird lol.")
					else:
						await client.add_roles(ctx.message.author, addmyrole)
					await client.remove_roles(ctx.message.author, removemyrole)
				else:
					print("hai")
				role = discord.utils.get(ctx.message.server.roles, name="Visionary")
				rolez = discord.utils.get(ctx.message.server.roles, name="Builder")
				roles = discord.utils.get(ctx.message.server.roles, name="Prime Mover")
				if membership == '1':
					if '530225776323330068' in [role.id for role in ctx.message.author.roles]: #Prime Mover
						await client.remove_roles(ctx.message.author, roles)
					if '524151873922662410' in [role.id for role in ctx.message.author.roles]: #Visionary
						await client.remove_roles(ctx.message.author, role)
					await client.add_roles(ctx.message.author, rolez)
					await client.send_message(ctx.message.author, "Thanks for verifying, " + lol[0]['Username'] + "! Your membership is currently **Builder**. *Want to upgrade*? Go to https://rubyrealms.com/upgrade")
					await client.delete_message(ctx.message)
				if membership == '2':
					if '530225776323330068' in [role.id for role in ctx.message.author.roles]: #Prime Mover
						await client.remove_roles(ctx.message.author, roles)
					if '524151823909781515' in [role.id for role in ctx.message.author.roles]: #Builder
						await client.remove_roles(ctx.message.author, rolez)
					await client.add_roles(ctx.message.author, role)
					await client.send_message(ctx.message.author, "Thanks for verifying, " + lol[0]['Username'] + "! Your membership is currently **Visionary**. *Want to upgrade*? Go to https://rubyrealms.com/upgrade")
					await client.delete_message(ctx.message)
				if membership == '3':
					if '524151823909781515' in [role.id for role in ctx.message.author.roles]: #Builder
						await client.remove_roles(ctx.message.author, rolez)
					if '524151873922662410' in [role.id for role in ctx.message.author.roles]: #Visionary
						await client.remove_roles(ctx.message.author, role)
					await client.add_roles(ctx.message.author, roles)
					await client.send_message(ctx.message.author, "Thanks for verifying, " + lol[0]['Username'] + "! Your membership is currently **Prime Mover**. See ya around.")
					await client.delete_message(ctx.message)
				if membership == '0':
					if '530225776323330068' in [role.id for role in ctx.message.author.roles]: #Prime Mover
						await client.remove_roles(ctx.message.author, roles)
					if '524151823909781515' in [role.id for role in ctx.message.author.roles]: #Builder
						await client.remove_roles(ctx.message.author, rolez)
					if '524151873922662410' in [role.id for role in ctx.message.author.roles]: #Visionary
						await client.remove_roles(ctx.message.author, role)
					messagez = await client.send_message(ctx.message.author, "Congrats for verifying, " + lol[0]['Username'] + "! Your membership is currently- Wait a second, you don't have one! *Want to upgrade?* Go to https://rubyrealms.com/upgrade")
					await client.delete_message(ctx.message)
			except:
				messagez = await client.send_message(ctx.message.channel, "**Invalid Code! Try again.**")
				await asyncio.sleep(3)
				await client.delete_message(messagez)
				await client.delete_message(ctx.message)

		else:
			messagez = await client.say("You are already verified. If you believe this is an error, contact a user with the 'Team Member' role.")
			await asyncio.sleep(3)
			await client.delete_message(messagez)
			await client.delete_message(ctx.message)
	
@client.command(pass_context=True)
async def trade(ctx):
	if '526468008852455444' in [role.id for role in ctx.user.roles]:
		channel = client.get_channel('484715821227048981')
		if ctx.message.channel == channel:
			if "530168328187019282" in [role.id for role in ctx.message.author.roles]:
				user = ctx.message.author
				role = discord.utils.get(user.server.roles, name='Trading')
				await client.remove_roles(user, role)
				await client.say("Your trading role has been removed.")
			else:
				user = ctx.message.author
				role = discord.utils.get(user.server.roles, name='Trading')
				await client.add_roles(user, role)
				await client.say("Success! Check your roles!")

@client.command(pass_context=True)
async def help(ctx):
	avatar = (ctx.message.author.avatar_url)
	embed = discord.Embed(title="**Ruby Realms Discord Help Section**", colour=discord.Colour(0xb3cd1e), description="**Notice: All Commands ARE Case-Sensitive!**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))

	embed.set_image(url="https://images-ext-1.discordapp.net/external/W-lbtzpJqUmGN5p4pLPUFzGmnoZP3ySkXkWLjwBC3N4/https/cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")
	embed.set_thumbnail(url=avatar)
	embed.set_author(name=ctx.message.author.name, icon_url=avatar)
	embed.set_footer(text="footer text", icon_url="https://images-ext-1.discordapp.net/external/W-lbtzpJqUmGN5p4pLPUFzGmnoZP3ySkXkWLjwBC3N4/https/cdn.discordapp.com/attachments/530310841279578132/530314023330119681/RedGrayGradientLogo.png")

	embed.add_field(name="**ruby.help**", value="Displays Helpful Commands")
	embed.add_field(name="**ruby.verify [code]**", value="Verifies your Discord account to Ruby Realms! Can only be used once. [code] is your Ruby Realms code, which you can find in your Ruby Realms settings.", inline=True)
	embed.add_field(name="**ruby.upgrade**", value="Gives you a link to the membership page.", inline=True)
	embed.add_field(name="**ruby.english**", value="Gives you the 'English' role so you can speak in English only channels!", inline=True)
	embed.add_field(name="**ruby.espanol or ruby.español**", value="Gives you the 'español' role so you can speak in Spanish/Español only channels!", inline=True)

	await client.send_message(ctx.message.author, embed=embed)		
		
@client.command(pass_context=True)
async def lottonum(ctx):
	omeganum = random.randint(1, 100)
	rannum = random.randint(1, 100)
	avatar = (ctx.message.author.avatar_url)
	embed = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Choosing Number.**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	embed.set_thumbnail(url=avatar)
	embed.set_author(name=ctx.message.author.name, icon_url=avatar)
	msg = await client.send_message(ctx.message.channel, embed=embed)
	await asyncio.sleep(.3)
	# Part One
	em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Choosing Number..**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(.3)
	# Part Two
	em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Choosing Number...**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(.3)
	# Part Three
	em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Choosing Number.**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(.3)
	# Part Four
	em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Choosing Number..**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(.3)
	# Part Five
	em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Choosing Number...**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(.3)
	em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="**Your number is " + str(omeganum) + ". Good Luck!**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(3)
	# ACTUALLY STARTING! PART SIX
	funnyquotes = ['Searching Mainstream Media....', 'Checking Pewdiepie Videos...', 'Checking my Minecraft Inventory...', 'Fighting Myself']
	em = embed.add_field(name="Checking if you are a lucky winner...",value=random.choice(funnyquotes))
	await client.edit_message(msg, embed=em)
	await asyncio.sleep(3)
	if omeganum == rannum:
		em = embed.clear_fields()
		await client.edit_message(msg, embed=em)
		em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="Status = **ENDED**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
		randomzz = ['Obtain the Grain!', 'Hmm...You think you got what it takes to win again?', 'Victory Royale!', '#Flex']
		em = embed.add_field(name="**You WIN!**",value=random.choice(randomzz))
		await client.edit_message(msg, embed=em)
	else:
		em = embed.clear_fields()
		await client.edit_message(msg, embed=em)
		em = discord.Embed(title="**Let's Pick a number!**", colour=discord.Colour(0xb3cd1e), description="Status = **ENDED**", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
		em = embed.add_field(name="**You lost! Sorry! Try again**!", value="Your number was **" + str(omeganum) + "**, and the winning number was **" + str(rannum) + "**.")
		await client.edit_message(msg, embed=em)
	
@client.command(pass_context=True)
async def english(ctx):
		channel = client.get_channel('530134123126325268')
		if ctx.message.channel == channel:
			if '530633136099426318' in [role.id for role in ctx.message.author.roles]:
				user = ctx.message.author
				role = discord.utils.get(user.server.roles, name='English')
				await client.remove_roles(user, role)
				await client.say("Your role has been removed!")
			else:
				user = ctx.message.author
				role = discord.utils.get(user.server.roles, name='English')
				await client.add_roles(user, role)
				await client.say("Your role has been added!")
				
@client.command(pass_context=True)
async def español(ctx):		
	channel = client.get_channel('530134123126325268')
	if ctx.message.channel == channel:	
		if '530633109818048512' in [role.id for role in ctx.message.author.roles]:
			user = ctx.message.author
			role = discord.utils.get(user.server.roles, name='Español')
			await client.remove_roles(user, role)
			await client.say("Rol removido!")
		else:
			user = ctx.message.author
			role = discord.utils.get(user.server.roles, name='Español')
			await client.add_roles(user, role)
			await client.say("EXITO! Checa tus roles!")
			
@client.command(pass_context=True)
async def espanol(ctx):		
	channel = client.get_channel('530134123126325268')
	if ctx.message.channel == channel:	
		if '530633109818048512' in [role.id for role in ctx.message.author.roles]:
			user = ctx.message.author
			role = discord.utils.get(user.server.roles, name='Español')
			await client.remove_roles(user, role)
			await client.say("Rol removido!")
		else:
			user = ctx.message.author
			role = discord.utils.get(user.server.roles, name='Español')
			await client.add_roles(user, role)
			await client.say("EXITO! Checa tus roles!")
				
				
@client.command(pass_context=True)
async def dothewave(ctx):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		await client.send_message(client.get_channel('462094440920645634'),"👋")
		await client.send_message(client.get_channel('526619228803956736'), "I waved in **#general-chat.**")
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'dothewave' command. Check this out immediately.")
		
@client.command(pass_context=True)
async def dothehi(ctx):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		await client.send_message(client.get_channel('462094440920645634'),"Hello. Checking in on my favorite community. C:")
		await client.send_message(client.get_channel('526619228803956736'), "I said Hi in **#general-chat**.")
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'dothehi' command. Check this out immediately.")
	
@client.command(pass_context=True)
async def dothecry(ctx):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		await client.send_message(client.get_channel('462094440920645634'),"😭")
		await client.send_message(client.get_channel('526619228803956736'), "I cried in **#general-chat.**")
	else:
		await client.send_message(client.get_channel("526619228803956736"), "A user by the name of " + ctx.message.author.name + ", also with the ID of '" + ctx.message.author.id + "' has attempted to use the 'dothecry' command. Check this out immediately.")
		
@client.command(pass_context=True)
async def lucky(ctx, num: int):
	number = random.randint(1, 1000)
	print(number)
	if num == number:
		await client.send_message(ctx.message.channel, "That was the right number! Good Job!")
	else:
		await client.send_message(ctx.message.channel, "Wrong Number. Oops! The number was " + str(number) + ".")
		
@client.command(pass_context=True)
async def perms(ctx, num: int, * ,role: str):
	if '527363576101339136' in [role.id for role in ctx.message.author.roles]:
		role = discord.utils.get(ctx.message.server.roles, name=role)
		await client.edit_role(ctx.message.server, role, permissions=discord.Permissions(num))
		await client.send_message(ctx.message.author, "Hi.")
	else:
		await client.say("Invalid Permissions....How do you know this command?")
		
		
client.run(os.environ['BOT_TOKEN'])
