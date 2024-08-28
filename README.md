Hello to everyone. Today I want to share with you the first tool
I wrote. I believe this tool will be very useful. The purpose of the
tool is to combine different encryption algorithms. My goal in writing
the tool is to bypass Regex (Regular Expression) against XSS (Cross-Site
Scripting) attacks on web pages protected by WAF (Web Application
Firewall). The principle of operation is recorded on the Github
platform.

Linkedln:
[[https://www.linkedin.com/in/r%C3%BCst%C9%99m-m%C9%99mm%C9%99dzad%C9%99-b78736278/]{.underline}](https://www.linkedin.com/in/r%C3%BCst%C9%99m-m%C9%99mm%C9%99dzad%C9%99-b78736278/)

Detailed work principle of this tool is shown below:

1\) User writes the payload which he/she wants to encode.

2\) Tool asks to user that, which encoding algorithm do you want to use?

3\) After the choice, tool asks how many characters do you want to
encode? Sometimes user needs to encode more than 1 character for
bypassing filters.

4\) Then, tool asks which characters do you want to encode? According to
the answer to the previous question this question will be repeated.

5\) The encoded result is shown as \"Current encoded result:\"

6\) Tool asks you do you want to continue encoding? If the answer is
\"Yes\", the entire process will be repeated, but it doesn\'t ask for
the user input again. The whole process will be done according to the
result of the first encoding. If the answer is \"No\" the process will
be ended and the encoded form of user input will be shown.

7\) User can do multiple encoding at the same time, with choosing the
8th choise at Encoding method choise time.
