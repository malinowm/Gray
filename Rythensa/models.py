from django.db import models

class Character(model.Model):
    #Base Stats
    maxHp = models.PositiveIntegerField()
    maxAp = models.PositiveIntegerField()
    maxPp = models.PositiveIntegerField()
    baseStrength = models.PositiveIntegerField()
    baseAgility = models.PositiveIntegerField()
    baseAura = models.PositiveIntegerField()
    baseConstitution = models.PositiveIntegerField()
    baseCaliber = models.PositiveIntegerField()
    baseFocus = models.PositiveIntegerField()

    #Skill Tree Stats
    perception = models.PositiveIntegerField()
    enhancement = models.PositiveIntegerField()
    metaphysical = models.PositiveIntegerField()
    elemental = models.PositiveIntegerField()
    veils = models.PositiveIntegerField()
    metamorphosis = models.PositiveIntegerField()
    conjuring = models.PositiveIntegerField()
    manipulation = models.PositiveIntegerField()
    empathy = models.PositiveIntegerField()
    healing = models.PositiveIntegerField()

    #Character Info
    name = models.CharField(max_length=100)
    owner = #many characters to one owner
    race = #many characters to one race
    element = #many characters to one element

    #Equipment/Ability Info
    weapon = #many characters to one weapon
    armor = #many characters to one armor
    accessories = #many to many
    abilities = #many to many(or just a list of strings)

    def __unicode__(self):
        return self.name
