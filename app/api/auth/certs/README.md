```shell
# Generate an RSA private key, of size 2048
[ ! -f jwt-private.pem ] && openssl genrsa -out jwt-private.pem 2048
```

```shell
# Extract the public key from the key pair, which can be used in a certificate
[ ! -f jwt-public.pem ] && openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```