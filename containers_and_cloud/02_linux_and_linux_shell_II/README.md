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

| Command | Effect |
|---------|--------|
| `chown alice file` | Change owner to 'alice' |
| `chown alice: file` | Change owner to 'alice' and group to alice's login group |
| `chown :developers file` | Change group to 'developers' |
| `chown alice:developers file` | Change owner to 'alice' and group to 'developers' |
| `chown 1001:1002 file` | Change owner to UID 1001 and group to GID 1002 |
| `chown --from=alice bob file.txt` | Change owner only if current owner is 'alice' |
| `chown --from=old_owner:old_group new_owner:new_group file-or-dir` | only change files that currently have a specific owner and/or group (either can be omitted) |

