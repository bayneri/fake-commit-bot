import subprocess
import random

rand = random.randint(0,10)
print('----------------')
print(rand)

if rand > 5:
    # my little tiny miny fake github activity
    subprocess.Popen(["bash", "/Users/halil/Desktop/funfunfun/fake-commit-bot/git.sh"])
else:
    print('unlucky')
