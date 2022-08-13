from dataclasses import dataclass


@dataclass
class Cart:
    goodId: str = None
    productId: str = None
    number: int = None
