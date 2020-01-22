import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import settings
from apicore import WarfaceUserProfile, WarfaceUserMainPve, WarfaceUserMainPvp
from views import *

class VkBot:

    def __init__(self, api_token):
        self.session = vk_api.VkApi(token=api_token)
        self.long_poll = VkLongPoll(self.session)
        self.vk = self.session.get_api()
 

    def listen_chat(self):
        for event in self.long_poll.listen():
            if self.event_is_valid(event):
                try:
                    response = self.message_handler(event.text)
                    self.send_response(response, event.user_id)
                except Exception:
                    pass

    def message_handler(self, message_text):
        if message_text == 'help':
            view = ViewAllCommands()
            return view.get_view()
        if len(message_text.split()) == 2:
            username, profile = message_text.split()
            if profile == 'pvp':
                return self.get_wf_user_pvp_profile(username)
            elif profile == 'pve':
                return self.get_wf_user_pve_profile(username)
        return self.get_wf_user_profile(message_text)

    def get_wf_user_profile(self, username):
        wf_user = WarfaceUserProfile(username)
        return self.get_wf_user_profile_view(wf_user)
    
    def get_wf_user_pvp_profile(self, username):
        wf_pvp_user = WarfaceUserMainPvp(username)
        return self.get_wf_user_pvp_view(wf_pvp_user)
    
    def get_wf_user_pve_profile(self, username):
        wf_pve_user = WarfaceUserMainPve (username)
        return self.get_wf_user_pve_view(wf_pve_user)

    def get_wf_user_pve_view(self, wf_user):
        view_profile = ViewPveProfile(wf_user)
        return view_profile.get_view_profile()

    def get_wf_user_profile_view(self, wf_user):
        view_profile = ViewProfile(wf_user)
        return view_profile.get_view_profile()

    def get_wf_user_pvp_view(self, wf_user):
        view_profile = ViewPvpProfile(wf_user)
        return view_profile.get_view_profile()

    def send_response(self, msg, user_id):
        self.vk.messages.send(
            user_id=user_id,
            message=msg,
            random_id=random.randint(1, 10 ** 10)
        )

    def event_is_valid(self, event):
        return event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.from_user




