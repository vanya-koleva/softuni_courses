# Linux and Linux Shell

## Common Commands

- `whoami` - Display the currently logged-in user

- `uname -a` - Display OS information

- `mkdir directory`
  
  - `mkdir dir1 dir2 dir3` - Creates three directories at one

  - `-p` - Create parent directories as needed (no error if they exist) ex.: `mkdir -p projects/2025/code`

  - `-v` - Show confirmation message

- `cp source destination`
  
  - `cp file1.txt file2.txt` - creates a new file named file2.txt with the same content.

  - `cp file1.txt /home/user/Documents/` - copy a file to a directory

  - `cp -r project/ backup/` - copy the whole project folder into backup (recursive)

- `mv source dest`

- `rm file or dir`

### `top` - Display all active processes
  
  - PID - Process ID
  - PR - Priority
  - NI - Nice value (affects priority)
  - VIRT - Virtual memory used
  - RES - Resident (RAM) memory used
  - SHR - Shared memory
  - S - Process state (R=Running, S=Sleeping, Z=Zombie, etc.)

#### Interactive Commands Inside `top`:

| Key           | Action                                                              |
| ------------- | ------------------------------------------------------------------- |
| **q**         | Quit `top`                                                          |
| **h**         | Help                                                                |
| **k**         | Kill a process (you’ll be prompted for PID)                         |
| **r**         | Renice (change priority) of a process                               |
| **P**         | Sort by CPU usage (default)                                         |
| **M**         | Sort by memory usage                                                |
| **T**         | Sort by time                                                        |
| **1**         | Show CPU usage per core                                             |
| **Shift + E** | Change memory unit (KB/MB/GB)                                       |
| **Shift + R** | Reverse sort order                                                  |
| **Space**     | Refresh immediately (otherwise it auto-refreshes every few seconds) |

#### Customizations

- `top -d 2` - Set refresh interval; updates every 2 seconds

- `top -u username` - Show only processes of a specific user

- `top -b -n 1 > top_output.txt` - Batch mode (for logging or scripts) - `-b` = batch mode, `-n 1` = one iteration

- `top -d 2 -n 5` - Display all processes with 2 sec delay 5 times

### `ls` - List files and directories

#### Common Options

| Option         | Description                                       | Example           |
| -------------- | ------------------------------------------------- | ----------------- |
| `-l`           | Long listing format (shows details)               | `ls -l`           |
| `-a`           | Include hidden files (starting with `.`)          | `ls -a`           |
| `-A`           | Include hidden files (excluding `.` and `..`)          | `ls -A`           |
| `-h`           | Human-readable file sizes (works with `-l`)       | `ls -lh`          |
| `-t`           | Sort by modification time (newest first)          | `ls -lt`          |
| `-r`           | Reverse order                                     | `ls -ltr`         |
| `-S`           | Sort by file size (largest first)                 | `ls -lS`          |
| `-R`           | Recursive listing (include subdirectories)        | `ls -R`           |
| `-d` | Display directory name only (with a pattern) | `ls -d */` |

- `ls -d */` - List only directories

- `ls -d .*/ ` - List only hidden directories

- `ls -p | grep -v /`  - List only files (exclude directories)
  
  - `ls -p` -  adds `/` after directories
  
  - `grep -v /` removes anything containing `/`, leaving only files
  
- `ls -pA | grep -v /` - Include hidden files

#### `ls -la` - Lists everything in the directory with detailed info

- Example output:

```
drwxr-xr-x  3 user user 4096 Oct 30 10:30 .
drwxr-xr-x 18 user user 4096 Oct 30 09:00 ..
-rw-r--r--  1 user user  512 Oct 29 15:12 notes.txt
drwxr-xr-x  2 user user 4096 Oct 29 12:45 Documents
lrwxrwxrwx  1 user user   11 Oct 30 10:00 shortcut -> /usr/bin/vim
crw-rw----  1 root tty  136, 1 Oct 30 08:00 tty1
```
**Columns:**

| Column  | Description                     |
| ------- | ------------------------------- |
| **1**   | File type (first char) and permissions (next **9** chars)      |
| **2**   | Number of hard links            |
| **3**   | Owner (user)                    |
| **4**   | Group                           |
| **5**   | File size (in bytes)            |
| **6–8** | Last modification date and time |
| **9**   | File or directory name          |

## File Types

- `-` - **Regular file**
  
- `d` - **Directory**

- `l` - **Symbolic link**: A shortcut or pointer to another file

- `b` - **Block**: Hardware devices that transfer data in blocks (e.g., hard drives, USB drives)

- `c` - **Character**: Hardware devices that transfer data character by character (e.g., keyboard, serial ports)

- `p` - **FIFO pipe**: Special file for inter-process communication

- `s` - **Local socket**: Special file used for network or inter-process communication

## Linux Directory Structure

- Often referred to as the **Filesystem Hierarchy Standard (FHS)**

- Syntax: `ls /`

- **`/bin` - User Binaries**
  
  - Basic user commands
  
  - Available to everyone and required for the system to boot or operate in minimal mode.
  
  - ex.: `ls`, `cp`, `mv`

- **`/sbin` - System Binaries**
  
  - System admin commands
  
  - Used by the superuser (root)
  
  - ex.: `reboot`, `fsck` (check/repair filesystems)

- **`/etc ` - Configuration Files**
  
  - “Editable Text Configuration”
  
  - Contains system-wide configuration files and scripts.
  
  - Keeps all the settings.
  
  - ex.: `passwd`, `ssh/`

- **`/dev` - Device Files**
  
  - Contains special files that represent hardware devices.
  
  - These are not real files — they act as interfaces to hardware (like drives, USBs, keyboards, etc.).
  
  - Linux treats everything as a file — even devices.
  
  - ex.: `sda` (hard drive partition), `tty` (terminal device)

- **`/proc` - Process Information**
  
  - What the kernel is doing right now.
  
  - Files inside `/proc` are generated dynamically by the kernel — not stored on disk.
  
  - ex.: `cpuinfo`, `meminfo`

- **`/boot` - Boot Loader Files**
  
  - Files needed to boot the Linux system — kernel and bootloader configs.

- **`/var` - Variable Files**
  
  - Files that change frequently — logs, mail, spool files, caches, etc.

- **`/tmp` - Temporary Files**
  
  - Stores temporary files created by applications or users.
  
  - Automatically cleared on reboot (on most systems).

- **`/usr` - User Programs**
  
  - User-installed software, libraries, documentation, and other non-essential (but important) files.
  
  - Often huge — like /Program Files on Windows.

- **`/home` - Home Directories**
  
  - Each user gets this personal space to store files, configs, and documents.

- **`/lib` - System Libraries**
  
  - Shared libraries needed by system programs in `/bin` and `/sbin`.
  
  - Includes kernel modules
