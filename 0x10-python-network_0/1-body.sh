#!/bin/bash
# Get the response body for a given URL for 200 status code responses.

# -s = Silent mode. Don't show progress meter or error messages.
# -L = Redirects in URL#!/bin/bash
# This script sends a get request and also and displays the body of the response
response=$(curl -sI $1) && [[ "$response" == *"200 OK"* ]] && curl -s $1
