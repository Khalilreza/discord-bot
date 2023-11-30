#Import discord class library to connect to Discord API
#Import the OS python module and random module
#Import the token file and ec2_metadate from AWS


import discord
import os
import random
from ec2_metadata import ec2_metadata

#Print ec2_metadate region and instance ID

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#Import load_dotenv file folder
#Creation of client object from discord subclass and defining token by retrieving the "TOKEN" string from OS with get.nav

client = discord.Bot()
token = str(os.getenv('TOKEN'))

#Formatting string into the argument parameter with brackets and creating an output to the terminal window
#Creation of output to the terminal window by formatting a string

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#Passing info into function. def_onmessage event taking details about message: username, channel, message 
#Converting an output of the terminal window to

@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
    
    #Output, format with brackets
    print(f'Message {user_message} by {username} on {channel}') 

    #Client user as a bot. If message is sent by bot then don't reply

    if message.author == client.user: 
        return
  
    #If statement that puts in the random discord channel while running another if statement
    #Second if statement is user message is hello then in the channel and string containing username and ec2 data

    if channel == "random": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f"Sooner! {username} Your EC2 Data: {ec2_metadata.region}") 
            return #<--Returning values passed into function
        
        #String option of EC2 Data message request and response to concentation stringpy -3 -m pip install -U py-cord --pre

        elif user_message.lower() == "EC2 Data": 
            await message.channel.send ("Your instance data is" + ec2_metadata.region)
            

#Running Client with defined token from Linux OS
client.run(token)