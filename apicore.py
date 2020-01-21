import requests
import json
from bs4 import BeautifulSoup


class WarfacePageUser:
    profile_config = 'profile'

    def __init__(self, username):
        self.username = username
        self.soup = self.get_soup()

    def get_soup(self):
        user_url = f'https://wfts.su/{self.profile_config}/{self.username}'
        page = requests.get(user_url).text
        soup = BeautifulSoup(page,'html.parser')
        return soup

    def get_value_by_name_field(self, name):
        tag = self.soup.find('span', text=name)
        return tag.next_sibling.text

    def get_skill_value_by_skill_name(self, skill_name):
        tag = self.soup.find('span', text=skill_name)
        if tag.previous_sibling != None:
            return tag.previous_sibling.text 
        return tag.next_sibling.text


class WarfaceUserProfile(WarfacePageUser):
    profile_config = 'profile'

    @property
    def server(self):
        return self.soup.find('td',{'class':'server'}).string

    @property
    def player_type(self):
        return self.soup.find('div',{'class':'player-type'}).string

    @property
    def rank(self):
        return self.get_value_by_name_field('Звание')

    @property
    def experience(self):
        return self.get_value_by_name_field('Получено очков опыта')

    @property
    def longest_match(self):
        return self.get_value_by_name_field('Самый продолжительный матч')

    @property
    def total_match_duration(self):
        return self.get_value_by_name_field('Общая продолжительность матчей')

    @property
    def game_time(self):
        return self.get_value_by_name_field('Проведено времени в игре')

    @property
    def clan(self):
        return self.get_value_by_name_field('Состоит в клане')

    @property
    def replenished_bp(self):
        return self.get_skill_value_by_skill_name('Пополнено БП')
    
    @property
    def restored_hp_value(self):
        return self.get_skill_value_by_skill_name('Восстановлено ОЗ')

    @property
    def count_of_reanimated_players(self):
        return self.get_skill_value_by_skill_name('Реанимировано игроков')

    @property
    def restored_ob_value(self):
        return self.get_skill_value_by_skill_name('Восстановлено ОБ')

class WarfaceUserPvp(WarfacePageUser):
    profile_config = 'pvp'

    @property
    def all_kills(self):
        return self.get_value_by_name_field('Убито противников')

    @property
    def all_shoots(self):
        return self.get_value_by_name_field('Произведено выстрелов')
    
    @property
    def hits_in_target(self):
        return self.get_value_by_name_field('Попаданий в цель')

    @property
    def kills_with_mine(self):
        return self.get_value_by_name_field('Убито минами')
    
    @property
    def kills_with_knife(self):
        return self.get_value_by_name_field('Убито в ближнем бою')

    @property
    def suicides_and_friendlyfire_kills(self):
        return self.get_value_by_name_field('Самоубийств и убитых союзников')

    @property
    def best_kill_combo(self):
        return self.get_value_by_name_field('Лучшая серия убийств')

    @property
    def deaths(self):
        return self.get_value_by_name_field('Смертей')

    @property
    def ratio_deaths_kills(self):
        return self.get_value_by_name_field('Соотношение убийств/смертей')
    
    @property
    def count_all_matches(self):
        return self.get_value_by_name_field('Сыграно матчей')

    @property
    def count_all_victories(self):
        return self.get_value_by_name_field('Количество побед')

    @property
    def count_all_draws(self):
        return self.get_value_by_name_field('Сыграно вничью')
    
    @property
    def winrate(self):
        return self.get_value_by_name_field('Процент побед')

    

wf_user = WarfaceUserPvp('Пираний')
print(wf_user.winrate)