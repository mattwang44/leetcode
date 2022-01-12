#!/bin/bash
for file in "leetcode/**/*.go" ; do 
    [ "$(sed -n '/^package main/p;q' $file)" ] || \
    ((echo "package main" | cat - $file) > temp && mv temp $file) 
done

gofmt -s -w .
