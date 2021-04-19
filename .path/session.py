#!/usr/bin/env python3

import subprocess
from subprocess import PIPE

_pane = ["-P", "-F", '#{pane_id}']

def run(args):
  process = subprocess.Popen(args, stdout=PIPE, stderr=PIPE)
  stdout, stderr = process.communicate()
  print("out", stdout, "err", stderr, "code", process.returncode)
  stdout = stdout.decode("utf-8")
  stderr = stderr.decode("utf-8")
  return stdout


def tmux(*cmd, t=None, get_pane=False):
  args = ['tmux']
  for key,val in enumerate(cmd):
    if key > 0:
      args+= ';'
    args+=val
  # print(args)
  if t:
    args = ["t", t]
  if get_pane:
    args = args + _pane

  result = run(args)
  if get_pane:
    result = result[:-1]
  return result

def attach(session):
	tmux(["a", "-t", session])

def select(pane):
  tmux(['select-pane', '-t', pane])

def bind(key, *cmd):
  bind_cmd = ['bind', key]
  tmux(bind_cmd, cmd)



session="se"
panes = []
panes.append(tmux(["new-session", "-s",  session, "-d"], get_pane=True))
compilation = tmux(["new-window", "-t", session], get_pane=True)
panes.append(tmux(['split-window', '-t', panes[0], '-h'], get_pane=True))
select(panes[0])
print(panes[1], panes[0])
tmux(["bind", "-n", "M-1", "sesnd-keys", "-t", compilation, "build.sh", "Enter"], ["swap-pane", "-t", panes[1], "-s", compilation], ['select-pane', '-t', panes[0]])
tmux(['bind', "-n", 'M-2', 'swap-pane', '-t', panes[1], '-s', compilation])
# tmux bind B swap-pane -t :1.2 -s $BUFF2# attach(session)
# tmux(["kill-session", "-t", session])

