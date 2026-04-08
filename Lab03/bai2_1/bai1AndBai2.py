p = int(input("p = "), 0)
q = int(input("q = "), 0)
e = int(input("e = "), 0)
M = int(input("M = "), 0)

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)


# Confidentiality
C_conf = pow(M, e, n)
M_decrypt = pow(C_conf, d, n)

# Authentication
C_auth = pow(M, d, n)
M_verify = pow(C_auth, e, n)


print("\n=== DEC ===")
print("n = ", n)
print("phi = ", phi)
print("e = ", e)
print("d = ", d)
print("PU = {" + str(e) + ", " + str(n) + "}")
print("PR = {" + str(d) + ", " + str(n) + "}")

print("\n--- CONFIDENTIALITY ---")
print("C =", C_conf)
print("M =", M_decrypt)
print("--- AUTHENTICATION ---")
print("S =", C_auth)
print("M =", M_verify)

print("\n=== HEX ===")
print("n = ", hex(n))
print("phi = ", hex(phi))
print("e = ", hex(e))
print("d = ", hex(d))
print("PU = {" + str(hex(e)) + ", " + str(hex(n)) + "}")
print("PR = {" + str(hex(d)) + ", " + str(hex(n)) + "}")

print("\n--- CONFIDENTIALITY ---")
print("C =", hex(C_conf))
print("M =", hex(M_decrypt))
print("--- AUTHENTICATION ---")
print("S =", hex(C_auth))
print("M =", hex(M_verify))