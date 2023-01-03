import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "$", selfbot = True)

token = 'токен'
appid = айди приложения
largeimageid = айди изображения


@bot.event
async def on_ready():
	await bot.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = appid,
			details = "самый верхний текст",
			name = "стримит на",
			assets = {
			  'large_image' : str(largeimageid),
			  'large_text':'ссылка при наводе на картинку'
			},
			url = "https://www.twitch.tv/404%27"
			)
		)
	print(f'Селфбот успешно запущен на аккаунте {bot.user}!')

bot.run(token, bot = False)
