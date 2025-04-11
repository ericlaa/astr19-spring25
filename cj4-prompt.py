class Axolotl:
    def __init__(self, arm_length, leg_length, eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.eyes = eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Axolotl Physical Characteristics:")
        print(f"- Arm Length: {self.arm_length}")
        print(f"- Leg Length: {self.leg_length}")
        print(f"- Number of Eyes: {self.eyes}")
        print(f"- Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"- Is Furry: {'Yes' if self.is_furry else 'No'}")

my_axolotl = Axolotl(1.2, 3.4, 2, True, False)
my_axolotl.describe()
