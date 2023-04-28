from classes.CityClass import CityClass

class WorldCity(CityClass):

  def __init__(self, id_num, name, name2, country, population, area,
               population_density, growth_rate, rail_type):
    super().__init__(id_num, name, population, area, population_density,
                     growth_rate, rail_type)
    self.name2 = name2
    self.country = country

  def __str__(self):
    # string representation of the WorldCity class
    return f"ID: {self.id}\nName: {self.name}\nName2: {self.name2}\ncountry: {self.country}\nPopulation: {self.population}\
                  \nArea: {self.area}\nPopulation Density: {self.population_density}\nGrowth Rate: {self.growth_rate}\
                  \nRail Type: {self.rail_type}"
