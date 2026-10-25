import os

print("="*35)
print("   MONTADOR DE PC GAMER v4.0")
print("="*35)

# Mostra suas peças
with open("lista.txt") as f:
    pecas = f.read().splitlines()

precos = []
total = 0

print("\nSua config:")
for peca in pecas:
    valor = int(input(f"  {peca}: R$ "))
    precos.append(valor)
    total += valor

# GPU separado
gpu_valor = int(input("  Placa de Vídeo: R$ "))
total += gpu_valor

# Calculos extras
frete = 50
total_com_frete = total + frete
parcela_12x = total_com_frete / 12

print("\n" + "="*35)
print(f"💰 Subtotal peças: R$ {total}")
print(f"📦 + Frete: R$ {frete}")
print(f"🔥 TOTAL FINAL: R$ {total_com_frete}")
print(f"💳 12x de R$ {parcela_12x:.2f} sem juros")
print("="*35)

# Salva o recibo bonito
with open("recibo-final.txt", "w") as f:
    f.write("=== RECIBO PC GAMER ===\n")
    for i, peca in enumerate(pecas):
        f.write(f"{peca} - R$ {precos[i]}\n")
    f.write(f"GPU - R$ {gpu_valor}\n")
    f.write(f"Frete - R$ {frete}\n")
    f.write(f"TOTAL: R$ {total_com_frete}\n")
    f.write(f"12x R$ {parcela_12x:.2f}\n")

print("\n✅ Recibo salvo em recibo-final.txt")
print("Arquivos na pasta:")
os.system("ls -lh *.txt *.py")
