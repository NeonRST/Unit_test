import unittype
from converter import UnitConverter
from converter_ui import ConverterUI
if __name__ == '__main__':
    convert = UnitConverter()
    x = unittype.UnitType
    ui = ConverterUI(convert, x)
    ui.run()


