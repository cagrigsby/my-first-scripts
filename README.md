# pw-expiry

These are scripts to determine which Linux users have not changed their passwords in the last 30 days. 
Please note that the bash script filters out system accounts by beginning the substring from the a specific starting index. 
In my case, the users accounts began in my /etc/shadow file at index 369. 
Your results may vary. You can return all accounts, including system accounts by substituting "${OUT:369}" on the last line for "$OUT".
Alternatively, you can subsitute the "369" for whatever index begins the user accounts for your Linux distro or situation. 
Cheers
