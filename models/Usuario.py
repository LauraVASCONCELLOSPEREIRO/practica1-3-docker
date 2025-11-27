from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar
import uuid

@dataclass
class Usuario:
    """Clase base para usuarios de la tienda."""
    nombre: str
    email: str
    id: str = ""
    _PREFIX: ClassVar[str] = "USR"
    
    def __post_init__(self) -> None:
        if not self.id:
            self.id = f"{self._PREFIX}-{uuid.uuid4()}"
    
    def is_admin(self) -> bool:
        """Por defecto, un usuario NO es admin."""
        return False
    
    def __str__(self) -> str:
        rol = "Admin" if self.is_admin() else "Cliente/Usuario"
        return f"[{self.id}] {self.nombre} <{self.email}> ({rol})"


@dataclass
class Cliente(Usuario):
    """Usuario de tipo cliente."""
    direccion: str = ""
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} <{self.email}> (Cliente) | Dirección: {self.direccion}"


@dataclass
class Administrador(Usuario):
    """Usuario con privilegios de administración."""
    def is_admin(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} <{self.email}> (Admin)"
