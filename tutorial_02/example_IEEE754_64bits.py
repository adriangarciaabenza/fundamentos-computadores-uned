import struct

x = 0.1

# Convertimos el float a sus 64 bits
bits = struct.unpack(">Q", struct.pack(">d", x))[0]
b = f"{bits:064b}"

signo = b[0]
exponente = b[1:12]
fraccion = b[12:]

print(f"{signo} | {exponente} | {fraccion}")
print("↑        ↑                         ↑")
print("signo  exponente                fracción")

#---------------------------------------------------------------
import struct

x = 0.1

bits = struct.unpack(">Q", struct.pack(">d", x))[0]
b = f"{bits:064b}"

signo_bit = b[0]
exp_bits = b[1:12]
frac_bits = b[12:]

s = int(signo_bit, 2)
E = int(exp_bits, 2)
e = E - 1023

# Fracción como valor decimal
fraccion = sum(
    int(bit) * 2**(-(i + 1))
    for i, bit in enumerate(frac_bits)
)

significando = 1 + fraccion

valor = (-1)**s * significando * 2**e

print("IEEE 754:")
print(f"{signo_bit} | {exp_bits} | {frac_bits}")

print("\nCampos:")
print(f"Signo:")
print(f"  bit = {signo_bit}")
print(f"  (-1)^s = {(-1)**s}")

print(f"\nExponente:")
print(f"  binario = {exp_bits}")
print(f"  almacenado E = {E}")
print(f"  exponente real e = {E} - 1023 = {e}")

print(f"\nFracción:")
print(f"  binario = 0.{frac_bits}")
print(f"  decimal ≈ {fraccion:.17f}")

print(f"\nSignificando:")
print(f"  1 + fracción = {significando:.17f}")

print("\nReconstrucción:")
print(f"  x = (-1)^{s} × {significando:.17f} × 2^{e}")
print(f"  x = {valor:.17f}")