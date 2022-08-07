import discord
from discord.ext import commands

import discord_components
from discord_components import Button, Select, SelectOption, ComponentsBot

oleg = ComponentsBot(">")

@oleg.event
async def on_ready():
    print('\nКакая-то лютая ху*ня родился, сучка\n', ('=' * 33))
    await oleg.change_presence(status = discord.Status.idle, activity = discord.Game('"монетка туда - сюда"')) #статус бота

@oleg.command()
async def button(self, ctx):
	   await ctx.send("Привет, здесь ты можешь выбрать роли, связанные с играми, в которые ты играешь. Ну.. пока я онлайн)", 
	    components= [[Button(label = "Дота", custom_id = "Dota"),
	    	Button(label = "Майнкрафт", custom_id = "MINECRAFT"),
	    	Button(label = "Тераррия", custom_id = "TERRARIA")
	    	]]
	    	)

@oleg.command()
async def butt(self, ctx):
    await ctx.send("Что бы начать деятельность на сервере, стань Микрочеликом (желательно ещё выбери игры, что бы иметь доступ к их чатам)", 
    	components = [[Button(label = "--------------------- Стать микрочеликом ---------------------", custom_id = "mic")
    		]]
    		)
	
@oleg.event()
async def on_button_click(self, interaction):

	dota = discord.utils.get( interaction.user.guild.roles, id = 668918782156341279)
	mine = discord.utils.get( interaction.user.guild.roles, id = 664165279693144064)
	terka = discord.utils.get( interaction.user.guild.roles, id = 722842360907825262)
	micro = discord.utils.get( interaction.user.guild.roles, id = 995297854358818877)

	match interaction.custom_id:
		case 'Dota':
			if dota in interaction.user.roles:
				await interaction.user.remove_roles(dota)

			else:
				await interaction.user.add_roles(dota)

		case 'MINECRAFT':
			if mine in interaction.user.roles:
				await interaction.user.remove_roles(mine)

			else:
				await interaction.user.add_roles(mine)

		case 'TERRARIA':
			if terka in interaction.user.roles:
				await interaction.user.remove_roles(terka)

			else:
				await interaction.user.add_roles(terka)
		case 'mic':
			if micro in interaction.user.roles:
				await interaction.user.remove_roles(micro)

			else:
				await interaction.user.add_roles(micro)
				
	try:  #СПЕЦИАЛЬНО ВЫЗЫВАЕТСЯ ИСКЛЮЧЕНИЕ, ПОТОМУ ЧТО МНЕ НЕ НУЖНО НИЧЕГО ОТВЕЧАТЬ ПОЛЬЗОВАТЕЛЮ, НО КАК НЕ ПИСАТЬ ЭТО Я НЕ НАШЁЛ
		await interaction.respond()
	except:
		pass	


oleg.run('TOKEN')