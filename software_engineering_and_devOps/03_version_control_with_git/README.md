# Version Control with Git

-   Git - Global Information Tracker

## Basic Git Commands

-   `git clone [remote url]`

-   `git pull` - Fetch and merge the latest changes from the remote repository

-   `git add [filename]`  
    `git add .` - add everything

-   `git commit –m "[your message here]"`

-   `git status`

-   `git init` - Create a new local repository (in the current directory)

-   `git remote add [remote name] [remote url]` - Create a remote (assign a short name for remote Git URL)

-   `git push [remote name] [local name]`

## Branching

-   Local branch - Branch in your local Git repo

-   Remote branch - Branch inside the remote repository

-   Upstream branch - the remote branch linked to your local branch, receiving changes when you push.

---

-   **Create** a new local branch

    -   `git branch [branch-name]`

-   **Create** a new branch and **switch** to it

    -   `git checkout -b [branch-name]`

-   **Switch** to an existing branch:

    -   `git switch [branch-name]`

    -   `git checkout [branch-name]`

-   **List** local branches

    -   `git branch`

-   **List** all local and remote branches:

    -   `git branch --all`

    -   `git branch -a`

-   **List** local together with the last commit message

    -   `git branch --verbose`

    -   `git branch -vv`

-   **List** all local and remote branches with the last commit message

    -   `git branch --all --verbose`

    -   `git branch –a -vv`

-   **Push to a new upstream** (in a new remote branch)

    -   `git push --set-upstream origin [branch-name]`

    -   `git push -u origin [branch-name]`

-   **Merge** another branch in the active branch

    -   `git merge [branch-name]`

-   **Delete** a **local** branch

    -   `git branch -d [branch-name]`

-   **Delete** a **remote** branch

    -   `git push origin -d [branch-name]`

