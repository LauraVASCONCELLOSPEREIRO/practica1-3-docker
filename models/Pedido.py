from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Tuple
import uuid

from .Usuario import Cliente
from .Producto import Producto

LineaPedido = Tuple[Producto, int]

@dataclass
class Pedido:
    """Representa un pedido realizado por un cliente."""
    cliente: Cliente
    items: List[LineaPedido] = field(default_factory=list)
    fecha: datetime = field(default_factory=datetime.now)
    id: str = ""
    
    def __post_init__(self) -> None:
        if not self.id:
            self.id = f"ORD-{uuid.uuid4()}"
    
    @property
    def total(self) -> float:
        return sum(prod.precio * cantidad for prod, cantidad in self.items)
    
    def __str__(self) -> str:
        lineas = []
        for p, c in self.items:
            lineas.append(f"  - {p.nombre} x {c} = {(p.precio*c):.2f}€")
        detalle = "\n".join(lineas) if lineas else "  (sin artículos)"
        return (f"Pedido {self.id} | Fecha: {self.fecha:%Y-%m-%d %H:%M}\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Artículos:\n{detalle}\n"
                f"TOTAL: {self.total:.2f}€")
