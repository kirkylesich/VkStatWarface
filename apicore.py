import requests
import json
import re
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

class WarfaceUserInfoForClass:
    class_name = 'Штурмовик'

    def __init__(self, soup):
        self.soup = soup
    
    def get_all_blocks_of_class(self):
        return self.soup.find_all('div', class_='statistics-block')
    
    def get_current_class_spans(self):
        class_block = self.soup.find('div', text=re.compile(f'^{self.class_name}'))
        return class_block.find_all_next('span')[:12]

    def get_value_by_name_field(self, field_name):
        class_fields = self.get_current_class_spans()
        for value in class_fields:
            if value.text == field_name:
                return class_fields[class_fields.index(value)+1].text

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

class WarfaceUserMainInfo(WarfacePageUser):

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

    @property
    def count_kicks_from_match(self):
        return self.get_value_by_name_field('Исключений из боя')

    @property
    def count_interrupted_mathces(self):
        return self.get_value_by_name_field('Прервано матчей')
    
    @property
    def game_time(self):
        return self.get_value_by_name_field('Время в игре')
    
    @property
    def engineer(self):
        engineer = WarfaceEngineerClass(self.soup)
        return engineer
    
    @property
    def medic(self):
        medic = WarfaceMedicClass(self.soup)
        return medic
    
    @property
    def rifleman(self):
        rifleman = WarfaceRiflemanClass(self.soup)
        return rifleman

    @property
    def sniper(self):
        sniper = WarfaceSniperClass(self.soup)
        return sniper
    
    @property
    def sad(self):
        sad = WarfaceSadClass(self.soup)
        return sad

class WarfaceUserClassInterface(WarfaceUserInfoForClass):
    class_name = 'Штурмовик'

    @property
    def all_shoots(self):
        return self.get_value_by_name_field('Произведено выстрелов')
    
    @property
    def hits_in_target(self):
        return self.get_value_by_name_field('Попаданий в цель')
    
    @property
    def hit_accuracy(self):
        return self.get_value_by_name_field('Меткость')
    
    @property
    def hits_in_head(self):
        return self.get_value_by_name_field('Попаданий в голову')
    
    @property
    def hits_in_head_with_knife(self):
        return self.get_value_by_name_field('Попаданий в голову в ближ. бою')
    
    @property
    def game_time(self):
        return self.get_value_by_name_field('В игре')

class WarfaceRiflemanClass(WarfaceUserClassInterface):
    class_name = 'Штурмовик'

class WarfaceMedicClass(WarfaceUserClassInterface):
    class_name = 'Медик'

class WarfaceSadClass(WarfaceUserClassInterface):
    class_name = 'СЭД'

class WarfaceEngineerClass(WarfaceUserClassInterface):
    class_name = 'Инженер'

class WarfaceSniperClass(WarfaceUserClassInterface):
    class_name = 'Снайпер'
        
class WarfaceUserMainPvp(WarfaceUserMainInfo):
    profile_config = 'pvp'
    
class WarfaceUserMainPve(WarfaceUserMainInfo):
    profile_config = 'pve'



wf_user = WarfaceUserMainPvp('Пираний')
print(wf_user.sad.game_time)