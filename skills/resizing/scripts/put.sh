#!/bin/bash
# put.sh <work dir> <id> '<upload_url>'   PUTs src/<id>.png to the presigned Creatify URL from upload_file. Prints "<id> 200".
cd "$1" && curl -s -o /dev/null -w "$2 %{http_code}\n" -X PUT -H "Content-Type: image/png" --data-binary @src/$2.png "$3"
