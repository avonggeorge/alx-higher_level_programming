#!/usr/bin/python3
# Deletes request passed as the first argument 

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response=$(curl -X DELETE -s -w "%{http_code}" -o response_body.txt $url)

if [ $? -ne 0 ]; then
    echo "Error: Failed to send DELETE request"
    exit 1
fi

http_code=$(tail -c 3 response_body.txt)
response_body=$(sed '$d' response_body.txt)

if [ $http_code -ne 200 ]; then
    echo "Error: DELETE request failed with HTTP status code $http_code"
    exit 1
fi

echo "Response body:"
echo "$response_body"

rm response_body.txt

