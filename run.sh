#!/bin/bash
echo "tsa check" | openssl ts -query -no_nonce -sha1 2>/dev/null | curl -s -S -H 'Content-Type: application/timestamp-query' --data-binary @- http://tsp.pki.mts.ru/tsp/ -o response.tsr
python3 sndzb.py "`openssl ts -reply -text -in response.tsr 2>/dev/null | grep Time`"
