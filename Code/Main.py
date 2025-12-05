# Einstiegspunkt für die Gastransportwartungsanalyse
# DIE REIHENFOLGE DER 3 CODEBLÖCKE DARF NICHT VERÄNDERT WERDEN!

import sys
import os
import requests

# Schritt 1 von 3: Projektverzeichnis zum Python-Pfad hinzufügen (ermöglicht Modulimporte bei direktem Skriptaufruf)
projektordner = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Gastransportwartungsanalyse
if projektordner not in sys.path:
    sys.path.insert(0, projektordner)


# Schritt 2 von 3: Main definieren
def main():
    print("Hello world!")

    url = "https://transparency.entsog.eu/api/v1/operationalData.csv"

    params = {
        "limit": -1,
        "indicator": "Firm Available,Firm Technical,Firm Booked,Planned interruption of firm capacity,Planned interruption of interruptible capacity",
        "periodType": "day",
        "timezone": "CET",
        "dataset": 1,
        "from": "2025-12-01",
        "to": "2026-11-27",
        "pointDirection": (
            "AT-TSO-0003ITP-00040entry,"
            "AT-TSO-0003ITP-00040exit,"
            "DE-TSO-0005ITP-00188entry,"
            "DE-TSO-0009ITP-00126entry,"
            "DE-TSO-0009ITP-00525entry,"
            "NO-TSO-0001ITP-00208exit"
        ),
    }

    zertifikats_pfad = os.path.join(projektordner, "Einstellungen", "Zertifikat.crt")
    print(zertifikats_pfad)
    response = requests.get(
        url,
        params=params,
        verify=zertifikats_pfad)
    response.raise_for_status()  # Fehler werfen, falls Response nicht OK

    os.makedirs("Debug", exist_ok=True)
    with open("Debug/Rohdaten.csv", "wb") as f:
        f.write(response.content)


# Schritt 3 von 3: Das Programm ausführbar machen.
if __name__ == "__main__":
    main()