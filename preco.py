print("=== MEU PC GAMER v3.0 - COMPLETO ===")
with open("lista.txt") as f:
    print(f.read())

print("\nDigite quanto você pagou em cada peça:")
ryzen = int(input("Ryzen 7 5700: R$ "))
placa = int(input("ASUS TUF A520: R$ "))
ram = int(input("RAM 16GB: R$ "))
ssd = int(input("SSD 500GB: R$ "))
gpu = int(input("Placa de Vídeo (ex: RX 580): R$ "))

total = ryzen + placa + ram + ssd + gpu

print(f"\n💰 TOTAL REAL COM GPU: R$ {total}")

# Salva num arquivo
with open("meu-orcamento.txt", "w") as f:
    f.write(f"Meu PC Gamer - Total: R$ {total}\n")
    f.write(f"Ryzen: {ryzen}, Placa: {placa}, RAM: {ram}, SSD: {ssd}, GPU: {gpu}\n")

print("✅ Orçamento salvo em meu-orcamento.txt!")

if total < 2000:
    print("Custo benefício INSANO!")
elif total < 3000:
    print("PCzão top, valeu cada centavo!")
else:
    print("MÁQUINA DE GUERRA!")
