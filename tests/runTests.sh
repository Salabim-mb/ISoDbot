#!/bin/bash

mkdir accounts

printf "user1\nname1\npass1" >> accounts/user1.tst
printf "user2\nasdhjasfnmab\nasdjhsajkfhjaks" >> accounts/user2.tst
printf "user3\nasdhasjkdhas" >> accounts/user3.tst
printf "user4\n " >> accounts/user4.tst
printf "user5\n\nname5" >> accounts/user5.tst
printf "user5\n\nname5" >> accounts/boguszj.tst
printf "user5" >> accounts/polaczej.tst
printf "user5\n\nname5" >> accounts/balasm.tst

python runTests.py

rm -r accounts
 
