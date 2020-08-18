#!/bin/bash
# JSON file POST
curl -sH "Content-Type: application/json" -d @"$2" "$1"
