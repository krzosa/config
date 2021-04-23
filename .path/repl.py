import sys
import subprocess

"""
python repl.py ${file}

This script runs the passed file either as a:
* test with pytest
* js test with npm test
* standalone python script
* and most importantly as a standalone module of a bigger project
"""

def module(path, modules):
    for i in modules:
        index = path.find(i)
        if index != -1:
            copy = path
            copy = copy.replace("/", ".")
            copy = copy[index:-3]
            return [True, copy, index]

    return [False, path, None]


		
def print_std(out):
    err = out.stderr.decode("utf-8")
    out = out.stdout.decode("utf-8")
    print(out, err)


if len(sys.argv) < 2:
    print("Pass an argument specyfying script you want to launch!")
    exit(0)

out = None
f = sys.argv[1].split("/")
file = f[-1]
print(file)


cwd = None
process_args = None
if file.startswith("test"):
    if file.endswith(".js"):
      cwd = "/".join(f[:-2])
      process_args = ["npm", "test", "--", sys.argv[1]]
    else:
      pytest = sys.executable[: sys.executable.index("/python")] + "/pytest"
      process_args = [pytest, "--no-cov", sys.argv[1]]
else:
    success, result, index = module(sys.argv[1], ["aries_cloudagent/", "services/"])
    if success:
      process_args = [sys.executable, "-m", result]
      cwd = sys.argv[1][:index]
    else:
      process_args = [sys.executable, result]

out = subprocess.run(process_args, cwd=cwd, capture_output=True)
print_std(out)

# process = subprocess.Popen(process_args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# for stdout_line in iter(process.stdout.readline, ""):
#   print(stdout_line.decode('utf-8'))
  
# print("END")

# for c in iter(lambda: process.stdout.read(1), b''):
#           sys.stdout.buffer.write(c)
#                   f.buffer.write(c)
# out = Popen(process_args, cwd=cwd, stdout=PIPE)
# queue = Queue()
# thread = Thread(target=enqueue_output, args=(out.stdout, queue))
# thread.deamon = True
# thread.start()

# try:  line = queue.get_nowait() # or q.get(timeout=.1)
# except Empty:
#   pass
# else:
#   print(line)
