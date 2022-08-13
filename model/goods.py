from dataclasses import dataclass


@dataclass
class Goods:
    id: str = None
    name: str = None
    retailPrice: int = None
    productId: int = None