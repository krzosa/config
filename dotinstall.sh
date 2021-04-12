git init --bare $HOME/.myconf
alias config='/usr/bin/git --git-dir=$HOME/.myconf/ --work-tree=$HOME'
config remote add origin https://github.com/krzosa/config.git
config fetch
config checkout main
config pull
