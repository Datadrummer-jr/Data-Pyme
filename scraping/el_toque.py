from httpx import Client, HTTPError
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_functions as mf
from dotenv import load_dotenv
from time import sleep

load_dotenv()

API_EL_TOQUE = os.getenv('EL_TOQUE')

header = {
    "accept": "*/*",
    "Authorization": f"Bearer {API_EL_TOQUE}"
}

def toque(inicio: str,fin: str):
    fechas = mf.intervalo_fechas(inicio, fin, False, False)
    urls = mf.intervalo_fechas(inicio, fin)
    with Client() as client:
        for i in range(len(fechas)-1) :
          try:
            url = f'https://tasas.eltoque.com/v1/trmi?{urls[i]}'
            response = client.get(url=url, headers=header)
            response.raise_for_status()
            tasas = response.json()
            tasas_actuales = mf.read_json("el_toque.json")
            tasas_actuales[fechas[i]["date_from"]] = tasas["tasas"]
            mf.save_json( tasas_actuales,"el_toque.json")
            sleep(2)
          except HTTPError:
             return 'durmiendo por: ', fechas[i]["date_from"]
    return urls

if __name__ == "__main__":
    fecha_inicio = "2025-11-09"
    fecha_fin = "2025-11-11"
    toque(fecha_inicio, fecha_fin)
