#!/bin/bash

echo "Host: $(hostname)"
echo "Disk Usage: $(df -h / | tail -n1)"
echo -e "Memory Usage:\n$(free -h | head -n2)"
echo "Uptime: $(uptime -p)"
