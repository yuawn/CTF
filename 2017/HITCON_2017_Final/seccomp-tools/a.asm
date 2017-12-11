A = arch
A = sys_number
A == read ? ok : next
A == write ? ok : next
A == open ? ok : next
return ERRNO(5)
ok:
return ALLOW
dead:
return KILL
