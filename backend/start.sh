#!/bin/bash

tmux new -s kicker -d
tmux send-keys -t kicker 'python3 /home/pi/kicker/backend/app.py' C-m
tmux new-window -n ws -t kicker
tmux send-keys -t kicker:1 'python3 /home/pi/kicker/backend/websockets/event_bus.py' C-m
tmux new-window -n ws -t kicker
tmux send-keys -t kicker:1 'python3 /home/pi/kicker/backend/websockets/state_bus.py' C-m
