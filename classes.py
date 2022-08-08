class Television:
    """
    A class representing details for Television objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Constructor to create initial state of Television object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__tvOn = False

    def power(self):
        """
        Method to change bool __tvOn
        """
        if self.__tvOn:
            self.__tvOn = False
        else:
            self.__tvOn = True

    def channel_up(self):
        """
        Method to increment int __channel by one if __tvOn is True,
        and if __channel is less than MAX_CHANNEL.
        If __channel is equal to MAX_CHANNEL, it is assigned MIN_CHANNEL
        """
        if self.__tvOn:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrement int __channel by one if __tvOn is True,
        and if __channel is greater than MIN_CHANNEL.
        If __channel is equal to MIN_CHANNEL, it is assigned MAX_CHANNEL
        """
        if self.__tvOn:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increment __volume by one if __tvOn is True,
         and if __volume is less than MAX_VOLUME
        """
        if self.__tvOn:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Method to decrement __volume by one if __tvOn is True,
        and if __volume is greater than MIN_VOLUME
        """
        if self.__tvOn:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method to return the Television object's status
        including __tvOn, __channel, and __volume
        :return: String containing TV status
        """
        return f"TV status: Is on = {self.__tvOn}, Channel = {self.__channel}, Volume = {self.__volume}"
