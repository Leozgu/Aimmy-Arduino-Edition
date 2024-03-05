# Aimmy Arduino Edition
Aimmy 1.5.2... but with Arduino support!
Wish I could add this to Aimmy 2.0, but unfortunately, it's closed source and I'm not an official dev for Aimmy.

also the source is on the master branch so it doesnt show up by default, just change the branch view from main to master

**DO NOT DM ME ON DISCORD FOR HELP I WILL BLOCK YOU**

Tags: Arduino AI Aim, AI chair, AI Aim Assist, AI undetected, Undetected bot, Fortnite Bot Undetected, Fortnite Arduino

# Features and Advantages:
- HID communication (No COM port required! Say goodbye to detection!)
- Easy to setup, just upload the script to your Arduino and get to work! (Unless you haven't spoofed your Arduino and disabled the COM port)
- Unlike Aimmy, fully undetected in R6, CoD, Apex, Fortnite, and some other games. If you use this in Valorant, it'll flag your account so you won't get banned for a month or 2 or until you reach Ascendant rank. CS2 FaceIt probably isn't safe either.

# Downsides:
- As of right now, it does not support USB Host Shields. (Should be easy to add though! If you succeed in adding it, please message me on Discord: Seconb). I can't add Host Shield support because I don't have one.
- Does not support Arduinos that don't have an ATmega32U4 chip, meaning only the Arduino Micro and Arduino Leonardo R3 will work.
- The Aimmy part itself is really easy to setup because you just extract it and run Netflix.vmp.exe, but if you don't know how to use an Arduino then have fun doing the tutorial below! I will not help you I swear to god if you DM me asking for help (and not related to the Host Shield thing I said above) I will block you so fast.

# Setup Tutorial
- https://streamable.com/oknd08 VIDEO TUTORIAL!!!
- Download Arduino IDE 1.8.19, accept everything in the setup. https://downloads.arduino.cc/arduino-1.8.19-windows.exe
- Go to MouseInstructArduino, and spoof your Arduino by pressing 1, then selecting your mouse. Press Y to disable COM port, it's optional but recommended.
- Go to the download for the tool and extract it anywhere https://github.com/Seconb/Aimmy-Arduino-Edition/releases/tag/v1
- Go to the MouseInstructArduino folder and run arduinospoofer.exe **AS ADMIN!! (REALLY IMPORTANT)**
- Go to the MoustInstructArduino folder and run MouseInstructArduino.ino
- When that opens, press CTRL+SHIFT+I. Search HID-Project and install it. It should say it's by NicoHood
- Next, click the button in the top left that shows an arrow pointing to the right (the Upload button) then QUICKLY press and hold the reset button for 1 second on your Arduino, then let go. The button should look something like this: https://support.arduino.cc/hc/article_attachments/5779192777244
- After it says "Done uploading" open Device Manager on your PC, you can just press the Windows Key and start typing "Device Manager" and it should pop up.
- Click the arrow next to "Ports (COM & LPT)"
- If the only thing you see is "Communications Port (COM1)" you're good.
- Close Device Manager and open Control Panel
- Click "View Devices and Printers", if you see one of the Devices looks like a mouse and it's called HID-compliant device or like the same name as the one you put while spoofing your Arduino, you're good.
- If you see something other than COM1 or you see an Arduino in Control Panel instead of HID-compliant device or something like that then you messed up in disabling COM port or spoofing. Do some Googling and fix your mistake or ask someone who knows what they're doing to help you. (**DO NOT DM ME ON DISCORD FOR HELP I WILL BLOCK YOU**)
- If you're an official tester for the program you can DM me.
- Run Netflix.vmp.exe as Admin
- Yes I know it looks suspicious as hell when you open "Netflix" and see a bunch of command prompts open and close I swear on god I'm not ratting 😭, It's just what the C# code does. The Netflix thing is also just a security measure against anti-cheats. If you don't believe me, try decompiling the program with ilSpy and decompile the mousemovement.exe using pyinstxtractor or whatever it's called. It's open source anyway so who cares!
- If it says "Mouse device found" in the console window then that means it's probably working. Use it the same as you would use normal Aimmy. DO NOT CLOSE THE CONSOLE WINDOW OR YOU WILL HAVE TO REOPEN AIMMY.

**DO NOT DM ME ON DISCORD FOR HELP I WILL BLOCK YOU**

# Credits:
- [https://github.com/khanxbahria/MouseInstruct]([url](https://github.com/khanxbahria/MouseInstruct)) - HUGE HELP THIS REPO IS REALLY AWESOME AND THE ONLY REASON WHY THIS EXISTS GO TO IT AND STAR IT!!!!
- ChatGPT Plus - Self explanatory, completed the parts I was too lazy to write
- Seconb (me) - I did all the work over a span of like 6 or 7 hours (the first prototype took like 4 hours and didn't work so I had to start from scratch, then the second version worked)
- The full team behind Aimmy obviously because I didn't make Aimmy
