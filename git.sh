commit="Commit: Update commits @ $(date)"
cd ~/Desktop/funfunfun/commit-bot/
echo "$commit" >> commits.md
echo "$commit"
echo

git add .
git commit -m "$commit"
git push origin master

exit 0
