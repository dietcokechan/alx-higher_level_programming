#!/bin/bash
# curl only methods
curl -i -L -X OPTIONS "$1" | grep -i Allow | cut -d ' ' -f2-
