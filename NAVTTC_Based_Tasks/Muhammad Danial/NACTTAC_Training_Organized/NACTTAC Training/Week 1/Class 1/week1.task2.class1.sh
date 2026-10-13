# PDF class alignment: Linux shell fundamentals
# Topics: pwd, cd, ls, cat, man, redirection, mkdir/rm/cp/mv, file reading, touch/nano, bash/sh, chmod, ps/kill, package management, environment variables.
# Original task implementation retained below.

# NAVTTC AI/ML Course — Task 2: Linux command practice
# Source/topic: NAVTTC PDF, Annexure-I, Task 2

#!/usr/bin/env bash
# Task 2 — Linux/Debian command practice.
# Run individual commands in a Linux terminal. This script demonstrates safe commands.
set -e
echo "Current directory:"; pwd
echo "Home directory contents:"; ls -la "$HOME"
echo "Create a practice folder:"
mkdir -p "$HOME/navttc_practice"
cd "$HOME/navttc_practice"
printf "Hello from Linux\n" > sample.txt
cat sample.txt
head -n 1 sample.txt
cp sample.txt copy.txt
mv copy.txt renamed.txt
file sample.txt
echo "Files:"; ls -l
# Useful commands to practice manually:
# cd, less, more, man ls, touch newfile.txt, nano newfile.txt,
# mkdir folder, rmdir empty_folder, rm file, chmod +x script.sh,
# ps, kill PID, sudo apt update, sudo apt upgrade, dpkg -l
# Be careful: rm deletes files; sudo runs commands with elevated privileges.
