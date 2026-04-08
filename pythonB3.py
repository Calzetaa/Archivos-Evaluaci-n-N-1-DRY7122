print("VALIDADOR DE ACL (Access Control List)")

acl_numero = int(input("\nIngrese el número de ACL IPv4: "))

print("\n" + "=" * 70)
print("RESULTADO")
print("=" * 70)

if acl_numero == 0:
    print(f"✗ El número {acl_numero} no es válido")
    print("  El número 0 no corresponde a ninguna ACL")

elif (1 <= acl_numero <= 99) or (1300 <= acl_numero <= 1999):
    print(f"✓ El número {acl_numero} es una ACL ESTÁNDAR")
    print("  Rango válido: 1-99 ó 1300-1999")

elif (100 <= acl_numero <= 199) or (2000 <= acl_numero <= 2699):
    print(f"✓ El número {acl_numero} es una ACL EXTENDIDA")
    print("  Rango válido: 100-199 ó 2000-2699")

elif acl_numero > 2699:
    print(f"✗ El número {acl_numero} no es válido")
    print("  El número excede el rango máximo permitido para ACL (2699)")

else:
    print(f"✗ El número {acl_numero} NO corresponde a una lista de acceso")
    print("  Rangos válidos:")
    print("  - ACL Estándar: 1-99 ó 1300-1999")
    print("  - ACL Extendida: 100-199 ó 2000-2699")

