#!/bin/bash
curl -X BREW http://brew.p.tjctf.org/flag -d "start" --header "Content-Type: message/teapot" --header "Accept-Additions: sugar"
sleep 60
curl -X BREW http://brew.p.tjctf.org/flag -d "stop" --header "Content-Type: message/teapot" --header "Accept-Additions: sugar" > flag.txt

