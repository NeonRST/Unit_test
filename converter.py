"""this module is for UnitConverter"""


class UnitConverter:
    """This class use for calculate the value"""
    def __init__(self):
        """initialize of Converter class"""
        self.unit_calculate_type = None
        self.val_start = None
        self.val_end = None

    def input1_set(self, new_val):
        """val_start setter"""
        self.val_start = new_val

    def input2_set(self, new_val):
        """val_end setter"""
        self.val_end = new_val

    def calculate_unit(self, val: int or float, unit_calculate_type):
        """this method return converted value"""
        self.unit_calculate_type = unit_calculate_type
        return self.unit_calculate_type.convert(self.val_start, self.val_end, val)

    @staticmethod
    def return_unit(type_of_unit):
        """return units"""
        try:
            return list(type_of_unit)
        except TypeError or ValueError:
            return None

