from dataclasses import dataclass

@dataclass
class TestNorm: #struktura badania
    name: str
    kind: str|None
    units: list[str]
    norm: str

    def to_csv(self):
        units = ",".join(self.units)
        return f"{self.name};{self.kind};{units};{self.norm}"