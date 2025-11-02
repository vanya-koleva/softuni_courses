# Linux and Linux Shell

## Users and Groups

📄 Users file: `/etc/passwd`

📄 Groups file: `/etc/group`

📄 `/etc/shadow` - Stores encrypted passwords and password policies. Readable only by root.

- Root User (Superuser):
  
  - User ID (UID): 0
  
  - The administrative account with unlimited, unrestricted power over the entire system.

- System Users (Service Accounts):
  
  - UID Range: 1-999 (on most modern systems)
  
  - Non-login accounts created during software installation to run system services.
  
  - If a service is compromised, the damage is contained to that system user's privileges.

- Common commands:

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
