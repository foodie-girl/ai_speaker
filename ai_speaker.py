import os

while True:
    text = input("Type What you want me to speak : ")
    if text=="exit":
        command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'"Bye Bye Friend - See you later"\')"'
        os.system(command)
        break

    command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    os.system(command)