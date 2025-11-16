' Datei, welche bei Doppelklick das gesamte Programm für die Gastransportwartungsanalyse startet

Dim shell
Set shell = CreateObject("WScript.Shell")

Dim fso, scriptDir, workingDir
Set fso = CreateObject("Scripting.FileSystemObject")

' Ordner des VBS-Skripts (Überordner)
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Unterordner "Code"
workingDir = scriptDir & "\Code"

' Pfad zur Miniconda Scripts/activate.bat
Dim condaActivate
condaActivate = """C:\ZusatzSW\Miniconda3\Scripts\activate.bat"""

' Befehl zusammenbauen
Dim cmd
cmd = "cmd /k ""cd /d " & workingDir & " && " & _
      "call " & condaActivate & " && " & _
      "(conda env list | findstr gastransportwartungsanalyse >nul || conda create -y -n gastransportwartungsanalyse python=3.10) && " & _
      "conda activate gastransportwartungsanalyse && " & _
      "pip install -r requirements.txt && " & _
      "python Main.py"""

shell.Run cmd, 1, True
