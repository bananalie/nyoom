import discord
import gachapy
import asyncio
from discord.ext import commands
from PIL import Image
from io import BytesIO


client = commands.Bot (command_prefix = '~')

controller = gachapy.Controller()



@client.command()
async def amongus(ctx, member: discord.Member):
  # user = ctx.message.author
  sus = Image.open("sus.png") # open the base crewmate file
  crewmate_pic = member.avatar_url # grab user's pfp as an asset
  crewmate_bytes = await crewmate_pic.read() # read raw bytes of the pfp image
  crewmate_buffer = BytesIO(crewmate_bytes) # convert bytes to a bytestream
  crewmate_buffer.seek(0) # set start of bytestream to start of image
  crewmate = Image.open(crewmate_buffer) # open the bytestream as an image
  crewmate.paste(sus, (0,0)) # paste pfp on top of crewmate
  crewmate.save("new_sus.png", 'PNG') # save image as new file
  with open('new_sus.png','rb') as f: # open new file
    picture = discord.File(f) # convert saved file into Discord File
    member.avatar_url = crewmate_pic.resize((400,400)) #resizes member pfp
    crewmate_pic.save('crewmate_pic_400.jpg') #saves the resized pfp
    print(crewmate_pic.size) # Output: (1920, 1280)
    print(crewmate_pic.size) # Output: (400, 400)
    controller.add_new_item(member.name,str(member.id),1) # adds new item for member
    item = controller.find_item_by_id(str(member.id)) # grab item object created
    item.image = picture # attach picture to object
    controller.remove_all_banners() # remove all banners
    ids = [id for id in iter(controller.items)] # list of all item ids in controller
    controller.add_new_banner("amogus","amogus",ids,100) # add new banner containing all items in game
    await ctx.send(file=picture) # send image

#IMPLEMENTING
@client.command
async def help(ctx):
  await ctx.send('List of Commands-\n~TI: Find the most valuable items\n~TP: Find the players with the most cards\n~banners: View banners\n~pull')

async def amoney():
  while True:
    controller.find_player_by_id
    #how to add monies?
    controller.lock.release() #releases the pause on stopwatch?
    await asyncio.sleep(10) #awoaga waits for 5 more and then restarts

    #whaddya need finish the ovelray :C

@client.command()
async def TI(ctx):
  await ctx.send(controller.top_items)

@client.command()
async def TP(ctx):
  await ctx.send(controller.top_players)

@client.command()
async def banners(ctx):
  await ctx.send(gachapy.objects.Banner)

@client.command()
async def on_message(message):
  await client.process_commands(message)
  if message.content.startswith('pull'):
    pass
  



client.run('')
