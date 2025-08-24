#!/bin/bash

if systemctl is-active --quiet ssh; then
	echo "SSH is running"
else
	echo "SSH is not running"
fi

AVAILABLE=$(df -h / | awk 'NR==2 {print $4}' | sed 's/G//')

if (( $(echo "AVAILABLE < 1" | bc -l) )); then
	echo "Warning: Disk space below 1GB!"
else
	echo "Disk space is sufficient: ${AVAILABLE}G"
fi
