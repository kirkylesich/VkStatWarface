class ViewBase:
    def __init__(self, wf_user):
        self.wf_user = wf_user

    
class ViewProfile(ViewBase):
    
    def get_view_profile(self):
        view = open('views/wf_profile.txt').read()
        return view.format(
            self.wf_user.username,
            self.wf_user.server,
            self.wf_user.player_type,
            self.wf_user.rank,
            self.wf_user.experience,
            self.wf_user.longest_match,
            self.wf_user.total_match_duration,
            self.wf_user.game_time,
            self.wf_user.clan,
            self.wf_user.replenished_bp,
            self.wf_user.restored_hp_value,
            self.wf_user.count_of_reanimated_players,
            self.wf_user.restored_ob_value,
        )

class ViewPvpProfile(ViewBase):
    
    def get_view_profile(self):
        view = open('views/wf_pvp_profile.txt').read()
        return view.format(
            self.wf_user.all_kills,
            self.wf_user.all_shoots,
            self.wf_user.hits_in_target,
            self.wf_user.kills_with_mine,
            self.wf_user.kills_with_knife,
            self.wf_user.suicides_and_friendlyfire_kills,
            self.wf_user.best_kill_combo,
            self.wf_user.deaths,
            self.wf_user.ratio_deaths_kills,
            self.wf_user.count_all_matches,
            self.wf_user.count_all_victories,
            self.wf_user.count_all_draws,
            self.wf_user.winrate,
            self.wf_user.count_kicks_from_match,
            self.wf_user.count_interrupted_mathces,
            self.wf_user.game_time,
            self.wf_user.rifleman.all_shoots,
            self.wf_user.rifleman.hits_in_target,
            self.wf_user.rifleman.hit_accuracy,
            self.wf_user.rifleman.hits_in_head,
            self.wf_user.rifleman.hits_in_head_with_knife,
            self.wf_user.rifleman.game_time,

            self.wf_user.medic.all_shoots,
            self.wf_user.medic.hits_in_target,
            self.wf_user.medic.hit_accuracy,
            self.wf_user.medic.hits_in_head,
            self.wf_user.medic.hits_in_head_with_knife,
            self.wf_user.medic.game_time,

            self.wf_user.sad.all_shoots,
            self.wf_user.sad.hits_in_target,
            self.wf_user.sad.hit_accuracy,
            self.wf_user.sad.hits_in_head,
            self.wf_user.sad.hits_in_head_with_knife,
            self.wf_user.sad.game_time,

            self.wf_user.engineer.all_shoots,
            self.wf_user.engineer.hits_in_target,
            self.wf_user.engineer.hit_accuracy,
            self.wf_user.engineer.hits_in_head,
            self.wf_user.engineer.hits_in_head_with_knife,
            self.wf_user.engineer.game_time,

            self.wf_user.sniper.all_shoots,
            self.wf_user.sniper.hits_in_target,
            self.wf_user.sniper.hit_accuracy,
            self.wf_user.sniper.hits_in_head,
            self.wf_user.sniper.hits_in_head_with_knife,
            self.wf_user.sniper.game_time,
        )

class ViewPveProfile(ViewBase):

    def get_view_profile(self):
        view = open('views/wf_pve_profile.txt').read()
        return view.format(
            self.wf_user.all_kills,
            self.wf_user.all_shoots,
            self.wf_user.hits_in_target,
            self.wf_user.kills_with_mine,
            self.wf_user.kills_with_knife,
            self.wf_user.suicides_and_friendlyfire_kills,
            self.wf_user.best_kill_combo,
            self.wf_user.deaths,
            self.wf_user.ratio_deaths_kills,
            self.wf_user.count_all_matches,
            self.wf_user.count_all_victories,
            self.wf_user.count_all_draws,
            self.wf_user.winrate,
            self.wf_user.count_kicks_from_match,
            self.wf_user.count_interrupted_mathces,
            self.wf_user.count_of_signs,
            self.wf_user.game_time,

            self.wf_user.rifleman.all_shoots,
            self.wf_user.rifleman.hits_in_target,
            self.wf_user.rifleman.hit_accuracy,
            self.wf_user.rifleman.hits_in_head,
            self.wf_user.rifleman.hits_in_head_with_knife,
            self.wf_user.rifleman.game_time,

            self.wf_user.medic.all_shoots,
            self.wf_user.medic.hits_in_target,
            self.wf_user.medic.hit_accuracy,
            self.wf_user.medic.hits_in_head,
            self.wf_user.medic.hits_in_head_with_knife,
            self.wf_user.medic.game_time,

            self.wf_user.sad.all_shoots,
            self.wf_user.sad.hits_in_target,
            self.wf_user.sad.hit_accuracy,
            self.wf_user.sad.hits_in_head,
            self.wf_user.sad.hits_in_head_with_knife,
            self.wf_user.sad.game_time,

            self.wf_user.engineer.all_shoots,
            self.wf_user.engineer.hits_in_target,
            self.wf_user.engineer.hit_accuracy,
            self.wf_user.engineer.hits_in_head,
            self.wf_user.engineer.hits_in_head_with_knife,
            self.wf_user.engineer.game_time,

            self.wf_user.sniper.all_shoots,
            self.wf_user.sniper.hits_in_target,
            self.wf_user.sniper.hit_accuracy,
            self.wf_user.sniper.hits_in_head,
            self.wf_user.sniper.hits_in_head_with_knife,
            self.wf_user.sniper.game_time,
        )

class ViewAllCommands:

    def get_view(self):
        view = open('views/all_commands.txt').read()
        return view