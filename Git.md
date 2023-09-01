## Store user-name and password(token) for future.
```git
git config --global credential.helper store
``` 

## How to remove or modify root commit in git?
For the most secure way is to use the `update-ref` command.
```git
git update-ref -d HEAD
```
It will delete the named reference `HEAD`, so it will reset(softly, you will not lose your work) all your commits of your current branch.

If what you want is to merge the first commit with the second one, you can use the `rebase` command.
```git
git rebase -i --root
```
And the other way could be create an orphan branch, a branch with the same content but without any commit history, and commit your new content on it.
```git
git checkout --orphan <new-branch-name>
```

