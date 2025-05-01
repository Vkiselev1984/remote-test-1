# remote-test-1

Testing work with Git
##Task

1. Choose a project in the programming language you are learning that you will practice working with in Git, and initialize a local repository in the folder of this project.

2. Create a non-empty remote repository (for example, with a README.md file) with a name that matches the name of this project.

3. Connect your project to this remote repository and push the code of this project to it. Resolve any conflicts and problems yourself if they arise during this task.

## Solution

### We created and initialized a local repository by adding the mine.py file to it:
1. Opened and created a folder in the VScode:
```Terminal
mkdir remote-test-1
cd remote-test-1
git init
```
2. Added file with code:
```Py
print("Hello, World!")
```
3. Added the file to the index and made a commit:
```Terminal
git add main.py
git commit -m "Initial commit"
```
### We have created a remote repository remote-test-1 in the web interface Git

### Added a remote repository in the terminal and sent the code to the remote repository in the master branch:
```Terminal
https://github.com/Vkiselev1984/remote-test-1.git
git push -u origin master
```
### Updated a file in the remote repository in the web interface and received changes in the terminal from the main branch:
```Terminal
git pull origin main
```
### Since the branches are not related by a common history, we got an error: fatal: refusing to merge unrelated histories

### Used the --allow-unrelated-histories option when running the git pull command
1. Switched to the main branch
```Terminal
git checkout main
```
2. Updated the local main branch, resolving unrelated stories by first updating the Readme file and adding tasks to it
```Terminal
git pull origin main --allow-unrelated-histories
```
### Now the file is loaded and we have merged the two branches:
```Terminal
git merge master
```
### Pushed changes to remote repository
```Terminal
git add .
git commit -m "Resolved merge conflicts"
git push origin main
```
