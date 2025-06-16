
import pandas as pd
from datetime import datetime
import pywhatkit as kit
import time

df = pd.read_csv("cumpleaños.csv")

hoy = datetime.now().strftime("%d-%m")

for index, fila in df.iterrows():
    if fila["Fecha"] == hoy:
        numero = str(fila["Telefono"])
        nombre = fila["Nombre"]
        mensaje = f"🎉 Feliz cumpleeeee!!!! {nombre} 🎂🎁 que tengas un dia muy lindo tkm! ❤️ sabes que eres muy importante para mi por eso nunca olvido tu cumple! 💕"

        horaActual = datetime.now()
        horaEnvio = horaActual.hour
        minutoEnvio = horaActual.minute + 1

        try:
            kit.sendwhatmsg(numero, mensaje, horaEnvio, minutoEnvio)
            print(f"Mensaje programado para {nombre} ({numero}) a las {horaEnvio}:{minutoEnvio}")
            time.sleep(10)
        except Exception as e:
            print(f"Error enviando mensaje a {nombre}: {e}")