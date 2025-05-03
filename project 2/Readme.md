# Working with changes

## Task #2

1. Look through the commit history of your project and pick three random commits. Look at the changes that were made in them.

2. Revert these changes with the git revert command one after another, so that you end up with three commits.

3. Try to undo these three commits:

- the last one — with the git reset --soft and git restore commands;

- the second to last one — with the git reset --mixed and git restore command;

- the first one — with the git reset --hard command.

## Solution

For the second task, we created a small Python project that contains a frontend — an html page.

The forms on this page allow the user to save their first name, last name, email, and phone number.

The project also contains backend files according to mvc and oop, and a configuration file that configures the work between the html page and the backend.

The gitignore file contains a list of files that should not be sent to Git.

Instead of a database, a JSON file on a remote server is used. The data entered by the user is committed and sent to the remote Git repository as pull requests. A separate branch is created for each commit, which should not merge with the main one when unloading data.

As a training exercise, it is suggested to perform actions with the received data, branches and commit history manually.

### Run the project in VSCode:

1. Open the project folder in VSCode.

Create and activate the virtual environment:

```Terminal
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

4. Go to the address in your browser:
   http://127.0.0.1:5000/

### Important

- To work correctly with Git, make sure that your project is initialized as a git repository and a remote repository is configured (git init, git remote add origin <url>).
- The server must have SSH or HTTPS access configured with pre-configured authorization.

### SSH auth

For automatic execution of Git commands to work correctly, make sure that:

SSH access to the remote repository is configured.

The SSH key is added to your GitHub/GitLab/Bitbucket account and is available for use.

On the first run, manually confirm the connection to the remote server to avoid an interactive prompt during automatic execution.

1. Example of checking the connection (run manually in the terminal):

```Terminal
ssh -T git@github.com
```

2. The command dir %USERPROFILE%\.ssh will list the existing keys. If there are none, create a new SSH key:

```Terminal
ssh-keygen -t ed25519 -C "your_email@example.com"
```

3. Add SSH key to SSH agent.

Start the SSH agent:

```Terminal
eval `ssh-agent -s`
```

Add the key to the agent:

```Terminal
ssh-add ~/.ssh/id_ed25519
```

4. Add your public SSH key to GitHub

5. Check your connection to GitHub via SSH

## Practice

So we have launched the project and now we will enter the user data in the browser. After confirmation, a window about successful execution will appear, and on the remote server a pull request with a new branch.

![pull-request](./img/pull-request.png)

After confirmation of the upload, you need to merge pull request.

![merge](./img/merge.png)

We got a new branch with user data.

![user-data](./img/user-data.png)

Let's upload the changes to the local repository:

```Terminal
git pull origin main
```

Our user-data.json file has been updated.

Let's add a few more users in the same way.

Great! We've added some users to our file and can now delete the branches we created earlier if we don't need them anymore.

We can also list the branches in the terminal with the command:

```Terminal
git branch
```

![branch](./img/branch.png)

Using the command "git log --oneline --graph --all" we can see all the branches and their commits in a graphical form.

![graph](./img/graph.png)

Using the "git diff branch-name" command we can see the specific changes that were made in a branch.

![diff](./img/diff.png)

Using the command "git diff main..user-7255098a" we can compare our main branch with the user branch.

![diff-main-user](./img/diff-main-user.png)

Let's look at all the commits and cancel the 3 ones of interest:

```Terminal
git log
```

![log](./img/log.png)

```Terminal
git revert ae5160429dfe6100002dcd0b203f0b8b495f04c8
git revert 783656f1123a7e812184fa947529a760b35a1815
git revert 412e8282d447d47938a788fedb751a5a30f828c1
git revert 669053f5c001343fcff3a793c8b11015634f284d
```

Or can use a range

```Terminal
git revert 669053f5c001343fcff3a793c8b11015634f284d..HEAD
```

We got an error because we are trying to undo a merge commit, but we did not specify which branch should be considered "master" when undoing.

To fix the situation, we specify the "-m" option and continue deleting using "git revert --continue".

> Attention! Be careful, if you make changes to other files during the work, these changes will also be deleted. In my case, the Readme.md file was rolled back and the images were deleted.

![undo](./img/undo.png)

Let's look at the contents of the userdata.json file and make sure that the data of the last two users with email addresses test4@test and test3@test have been deleted.
