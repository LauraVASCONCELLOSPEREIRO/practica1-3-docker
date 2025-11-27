from __future__ import annotations
from typing import Dict, List, Tuple, Literal, Optional
from datetime import datetime

from models.Usuario import Usuario, Cliente, Administrador
from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Pedido import Pedido

TipoUsuario = Literal["cliente", "administrador"]
LineaCompra = Tuple[str, int]  # (id_producto, cantidad)


class TiendaService:
    """Servicio central de la tienda: gestiona usuarios, productos y pedidos."""
    def __init__(self) -> None:
        self._usuarios: Dict[str, Usuario] = {}
        self._productos: Dict[str, Producto] = {}
        self._pedidos: List[Pedido] = []
    
    # ---------- Usuarios ----------
    def registrar_usuario(self, tipo: TipoUsuario, nombre: str, email: str, direccion: str = "") -> Usuario:
        if tipo == "cliente":
            u = Cliente(nombre=nombre, email=email, direccion=direccion)
        elif tipo == "administrador":
            u = Administrador(nombre=nombre, email=email)
        else:
            raise ValueError("Tipo de usuario no válido. Use 'cliente' o 'administrador'.")
        self._usuarios[u.id] = u
        return u
    
    def obtener_usuario(self, usuario_id: str) -> Optional[Usuario]:
        return self._usuarios.get(usuario_id)
    
    # ---------- Productos ----------
    def anadir_producto(self, producto: Producto) -> Producto:
        self._productos[producto.id] = producto
        return producto
    
    def crear_producto_electronico(self, nombre: str, precio: float, stock: int, meses_garantia: int = 24) -> ProductoElectronico:
        p = ProductoElectronico(nombre=nombre, precio=precio, stock=stock, meses_garantia=meses_garantia)
        return self.anadir_producto(p)
    
    def crear_producto_ropa(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> ProductoRopa:
        p = ProductoRopa(nombre=nombre, precio=precio, stock=stock, talla=talla, color=color)
        return self.anadir_producto(p)
    
    def eliminar_producto(self, producto_id: str) -> bool:
        return self._productos.pop(producto_id, None) is not None
    
    def listar_productos(self) -> List[Producto]:
        return list(self._productos.values())
    
    def obtener_producto(self, producto_id: str) -> Optional[Producto]:
        return self._productos.get(producto_id)
    
    # ---------- Pedidos ----------
    def realizar_pedido(self, cliente_id: str, items: List[LineaCompra]) -> Pedido:
        usuario = self._usuarios.get(cliente_id)
        if usuario is None:
            raise ValueError("El usuario no existe")
        if not isinstance(usuario, Cliente):
            raise PermissionError("Solo los clientes pueden realizar pedidos")
        
        # Comprobar stock
        lineas: List[Tuple[Producto, int]] = []
        for prod_id, cantidad in items:
            prod = self._productos.get(prod_id)
            if prod is None:
                raise ValueError(f"Producto con id {prod_id} no existe")
            if not prod.tiene_stock(cantidad):
                raise ValueError(f"No hay stock suficiente de '{prod.nombre}' (solicitado: {cantidad}, disponible: {prod.stock})")
            lineas.append((prod, cantidad))
        
        # Descontar stock
        for prod, cantidad in lineas:
            prod.actualizar_stock(-cantidad)
        
        pedido = Pedido(cliente=usuario, items=lineas)
        self._pedidos.append(pedido)
        return pedido
    
    def listar_pedidos_por_usuario(self, cliente_id: str) -> List[Pedido]:
        pedidos = [p for p in self._pedidos if p.cliente.id == cliente_id]
        pedidos.sort(key=lambda p: p.fecha)  # orden por fecha ascendente
        return pedidos
