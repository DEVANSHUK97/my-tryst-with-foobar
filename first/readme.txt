
Mounting /home/guest...
Welcome to foobar version 1-335-gea1c3e3-beta (2021-01-25T20:45:33.542835)

Google has a code challenge ready for you.
Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on their space station. From here, you just might be able to subvert Commander Lambda's plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

Warning! Your invitation may expire if you leave this page. Click here to sign in so you can save your progress and resume later.

For a list of commands type help. To get started with your first challenge type request.

Mounting /home/khurmad...
Logged in as khurmad.
foobar:~/ khurmad$ help
Use the following shell commands:

cd	change directory [dir_name]
cat	print file [file_name]
deleteme	delete all of your data associated with foobar
edit	open file in editor [file_name]
feedback	provide feedback on foobar
less	print a file a page at a time [file_name]
ls	list directory contents [dir_name]
request	request new challenge
status	print progress
submit	submit final solution file for assessment [file_name]
verify	runs tests on solution file [file_name]

Keyboard help:

Ctrl + S	save the open file [when editor is focused]
Ctrl + E	close the editor [when editor is focused]

Toggle between the editor and terminal using ESC followed by TAB, then activate with ENTER.

foobar:~/ khurmad$
foobar:~/ khurmad$ ls
journal.txt
start_here.txt
foobar:~/ khurmad$ cat start_here.txt
Type request to request a challenge. Type help for a list of commands.
foobar:~/ khurmad$ cat journal.txt
Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on their space station. From here, you just might be able to subvert Commander Lambda's plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...
foobar:~/ khurmad$ request
You are about to begin a TIME-LIMITED challenge. You will have 7 days to complete each newly requested challenge or LOSE ACCESS to this site.
Do you wish to proceed and start the timer on your first challenge?
[Y]es or [N]o: y
Requesting challenge...
Why did you sign up for infiltration duty again? The pamphlets from Bunny HQ promised exotic and interesting missions, yet here you are drudging in the lowest level of Commander Lambda's organization. Hopefully you get that promotion soon...
New challenge "Re-ID" added to your home folder.
Time to solve: 168 hours.
foobar:~/ khurmad$ cd re-id/

foobar:~/re-id khurmad$ cat readme.txt
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random IDs based on a Completely Foolproof Scheme.

Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(0)
Output:
    23571

Input:
Solution.solution(3)
Output:
    71113

-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
