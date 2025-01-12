from dataclasses import dataclass

@dataclass
class TestNorm:
    """
    Klasa definiuje strukturę pojedynczego badania.
    Atrybuty:
        name (str): Nazwa badania.
        kind (str | None): Nazwa podbadania (jeśli dotyczy).
        units (list[str]): Lista możliwych jednostek.
        norm (str): Zakres normy dla badania.
    """
    name: str
    kind: str|None
    units: list[str]
    norm: str

    def to_csv(self):
        """
        Konwertuje dane obiektu TestNorm na sformatowany ciąg tekstowy w formacie CSV.

        Zwraca:
            Dane badania w formacie CSV, gdzie poszczególne pola są oddzielone średnikami.
            Format: "nazwa badania;rodzaj podbadania;jednostki;norma".
        """
        units = ",".join(self.units)
        return f"{self.name};{self.kind};{units};{self.norm}"
