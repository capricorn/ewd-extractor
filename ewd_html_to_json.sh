#!/bin/bash

output=$(
    for fn in ewd-index-html/*.html; do 
        cd ewd_extractor; 
        poetry run python -m ewd_extractor.main "../$fn"; 
        cd ..; 
    done)

echo $output | jq -s '{ entries: add }'