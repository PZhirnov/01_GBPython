class Road:
    __weight_per_one = 25
    __asphalt_thickness = 5

    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def mass_calculation_t(self):
        mass_res = (self._lenght * self._width *
                    self.__weight_per_one * self.__asphalt_thickness) / 1000
        return mass_res


your_road = Road(20, 5000)
res_mass = your_road.mass_calculation_t()
print('{:,g}'.format(res_mass).replace(',', ' '), 'т.')
