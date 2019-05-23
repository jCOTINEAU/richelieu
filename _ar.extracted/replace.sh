#!/bin/bash

sed -i 's/cd/b5/g' prime.txt
sed -i 's/57/a4/g' prime.txt

sed -i 's/54/16/g' prime.txt

sed -i 's/12/f4/g' prime.txt

sed -i 's/66/e1/g' prime.txt


sed -i 's/fb/7f/g' prime.txt

#1342  sed -i 's/7f/fb/g' prime.txt
# 1343  sed -i 's/e1/66/g' prime.txt
# 1344  sed -i 's/f4/12/g' prime.txt
# 1345  sed -i 's/16/54/g' prime.txt
# 1346  sed -i 's/a4/57/g' prime.txt
# 1347  sed -i 's/b5/cd/g' prime.txt
# 1348  openssl rsautl -encrypt -pubin -inkey public.key -in motDePasseGPG.txt -out motDePasseGPG.txt.enc
