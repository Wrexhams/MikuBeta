# convert.py
with open('MikuProjectReborn.lua', 'r', encoding='utf-8') as f:
    contents = f.read()

with open('MikuProjectReborn.lua', 'w', encoding='cp1251') as f:
    f.write(contents)

print("✓ Файл успешно конвертирован из UTF-8 в Windows-1251")
