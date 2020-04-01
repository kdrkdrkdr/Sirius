pyinstaller -y -F --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5 -i "./ms.ico" "Sirius.py" 

move dist/Sirius.exe ../

rmdir /s /q build __pycache__ 

del /s /q Sirius.spec

cd dist

move Sirius.exe ../Sirius.exe

cd ..

rmdir /s /q dist

exit