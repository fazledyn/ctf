## Instructions

- Extract public key from the certificate
```sh
openssl x509 -pubkey -noout -in cert > key.pub
```
- Extract the numbers from the text format
```sh
openssl rsa -pubin -in key.pub -text 
```
- Get the modulus, goto factordb.com to factor the number.
- Submit it as picoCTF{p,q}
