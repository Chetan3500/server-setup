#!/bin/bash

COUNT=0
for file in /var/log/*.log; do
    echo "File $file, Size: $(ls -lh "$file" | awk '{print $5}')"
    ((COUNT++))
done
echo "Total log files: $COUNT"
