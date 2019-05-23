#!/bin/bash
#openssl rsa -pubin -in /tmp/public.key -text -noout


openssl asn1parse -genconf privkey.asn -out private.der
openssl rsa -inform DER -outform PEM -in private.der -out private.pem
openssl rsautl -decrypt -inkey private.pem -in motDePasseGPG.txt.enc -out success
