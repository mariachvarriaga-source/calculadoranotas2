# Registro Básico de Ventas Diarias

# Solicitar datos al usuario
nombre_cliente = input("Ingrese el nombre del cliente: ")

precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

vip_input = input("¿El cliente tiene membresía VIP? (si/no): ").lower()

# Convertimos a booleano
es_vip = vip_input == "si"

# Cálculos
subtotal = precio_unitario * cantidad

descuento = 0
if es_vip:
    descuento = subtotal * 0.10  # 10% de descuento

total_final = subtotal - descuento

# Mostrar resumen
print("\n----- RESUMEN DE LA VENTA -----")
print(f"Cliente: {nombre_cliente}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total final a pagar: ${total_final:.2f}")
