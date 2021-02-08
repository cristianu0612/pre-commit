#!/bin/bash

MSG="$1"

if ! grep -qE "updated" "$MSG";then
    cat "$MSG"
    echo "Your commit message must contain the word 'updated'"
    exit 1
fi
