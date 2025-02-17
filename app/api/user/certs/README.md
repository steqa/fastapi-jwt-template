```shell
# Generate a 32-byte random secret key encoded in base64
[ ! -f secret.key ] && openssl rand -base64 32 > secret.key
```