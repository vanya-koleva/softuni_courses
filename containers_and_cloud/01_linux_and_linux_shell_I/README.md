# Linux and Linux Shell

## Common Commands

- `whoami` - Display the currently logged-in user

- `uname -a` - Display OS information

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

