#!/bin/bash
# 1337  gpg -o lsb_RGB.png.enc --symmetric lsb_RGB.png
# 1338  vim motDePasseGPG.txt

# 1339  openssl genrsa -out priv.key 4096
# 1340  openssl rsa -pubout -out public.key -in priv.key
# 1341  openssl rsa -noout -text -in priv.key | grep prime1 -A 18 > prime.txt
sed -i 's/7f/fb/g' prime.txt
sed -i 's/e1/66/g' prime.txt
sed -i 's/f4/12/g' prime.txt
sed -i 's/16/54/g' prime.txt
sed -i 's/a4/57/g' prime.txt
sed -i 's/b5/cd/g' prime.txt
# 1348  openssl rsautl -encrypt -pubin -inkey public.key -in motDePasseGPG.txt -out motDePasseGPG.txt.enc
