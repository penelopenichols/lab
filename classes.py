class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.channel = Television.MIN_CHANNEL
        self.volume = Television.MIN_VOLUME
        self.tvOn = False

    def power(self):
        if self.tvOn:
            self.tvOn = False
        else:
            self.tvOn = True

    def channel_up(self):
        if self.tvOn:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.tvOn:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.tvOn:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        if self.tvOn:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        return f"TV status: Is on = {self.tvOn}, Channel = {self.channel}, Volume = {self.volume}"
