from classes import *


class Test:
    def setup_method(self):
        self.TV = Television()

    def test_power(self):
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.TV.power()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.TV.power()
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.TV.channel_up()
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.TV.power()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.TV.channel_up()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.TV.channel_up()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.TV.channel_up()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.TV.channel_up()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.TV.channel_down()
        assert self.TV.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.TV.power()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.TV.channel_down()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.TV.channel_down()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.TV.channel_down()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.TV.channel_down()
        assert self.TV.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

