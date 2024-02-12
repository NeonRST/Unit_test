"""An enumeration of known types of units."""
import enum


def unit_type_return(class_name: str):
    for unit in list(UnitType):
        if class_name in unit.value:
            return unit.cls
    for length in list(LengthUnit):
        if class_name in length.value:
            return length
    for temp in list(TempUnit):
        if class_name in temp.value:
            return temp
    for time in list(TimeUnit):
        if class_name in time.value:
            return time
    for memory in list(MemoryUnit):
        if class_name in memory.value:
            return memory
    return "Unknown"


class LengthUnit(enum.Enum):
    """This class collect all length unit"""
    cm = (1, "Centimeter")
    mm = (0.1, "Millimeter")
    km = (100000, "Kilometer")
    m = (100, "Meter")
    wa = (200, "Wa")
    sok = (50, "Sok")

    def __init__(self, val1, val2):
        """initialize of LengthUnit"""
        self.val_start = val1
        self.val_end = val2

    def __str__(self):
        return self.val_end

    @staticmethod
    def convert(unit1, unit2, user_input):
        if unit1.value == "Centimeter":
            return f"{user_input * unit2.val_start:.5g}"
        return f"{(user_input * unit1.val_start) / unit2.val_start:.5g}"


class TempUnit(enum.Enum):
    """Define the unit_types here.  The value is the printable type name."""
    celsius = ({"initial": 0, "multiply": 1}, "Celsius")
    fahrenheit = ({"initial": 32, "multiply": 1.8}, "Fahrenheit")
    kelvin = ({"initial": 273.15, "multiply": 1}, "Kelvin")

    def __init__(self, val1, val2):
        self.val_start = val1
        self.val_end = val2

    def __str__(self):
        return self.val_end

    @staticmethod
    def convert(unit1, unit2, user_input):
        if unit1.value == "Celsius":
            return f"{unit2.val_start['initial'] + (unit2.val_start['multiply'] * user_input):.5g}"
        return \
            f"{unit2.val_start['multiply'] * ((user_input - unit1.val_start['initial']) / unit1.val_start['multiply']) + unit2.val_start['initial']:.5g}"


class TimeUnit(enum.Enum):
    """This class collect all money unit"""
    sec = (3600, "Second")
    minute = (60, "Minute")
    hour = (1, "Hour")
    day = (1/24, "Day")

    def __init__(self, val1, val2):
        self.val_start = val1
        self.val_end = val2

    @staticmethod
    def convert(unit1, unit2, user_input):
        if "Hour" in unit1.value:
            return f"{user_input * unit2.val_start:.5g}"
        return f"{(user_input / unit1.val_start) * unit2.val_start:.5g}"

    def __str__(self):
        return self.val_end


class MemoryUnit(enum.Enum):
    """This class collect all money unit"""
    bit = (1, "Binary Digit")
    byte = (8, "Byte")
    kb = (1024, "Kilo Byte")
    mb = (1024**2, "Mega Byte")
    gb = (1024**3, "Giga Byte")
    tb = (1024**4, "Terra Byte")

    @staticmethod
    def convert(unit1, unit2, user_input):
        if "Binary Digit" in unit1.value:
            return f"{user_input * unit2.val_start:.5g}"
        return f"{(user_input * unit1.val_start) / unit2.val_start:.5g}"

    def __init__(self, val1, val2):
        self.val_start = val1
        self.val_end = val2

    def __str__(self):
        return self.val_end


class UnitType(enum.Enum):
    length = ("Length", LengthUnit)
    time = ("Time", TimeUnit)
    temperature = ("Temperature", TempUnit)
    memory = ("Memory", MemoryUnit)

    def __init__(self, name, cls):
        self.cls_name = name
        self.__cls = cls

    @property
    def cls(self):
        return self.__cls

    def __str__(self):
        return self.cls_name
