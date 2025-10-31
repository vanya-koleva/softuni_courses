echo "1. Checking current directory:"
pwd

echo "2. Listing files:"
ls

echo "3. Listing hidden files with details:"
ls -al

echo "4. Listing hidden files:"
ls -a

echo "5. Listing files with details in the root directory:"
ls -al /

echo "6. Changing directory to /etc:"
cd /etc

echo "7. Files starting with 'os':"
ls os*

echo "8. Content of os-release:"
cat os-release

echo "9. Information about the distibution:"
uname -a

echo "10. Hostname:"
hostname

echo "11. Changing directory back to home:"
cd

echo "12. Hostname:"
cat /etc/hostname

echo "13. Changing hostname:"
hostname my-new-hostname

echo "14. Log out and back in to see hostname change. Display hostname:"
hostname

echo "15. Current date:"
date

echo "16. Formatted date (YYYY-MM-DD):"
date +%Y-%m-%d

echo "17. Displaying calendar for the next 3 months:"
cal -3

echo "18. Checking system uptime:"
uptime

echo "19. Displaying command history:"
history

echo "20. Checking bash history file:"
cat ~/.bash_history

echo "21. Exiting session:"
exit
