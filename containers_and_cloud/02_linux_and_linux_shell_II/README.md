# Linux and Linux Shell

## 👥 Users and Groups

📄 Users file: `/etc/passwd`

📄 Groups file: `/etc/group`

🔒 `/etc/shadow` - Stores encrypted passwords and password policies. Readable only by root.

- 👑 **Root User (Superuser)**:
  
  - User ID (UID): 0
  
  - The administrative account with unlimited, unrestricted power over the entire system.

- 🤖 **System Users (Service Accounts)**:
  
  - UID Range: 1-999 (on most modern systems)
  
  - Non-login accounts created during software installation to run system services.
  
  - If a service is compromised, the damage is contained to that system user's privileges.

- 🛠️ **Common commands**:

    - `adduser` or `useradd`
    
    - `passwd` - Set or change a user's password
    
    - `deluser`
    
    - `usermod` - Modify user account details. Used with options
    
    - `groupadd` - Create a new group
    
    - `groupdel`
    
    - `gpasswd` - Manage group passwords
    
    - `groups` - List groups a user belongs to
  
- Users must have a primary group, specified in `/etc/passwd`
  
- They may have supplementary groups, listed in `/etc/group`

## 🔐 Access Rights

![AccessRights](https://github.com/vanya-koleva/softuni_courses/blob/main/containers_and_cloud/02_linux_and_linux_shell_II/file_permissions.jpg)

| Symbol | Meaning       | Value |
| ------ | ------------- | ----- |
| `r`    | Read          | 4     |
| `w`    | Write         | 2     |
| `x`    | Execute       | 1     |
| `-`    | No permission | 0     |

- Add the values to get the octal digit for each category.
  
  - Example: `rwxr-xr--` becomes:

    👤 Owner: `rwx` = 4+2+1 = 7

    👥 Group: `r-x` = 4+0+1 = 5

    🌍 Others: `r--` = 4+0+0 = 4

    Thus, the octal mask is `754`.

  
### 🛠️ `chmod`

- Change the permissions of a file or directory for all types of users

- 💡 To execute a script the user must also have read permission (interpreter must read the code).

- **Octal mode**:
    
  - `chmod 600 file` - Only the owner can read and write
  
  - `chmod 700 private_dir` - Only the owner can read, write, and access the directory
    
  - `chmod -R 755 /path/to/folder` - Apply changes to all files and subdirectories.

- **Symbolic mode**:

```bash
chmod [who][operator][permission] file
```

| Operator | Meaning              |
| -------- | -------------------- |
| `+`      | Add permission       |
| `-`      | Remove permission    |
| `=`      | Set exact permission |

```bash
chmod u+x script.sh     # Add execute permission to the user
chmod g-w file.txt      # Remove write permission from group
chmod o=r file.txt      # Others can only read
chmod a+r file.txt      # Everyone can read (a = all)

chmod +x script.sh      # The '+' defaults to 'a' (all)
```

### 🛠️ `chown`

- Change file owner and/or group.

- Regular users can only change **the group** of a file they own, to a group they are a member of. Cannot change the file’s owner to another user.

- Can take `-R` for recursive changes to the files and subdirectories.

- `chgrp [options] group file` is usually used when changing only group

```bash
chown [options] [owner][:[group]] file
```

| Command | Effect |
|---------|--------|
| `chown alice file` | Change owner to 'alice' |
| `chown alice: file` | Change owner to 'alice' and group to alice's login group |
| `chown :developers file` | Change group to 'developers' |
| `chown alice:developers file` | Change owner to 'alice' and group to 'developers' |
| `chown 1001:1002 file` | Change owner to UID 1001 and group to GID 1002 |
| `chown --from=alice bob file.txt` | Change owner only if current owner is 'alice' |
| `chown --from=old_owner:old_group new_owner:new_group file-or-dir` | only change files that currently have a specific owner and/or group (either can be omitted) |

## 🌍 Environment Variables

- ⚙️ Provide config settings to Linux apps

- Exported variables are available to child processes

- Names use `CAPITAL_LETTERS` by convention

- No spaces: `VAR=value`

- Case-sensitive

- 🛠️ **Commands**:

    - List all environment variables:
    
    ```bash
    env
    printenv
    ``` 

    - Print a single environment variable:

    ```bash
    printenv HOME
    echo $HOME
    ```

    - Set a new environment variable. Changes in current session only (use config files for permanence):

    ```bash
    export VAR=VALUE
    ```

    - Unset variable:

    ```bash
    unset VARIABLE_NAME
    ```

- Examples:

```bash
export PATH=$PATH:/my/custom/bin
export EDITOR=vim                
unset TMP_VAR                    
```

## SSH (Secure Shell)

- Allows connecting to a remote machine's console

```bash
ssh [options] [user@]hostname

ssh hostname -l user
```
- `ssh` - invokes the SSH client program

- `192.168.0.28` - IP address (or hostname) of the remote machine

- `-l root` - specifies the login name (in this case, the root user)

## Processes and Jobs

-   **All Jobs are Processes**, but not all Processes are Jobs.

-   A **Process** is the OS's view of a running program.

-   A **Job** is the Shell's view of a process or pipeline that *it is managing*.

| Feature | Process | Job |
| :--- | :--- | :--- |
| **Manager** | Linux Kernel | Shell (Bash, Zsh, etc.) |
| **Identifier** | Process ID (PID) | Job ID (JID) e.g., `[1]` |
| **Scope** | System-wide | Local to a specific shell session |
| **Grouping** | A single unit of execution | Can be a single process or a pipeline |
| **Control** | Kernel scheduler, signals (`kill`) | Shell built-ins (`fg`, `bg`, `jobs`) |
| **Lifetime** | Can outlive the parent shell (daemon) | Typically dies when the parent shell exits |

- **Examples of Processes:**
  
  - The `ls` command
  
  - Firefox browser (firefox)

- **Examples of Jobs:**

  - Starting `vim` to edit a file. It's a process, but the shell sees it as a job and gives it control of the terminal (a **foreground job**).
  
  - Starting `sleep 1000 &`. The `&` puts it in the background. The shell reports: `[1] 12345`. Here, `[1]` is the Job ID and `12345` is the PID.
  
  - A command pipeline: `find / -name "*.conf" 2>/dev/null | head -n 20 &`. The entire `find | head` pipeline is one job.

### Commands

- List jobs:

```bash
jobs [options] [jobspec]
```

- List processes:

```bash
ps
top
htop
```

- Kill a job or process: 

```bash
kill [options] pid | jobspec
```

- Run command in background

```bash
command &
```

- Suspend current job - `CTRL + Z`

## More Linux Commands

- `wget` - A free utility for non-interactive download of files from the Web

```bash
wget [options] URL
```

- `curl` - A tool for transferring data from or to a server

```bash
curl [options] URL
```
