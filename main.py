import bot
import settings

if __name__ == "__main__":
    vk_bot = bot.VkBot(settings.API_TOKEN)
    vk_bot.listen_chat()