#!/usr/bin/python3
import os, tempfile, subprocess

try:
    data = input("ELF>").strip()
    data = bytes.fromhex(data)
    if len(data) > 45: raise Exception("too large")
    if data[:4] != b"\x7fELF": raise Exception("not an ELF file")

    with tempfile.TemporaryDirectory() as dirname:
        name = os.path.join(dirname, "user.elf")
        with open(name, "wb") as f: f.write(data)
        os.chmod(name, 0o500)
        print(subprocess.check_output(name))

except Exception as e:
    print("FAIL:", e)
    exit(1)
