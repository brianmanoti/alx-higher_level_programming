#!/bin/bash

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

# Get the URL from the first argument
url=$1

# Send the request using curl and store the response in a variable
response=$(curl -sI "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -iE '^content-length:' | awk '{print $2}' | tr -d '\r')

# Check if the content length is available
if [ -z "$content_length" ]; then
  echo "Failed to get the content length for the URL: $url"
  exit 1
fi

echo "Size of the response body: $content_length bytes"
