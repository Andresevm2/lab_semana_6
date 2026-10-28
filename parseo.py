def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    if not isinstance(linea, str):
        raise ValueError("La línea debe ser una cadena de texto.")
    
    partes = linea.split(",")
    if len(partes) != 4:
        raise ValueError("La línea debe contener exactamente 4 elementos.")
    
    codigo = partes[0].strip()
    nombre = partes[1].strip()
    
    try:
        precio = float(partes[2].strip())
        if precio < 0:
            raise ValueError
    except ValueError:
        raise ValueError("Precio inválido.")
        
    try:
        cantidad = int(partes[3].strip())
        if cantidad < 0:
            raise ValueError
    except ValueError:
        raise ValueError("Cantidad inválida.")
        
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }


def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    prod = parsear_producto(linea)
    valor = round(prod["precio"] * prod["cantidad"], 1)
    return f"{prod['codigo']} - {prod['nombre']}: ${valor}"


def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    if not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("La lista no puede estar vacía.")
    
    salida = []
    for linea in lineas:
        salida.append(resumen_de_producto(linea))
    return salida


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    if not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("La lista no puede estar vacía.")
        
    total = 0.0
    for linea in lineas:
        prod = parsear_producto(linea)
        total += prod["precio"] * prod["cantidad"]
    return round(total, 1)


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    if not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("La lista no puede estar vacía.")
        
    mejor_linea = lineas[0]
    prod_mejor = parsear_producto(mejor_linea)
    mejor_valor = prod_mejor["precio"] * prod_mejor["cantidad"]
    
    for linea in lineas[1:]:
        prod = parsear_producto(linea)
        valor = prod["precio"] * prod["cantidad"]
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_linea = linea
            
    return resumen_de_producto(mejor_linea)


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    # Ejemplos activos para visualizar la ejecución
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
