from django.db import models

class Character(models.Model):
    # Core details
    name = models.CharField(max_length=100)
    # race = models.CharField(max_length=50)  # E.g., Human, Elf
    # character_class = models.CharField(max_length=50)  # E.g., Fighter, Wizard
    # background = models.CharField(max_length=100)  # E.g., Acolyte, Soldier
    # alignment = models.CharField(max_length=50)  # E.g., Chaotic Good, Neutral
    #
    # # Ability scores
    # strength = models.IntegerField()
    # dexterity = models.IntegerField()
    # constitution = models.IntegerField()
    # intelligence = models.IntegerField()
    # wisdom = models.IntegerField()
    # charisma = models.IntegerField()
    #
    # # Additional attributes
    # level = models.IntegerField(default=1)
    # experience_points = models.IntegerField(default=0)
    # hit_points = models.IntegerField()
    # armor_class = models.IntegerField()
    # initiative = models.IntegerField()
    # speed = models.IntegerField()  # Typically in feet
    #
    # # Skills (as per the Player's Handbook)
    # acrobatics = models.BooleanField(default=False)
    # animal_handling = models.BooleanField(default=False)
    # arcana = models.BooleanField(default=False)
    # athletics = models.BooleanField(default=False)
    # deception = models.BooleanField(default=False)
    # history = models.BooleanField(default=False)
    # insight = models.BooleanField(default=False)
    # intimidation = models.BooleanField(default=False)
    # investigation = models.BooleanField(default=False)
    # medicine = models.BooleanField(default=False)
    # nature = models.BooleanField(default=False)
    # perception = models.BooleanField(default=False)
    # performance = models.BooleanField(default=False)
    # persuasion = models.BooleanField(default=False)
    # religion = models.BooleanField(default=False)
    # sleight_of_hand = models.BooleanField(default=False)
    # stealth = models.BooleanField(default=False)
    # survival = models.BooleanField(default=False)
    #
    # # Proficiencies and equipment
    # proficiencies = models.TextField(blank=True)  # JSON or CSV format
    # equipment = models.TextField(blank=True)  # JSON or CSV format
    #
    # # Spells and features
    # spells = models.TextField(blank=True)  # JSON or CSV format
    # features_and_traits = models.TextField(blank=True)  # JSON or CSV format

    def __str__(self):
        # return f"{self.name} ({self.character_class})"
        return f"{self.name}"
