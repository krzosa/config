sh_var=$(tmux split-window -P -F "#{pane_id}")
tmux display -p -t %8 "a"
