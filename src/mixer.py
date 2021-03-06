import os
import pygame

DIRNAME = os.path.dirname(__file__)

class Mixer:
    """A class for playing sounds and music

    Attributes:
        track_list: a list of track names
        paused: boolean value if music is currently playing or not
    """
    def __init__(self):
        """A class constructor

        Attributes:
            track_list: a list of track names
            paused: boolean value if music is currently playing or not
        """
        pygame.mixer.pre_init()
        pygame.mixer.init()
        self.track_list = {0:"bgm1.wav"}
        self.paused = False

    def load_track(self, track):
        pygame.mixer.music.load(os.path.join(DIRNAME, "assets", self.track_list[track]))

    def unload_track(self):
        pygame.mixer.music.unload()

    def set_volume(self, volume=0.3):
        pygame.mixer.music.set_volume(volume)

    def play_music(self, loops=-1):
        pygame.mixer.music.play(loops=loops)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        """Pauses or unpauses music if called
        """
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False
