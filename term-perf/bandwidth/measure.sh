# timeout 32 sh -c 'cat /dev/urandom | base32 > junk.bin'
# timeout 8 sh -c 'cat junk.bin | tee junk.hyper'
# /usr/local/bin/gtimeout 8 sh -c 'cat ../junk.bin | /usr/local/bin/gtee junk.hyper'
wc junk.out
