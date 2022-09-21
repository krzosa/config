Install:

```
git init --bare $HOME/.myconf
alias config='/usr/bin/git --git-dir=$HOME/.myconf/ --work-tree=$HOME'
config remote add origin https://github.com/krzosa/config.git
config fetch
config checkout main
```

sh_var=$(tmux split-window -P -F "#{pane_id}")
tmux display -p -t %8 "a"
