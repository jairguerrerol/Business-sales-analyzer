import pandas as pd
import matplotlib.pyplot as plt

#lectura de datos
df = pd.read_csv("data/ventas.csv")

#caculo de ingresos
df["Ingresos"] = df["Precio"] * df["Cantidad"]

# Ventas totales
ventas_totales = sum(df["Ingresos"])

#producto mas vendido
producto_top= df.groupby("Producto")["Cantidad"].sum().idxmax()

#Ingresos por producto
ingresos_producto = df.groupby("Producto")["Ingresos"].sum().sort_values(ascending= False)

print(df)
print(f"""
====Reporte de Ventas====

Ventas totales: {ventas_totales}

Producto mas vendido: {producto_top}

Ingresos por producto: \n{ingresos_producto}

""")

#cracion de grafico
plt.figure(figsize=(8,5))
ingresos_producto.plot(kind="bar")
plt.title("Ingresos por producto")
plt.ylabel("Ingresos ($)")
plt.tight_layout()

#guardar grafico
plt.savefig("assets/grafico_ventas.png")
print("Grafico de ventas guardado en assets/grafico_ventas.png")