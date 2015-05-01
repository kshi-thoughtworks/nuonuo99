#!/usr/bin/expect -f

# root/S801220k
set timeout 60
set passwd "S801220k"

spawn ssh root@123.57.142.206
expect {
    #"yes/no" {send "yes\r"; exp_continue}
    "password:" {send "$passwd\n"}
}
interact
