#!/bin/bash
echo "tsa check" | openssl ts -query -no_nonce -sha1 2>/dev/null | curl -s -S -H 'Content-Type: application/timestamp-query' --data-binary @- http://tsa.example.com/ -o response.tsr
python3 /usr/share/tsacheck/sndzb.py "`openssl ts -reply -text -in response.tsr 2>/dev/null | grep -oPi \"(?<=Time stamp: ).*\"`"
