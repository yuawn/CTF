Seccomp Tools
====

Where Is The Service
--------------------
nc 10.0.<TN>.1 9487

Which File Should Be Patched
----------------------------
`seccomp-tools`

Where Is The Flag
-----------------
`/home/seccomp-tools/flag`

How We Run This Service
-----------------------
`nsjail --config seccomp-tools.cfg` that launched by xinetd.
