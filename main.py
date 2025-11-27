from Services.Tienda_service import TiendaService

def imprimir_inventario(service: TiendaService) -> None:
    print("\n== INVENTARIO ==")
    for p in service.listar_productos():
        print(p)

def imprimir_historial(service: TiendaService, cliente_id: str) -> None:
    print("\n== HISTÓRICO DE PEDIDOS ==")
    pedidos = service.listar_pedidos_por_usuario(cliente_id)
    if not pedidos:
        print("No hay pedidos para este cliente.")
    for ped in pedidos:
        print(ped)
        print("-" * 40)

def main() -> None:
    tienda = TiendaService()
    
    # ---- Registrar usuarios ----
    c1 = tienda.registrar_usuario("cliente", nombre="Lucía Vidal", email="lucia.vidal@example.com", direccion="C/ Río Miño 12, Ourense")
    c2 = tienda.registrar_usuario("cliente", nombre="Mario Castaño", email="mario.castano@example.com", direccion="Av. do Mar 45, A Coruña")
    c3 = tienda.registrar_usuario("cliente", nombre="Eva Tejero", email="eva.tejero@example.com", direccion="Rúa das Letras 3, Lugo")
    admin = tienda.registrar_usuario("administrador", nombre="Sofía Campos", email="sofia.campos@example.com")
    
    # ---- Crear productos ----
    p1 = tienda.crear_producto_electronico("Portátil Acer Aspire 3", precio=549.99, stock=5, meses_garantia=24)
    p2 = tienda.crear_producto_electronico("Auriculares inalámbricos NovaGo", precio=39.90, stock=15, meses_garantia=12)
    p3 = tienda.crear_producto_ropa("Sudadera básica Unisex", precio=24.50, stock=20, talla="M", color="gris")
    p4 = tienda.crear_producto_ropa("Pantalón chino", precio=29.99, stock=18, talla="42", color="azul marino")
    p5 = tienda.crear_producto_ropa("Camiseta deportiva", precio=14.99, stock=25, talla="L", color="verde")
    
    # ---- Listar productos ----
    imprimir_inventario(tienda)
    
    # ---- Realizar pedidos ----
    pedido1 = tienda.realizar_pedido(c1.id, items=[(p1.id, 1), (p3.id, 2)])
    pedido2 = tienda.realizar_pedido(c2.id, items=[(p2.id, 1), (p4.id, 1)])
    pedido3 = tienda.realizar_pedido(c3.id, items=[(p3.id, 1), (p4.id, 2), (p5.id, 1)])
    
    print("\n== PEDIDOS REALIZADOS ==")
    print(pedido1); print("-" * 40)
    print(pedido2); print("-" * 40)
    print(pedido3); print("-" * 40)
    
    # ---- Ver stock actualizado ----
    imprimir_inventario(tienda)
    
    # ---- Historial de un cliente ----
    imprimir_historial(tienda, c1.id)

if __name__ == "__main__":
    main()
