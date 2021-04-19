import sys
import subprocess


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
if file.startswith("test"):
    if file.endswith(".js"):
        cwd = "/".join(f[:-2])
        out = subprocess.run(["npm", "test", "--", sys.argv[1]], cwd=cwd, capture_output=True)
    else:
        pytest = sys.executable[: sys.executable.index("/python")] + "/pytest"
        out = subprocess.run([pytest, "--no-cov", sys.argv[1]], capture_output=True)
else:
    success, result, index = module(sys.argv[1], ["aries_cloudagent/", "services/"])
    if success:
        out = subprocess.run(
            [sys.executable, "-m", result], capture_output=True, cwd=sys.argv[1][:index]
        )
    else:
        out = subprocess.run([sys.executable, result], capture_output=True)

print_std(out)
