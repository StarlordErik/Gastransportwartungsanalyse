# Einstiegspunkt für die Gastransportwartungsanalyse

import sys
import os

# Projektverzeichnis zum Python-Pfad hinzufügen (ermöglicht Modulimporte bei direktem Skriptaufruf)
projektordner = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Gastransportwartungsanalyse
if projektordner not in sys.path:
    sys.path.insert(0, projektordner)

def main():
    print("Hello world!")


if __name__ == "__main__":
    main()