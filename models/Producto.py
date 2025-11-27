from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar
import uuid

@dataclass
class Producto:
    """Clase base para productos de la tienda.
    
    Atributos:
        id: identificador único (UUID en str)
        nombre: nombre comercial del producto
        precio: precio unitario en euros
        stock: unidades disponibles
    """
    nombre: str
    precio: float
    stock: int
    id: str = ""
    
    _PREFIX: ClassVar[str] = "PRD"
    
    def __post_init__(self) -> None:
        if not self.id:
            self.id = f"{self._PREFIX}-{uuid.uuid4()}"
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")
    
    def tiene_stock(self, cantidad: int) -> bool:
        """Devuelve True si hay al menos 'cantidad' en stock."""
        return cantidad >= 0 and self.stock >= cantidad
    
    def actualizar_stock(self, delta: int) -> None:
        """Suma (o resta si es negativo) unidades al stock.
        Lanza ValueError si el resultado sería negativo.
        """
        nuevo = self.stock + delta
        if nuevo < 0:
            raise ValueError("No hay suficiente stock para realizar la operación")
        self.stock = nuevo
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio:.2f}€ (stock: {self.stock})"


@dataclass
class ProductoElectronico(Producto):
    """Producto electrónico con meses de garantía."""
    meses_garantia: int = 24
    
    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} - {self.precio:.2f}€ "
                f"(stock: {self.stock}) | Garantía: {self.meses_garantia} meses")


@dataclass
class ProductoRopa(Producto):
    """Producto de ropa con talla y color."""
    talla: str = "M"
    color: str = "negro"
    
    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} - {self.precio:.2f}€ "
                f"(stock: {self.stock}) | Talla: {self.talla}, Color: {self.color}")
