from dataclasses import dataclass


@dataclass
class Example:
    """
    Invariant: attr > 0
    """

    attr: int

    @property
    def attr(self) -> int:
        return self._attr

    @attr.setter
    def attr(self, attr: int) -> None:
        if attr >= 0:
            self._attr = attr
            return
        print("Attr must be positive")

    def print_public(self):
        print(f"here is the public: {self.attr}")


example = Example(10)

print(example.attr)
example.print_public()
example.attr = 9

print(example.attr)
example.print_public()

example.attr = -1
print(example.attr)

example.print_public()
