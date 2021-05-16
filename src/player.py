from entity import Entity
from spritesheet import Spritesheet

SPRITE_SHEET = Spritesheet("player-spritesheet.png")
STAB_SPRITE_SHEET = Spritesheet("playerstab.png")
PLAYER_SHIELDED_SHEET = Spritesheet("playershielded-sheet.png")

class Player(Entity):
    """A player class

    Attributes:
        direction: which direction this entity is currently facing (0-3)
        images: a list of pygame.images
        stab_images: a list of pygame images
        shielded_images: a list of pygame images
        image: current image
        rect: pygame rect object
        health_capacity: maximum amount of health
        current_health: current amount of health
        shielded: boolean, True if player is shielded
        inventory: a dict which keeps track of players inventory
    """
    def __init__(self, map_pos_x, map_pos_y, pos_x=0, pos_y=0):
        """A class constructor

        Args:
            map_pos_x: spot on the map on the x-axis
            map_pos_y: spot on the map on the y-axis
            pos_x: spot on the screen on the x-axis
            pos_y: spot on the screen on the y-axis
        """
        super().__init__(map_pos_x, map_pos_y)
        self.images = [SPRITE_SHEET.load_strip((0, i*50, 50, 50), 4, -1)
                       for i in range(4)]

        self.direction = 2
        self.stab_images = STAB_SPRITE_SHEET.load_strip((0, 0, 50, 50), 4, -1)
        self.shielded_images = PLAYER_SHIELDED_SHEET.load_strip((0, 0, 50, 50), 4, -1)
        self.image = self.images[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.health_capacity = 10
        self.current_health = 10
        self.shielded = False
        self.inventory = {"Sword":1,
                          "Shield":1,
                          "Potion":1}

    def change_direction(self, direction):
        """A method which changes the direction which this entity is facing

        Args:
            direction: integer (0-3)
        """
        self.direction = direction
        self.image = self.images[self.direction][self.frame]

    def update(self, current_time):
        """A method which updates animations
        """
        if self.shielded:
            return

        if current_time - self.last_updated >= 120:
            if self.attack:
                self.attack_animation()
            else:
                self.walking_animation()
                self.image = self.images[self.direction][self.frame]
            self.last_updated = current_time

    def attack_animation(self):
        """A method which updates attack animation
        """
        if self.image in self.stab_images:
            self.attack = False
            self.image = self.images[self.direction][0]
        else:
            self.image = self.stab_images[self.direction]

    def apply_shield(self):
        """A method which applies shielding
        """
        if self.shielded:
            self.shielded = False
            self.image = self.images[self.direction][self.frame]
        else:
            self.shielded = True
            self.image = self.shielded_images[self.direction]

    def consume_potion(self):
        """A method which checks if there are any potions left in the inventory
        and consumes one, healing the player by 5 health
        """
        if self.inventory["Potion"] > 0:
            self.inventory["Potion"] -= 1
            if self.current_health + 5 > self.health_capacity:
                self.current_health = self.health_capacity
            else:
                self.current_health += 5
