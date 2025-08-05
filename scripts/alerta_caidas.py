import pandas as pd
import os
from datetime import datetime

# =========================
# Configuraciones
# =========================
UMBRAL_CAIDA = -0.3
RUTA_EXCEL = "../data/ventas_semanales_100.xlsx"
RUTA_LOGS = "./logs"
RUTA_OUTPUTS = "./outputs"

# =========================
# Función principal
# =========================
def main():
    df = pd.read_excel(RUTA_EXCEL)

    # Validación de columnas mínimas
    if "Semana" not in df.columns or "Ventas" not in df.columns:
        mensaje = " El archivo no contiene las columnas requeridas: 'Semana' y 'Ventas'"
        loggear(mensaje)
        print(mensaje)
        return

    df = df.sort_values(by='Semana')

    ventas_por_semana = df.groupby("Semana")["Ventas"].sum().reset_index()
    
    if len(ventas_por_semana) < 2:
        mensaje = " No hay suficientes semanas para comparar."
        loggear(mensaje)
        print(mensaje)
        return

    ventas_recientes = ventas_por_semana.tail(2)
    semana_anterior = ventas_recientes.iloc[0]["Semana"]
    semana_actual = ventas_recientes.iloc[1]["Semana"]

    total_anterior = ventas_recientes.iloc[0]["Ventas"]
    total_actual = ventas_recientes.iloc[1]["Ventas"]

    variacion = (total_actual - total_anterior) / total_anterior

    if variacion < UMBRAL_CAIDA:
        porcentaje = abs(round(variacion * 100, 2))
        df_actual = df[df["Semana"] == semana_actual]

        top_caidas = df_actual.sort_values("Ventas").head(10)
        resumen = (
            f" Alerta de caída del {porcentaje}% entre semana {semana_anterior} y {semana_actual}\n"
            f" Top productos con menores ventas:\n"
        )
        resumen += "\n".join(f"- {row['Producto']}: {row['cantidad']}" for _, row in top_caidas.iterrows())

        loggear(resumen)
        exportar_excel(top_caidas)
        print(resumen)
    else:
        mensaje = f" Sin caídas relevantes de ventas entre semana {semana_anterior} y {semana_actual}"
        loggear(mensaje)
        print(mensaje)

# =========================
# Guardar log en /logs
# =========================
def loggear(texto):
    os.makedirs(RUTA_LOGS, exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d")
    ruta_completa = os.path.join(RUTA_LOGS, f"log_{fecha}.txt")
    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(texto)

# =========================
# Guardar Excel en /outputs
# =========================
def exportar_excel(df):
    os.makedirs(RUTA_OUTPUTS, exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d")
    ruta_excel = os.path.join(RUTA_OUTPUTS, f"productos_criticos_{fecha}.xlsx")
    df.to_excel(ruta_excel, index=False)

# =========================
# Entrada
# =========================
if __name__ == "__main__":
    main()
