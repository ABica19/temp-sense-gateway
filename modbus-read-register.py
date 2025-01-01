from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime
import json
import time


# Funktion um die aktuelle uhrzeit zu finden.
def current_time():
    now = datetime.now().isoformat()
    return now


host = ''  # IP-Adresse von dem Gateway wird in diesem Variable gespeichert
port = 502  # Default port Modbus TCP
client = ModbusTcpClient(host, port)

while True:
    client.connect()
    # Liest den Wert von einem holding register in der Adresse 1000 # 1000 ist in diesem fall ein beispiel
    rr = client.read_holding_registers(1000, 1, unit=1)

    data = {
        "datetime": current_time(), # Aufruf der Methode current_time()
        "data": rr.registers  # Daten von Register anzeigen
    }

    # Daten in json-Format anzeigen
    print(json.dumps(data))

    # Nach 5 Minuten Wartezeit , werden das Lesen anfangen.
    time.sleep(5)
