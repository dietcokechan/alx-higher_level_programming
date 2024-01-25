#!/bin/bash
# curl only methods
curl -sI OPTIONS "$1" | grep -i Allow | cut -d ' ' -f2-
