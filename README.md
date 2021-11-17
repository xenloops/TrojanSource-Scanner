# TrojanSource-Scanner
Checks for attack described at https://trojansource.codes, and in the preprint at https://arxiv.org/abs/2111.00169.

The tl;dr is that control characters in Unicode relating to bidirectionality (i.e. whether text in a language is read left-to-right or right-to-left) could be used to create arbitrary source code that would pass a standard manual code review, yet compile to exhibit functionality unintended by the design team. This is extremely concerning for open-source libraries widely used in commercial products, web sites, mobile apps, and desktop applications. The site and paper above give straightforward examples and list some concerning code editors that do not display the control characters.

This simple Python script scans the source file and lists the positions of specific Unicode characters found (listed in the paper). The filename is hardcoded for now; change this to the file to scan.

I was able to recreate the Java attack example from the paper in the text editor Kate on Debian Linux, and was able to do the same using Visual Studio Code. Both will display printable characters, but Kate interpreted the control chars (as one would expect) as typed:

![image](https://user-images.githubusercontent.com/57366429/141070870-643eb31e-f633-4782-839a-81596f0fb3f6.png)

Code displayed the characters as their Unicode codes, making them easy to spot if used to review the code:

![image](https://user-images.githubusercontent.com/57366429/141069965-82e55976-2196-4d5c-883e-3f0094970db8.png)

The Github editor doesn't show the characters themselves, but does display a nice warning banner and flags the lines in question:

![image](https://user-images.githubusercontent.com/57366429/141071582-bfe2f699-d325-45c1-81c9-b2fe4150b16a.png)

Eclipse, to my chagrin, did not display the codes at all, nor did it attempt to interpret them. So nothing seemed amiss:

![image](https://user-images.githubusercontent.com/57366429/141070160-589b6b53-5128-46bd-a150-c1f5f9e0c5cd.png)

This is a concerning attack on its surface, with the threat that reviewers are not seeing what's actually in the code. But the ease of finding control characters coupled with its new appearance as a possible avenue of attack and the fact that some editors do already show/flag the existance of control characters should put us, if not at ease, then at least aware of the potential and act accordingly.

Future plans:
* Add param(s) for filename(s)/directory, so it isn't hard-coded
* Add param for whether to automatically delete dangerous characters found
* Display line, col instead of char count
* Display section of line containing dangerous character, showing char by its initialism
* Add any other control characters that don't belong in source code
* Add homoglyph attack detection

