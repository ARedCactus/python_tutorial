# 计算R1  
L0_bytes = bytes.fromhex('3E2A5782')  
F_output_bytes = bytes.fromhex('2163A59D')  
R1_bytes = bytes([a ^ b for a, b in zip(L0_bytes, F_output_bytes)])  
R1_hex = R1_bytes.hex().upper()  
  
# L1直接等于R0  
R0_bytes = bytes.fromhex('346EC825')  
L1_hex = R0_bytes.hex().upper()  
  
print(f"L1 = {L1_hex}")  # 输出L1  
print(f"R1 = {R1_hex}")  # 输出R1