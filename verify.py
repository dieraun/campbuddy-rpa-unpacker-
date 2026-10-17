import random2 as py27
py27.seed(3976940025)
v1 = py27.randint(0, 65535)
v2 = py27.randint(0, 65535)
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"r1 (v1 ^ 43690) = {v1 ^ 43690}")
print(f"r2 (v2 ^ 21845) = {v2 ^ 21845}")
key = (((v1 ^ 43690) << 16) | (v2 ^ 21845)) ^ 3067549256
print(f"正确密钥 = {key}")