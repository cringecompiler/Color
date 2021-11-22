from abc import abstractmethod


class ComputerColor:
    @classmethod
    @abstractmethod
    def __repr__(cls):
        pass

    @classmethod
    @abstractmethod
    def __mul__(cls, other):
        pass

    @classmethod
    @abstractmethod
    def __rmul__(cls, other):
        pass


class RGBColor(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, RGBColor):
            return False
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __add__(self, other):
        if not isinstance(other, RGBColor):
            raise ValueError(f"Сложение цвета с {type(other)} недопустимо")
        return RGBColor(min(self.red + other.red, 255),
                        min(self.green + other.green, 255),
                        min(self.blue + other.blue, 255)
                        )

    def __mul__(self, other: float):
        if 0 <= other <= 1:
            cl = -256 * (1 - other)
            F = (259 * (cl + 255)) / (255 * (259 - cl))
            return RGBColor(int(F * (self.red - 128) + 128),
                            int(F * (self.green - 128) + 128),
                            int(F * (self.blue - 128) + 128)
                            )
        raise ValueError

    __rmul__ = __mul__

    def __hash__(self):
        return hash((self.red, self.green, self.blue))


class HSLColor(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __repr__(self):
        return f'{self.START};{0};{0};{0}{self.MOD}●{self.END}{self.MOD}'

    def __mul__(self, other):
        return HSLColor()

    __rmul__ = __mul__


def print_a(color: ComputerColor):
    """вывод в консоль буквы А в определенном цвете"""
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


if __name__ == '__main__':
    orange1 = RGBColor(255, 165, 0)
    red = RGBColor(255, 0, 0)
    green = RGBColor(0, 255, 0)
    orange2 = RGBColor(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(red + green)
    print(set(color_list))
    print(0.5 * red)
    print_a(red)
    dark = HSLColor()
    print_a(dark)
