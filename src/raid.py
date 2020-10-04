from texts import raidText

class Raid:
    """
    Raid class: define raid objects with a information and methods needed.
    """

    def __init__(self, RAID_ID, level, boss, time, gym, local, raid_list, mentions):
        self.level = level
        self.boss = boss
        self.time = time
        self.gym = gym
        self.local = local
        self.id = RAID_ID
        self.list = raid_list
        self.mentions = mentions
        self.text = raidText
    
    def get_text(self):
        output = self.text.format(self.level, self.boss, self.time, self.gym, self.local, self.id)
        index = 0
        for player in self.mentions:
            index+=1
            output+="\n{}. {}".format(index, player)
        return output
    
    def get_id(self):
        return self.id
    
    def set_level(self, level):
        self.level = level

    def set_boss(self, boss):
        self.boss = boss

    def set_time(self, time):
        self.time = time

    def set_gym(self, gym):
        self.gym = gym

    def set_local(self, local):
        self.local = local

    def set_list(self, lst):
        self.list = lst.copy()
    
    def get_list(self):
        return self.list

    def set_mentions(self, mentions):
        self.mentions = mentions.copy()

    def get_mentions(self):
        return self.mentions

        
