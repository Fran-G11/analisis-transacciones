try:
    transacciones = input("Ingrese las transacciones separadas por comas (ejemplo: 100,-50,200,-30): ")
    transacciones = [float(t.strip()) for t in transacciones.split(",")]

    depositos = sum(t for t in transacciones if t > 0)
    retiros = sum(t for t in transacciones if t < 0)
    saldo_final = sum(transacciones)

    # Cálculos avanzados
    promedio_depositos = depositos / len([t for t in transacciones if t > 0]) if depositos > 0 else 0
    promedio_retiros = abs(retiros) / len([t for t in transacciones if t < 0]) if retiros < 0 else 0
    max_transaccion = max(transacciones)
    min_transaccion = min(transacciones)

    # Filtro por umbral
    umbral = float(input("Ingrese un umbral para filtrar transacciones: "))
    transacciones_filtradas = [t for t in transacciones if abs(t) > umbral]

    print(f"Total de depósitos: {depositos:.2f}")
    print(f"Total de retiros: {abs(retiros):.2f}")
    print(f"Saldo final: {saldo_final:.2f}")
    print(f"Promedio de depósitos: {promedio_depositos:.2f}")
    print(f"Promedio de retiros: {promedio_retiros:.2f}")
    print(f"Transacción máxima: {max_transaccion:.2f}")
    print(f"Transacción mínima: {min_transaccion:.2f}")
    print(f"Transacciones mayores al umbral: {transacciones_filtradas}")
except ValueError:
    print("Error: Pro favor ingrese valores numéricos válidos.")
