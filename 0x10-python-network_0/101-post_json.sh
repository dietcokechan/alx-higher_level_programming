#!/bin/bash
# curl a json file
curl -s "$1" POST -H "Content-Type: application/json" -d "$(cat "$2")"
