
# Calculadora de Média

Uma simples calculadora de média de notas finais trimestrais


## Build para .EXE

Para transformar o arquivo em .EXE baixe o pyinstaller

```bash
  pip install pyinstaller
```
Depois disso é só rodar este comando para transformar em .EXE

```bash
  pyinstaller --onefile --windowed --clean --icon=cosin.ico --add-data "cosin.ico;." app.py

```
