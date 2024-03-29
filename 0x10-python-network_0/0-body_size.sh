#!/bin/bash
# This script fetches the content length of a request made
curl -s "$1" | wc -c

