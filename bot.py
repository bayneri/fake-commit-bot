import subprocess
import random

rand = random.randint(0,10)

if rand > 5:
    # my little tiny miny fake github activity
    subprocess.Popen(["bash", "./git.sh"])
