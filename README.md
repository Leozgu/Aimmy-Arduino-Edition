## Aimmy Arduino Edition!
Aimmy 1.5.2... but with Arduino support!
Wish I could add this to Aimmy 2.0, but unfortunately, it's closed source and I'm not an official dev for Aimmy.

Star this repo to support me, but to support Aimmy's development donate to Babyhamsta via the attached sponsor link!

**DO NOT ASK FOR HELP ON DISCORD. ONLY DM ME IF YOU WANNA ADD HOST SHIELD SUPPORT.**

Tags: Arduino AI Aim, AI chair, AI Aim Assist, AI undetected, Undetected bot, Fortnite Bot Undetected, Fortnite Arduino

## Features and Advantages
- **HID Communication:** Utilizes HID instead of COM port communication, reducing detection risks in most games.
- **Easy Setup:** Straightforward script upload process to your Arduino. Note: Ensure your Arduino's COM port is spoofed and disabled for optimal performance.
- **Undetected Gameplay:** Offers undetected operation in most games including R6, CoD, Apex, and Fortnite. Detected in Valorant and CS2 FaceIt.

## Limitations

- **USB Host Shields:** Does not support USB Host Shields. Community contributions for this feature are welcome. Plug your mouse into your PC instead of the shield if you are using one.
- **Chip Compatibility:** Specifically designed for Arduinos with an ATmega32U4 chip, such as the Leonardo R3. Other Arduinos might work by installing HoodLoader2 but the autospoofer won't work with those.

## Setup Tutorial
- [Video Tutorial](https://streamable.com/oknd08) 
- Download and install [Arduino IDE 1.8.19](https://downloads.arduino.cc/arduino-1.8.19-windows.exe)
- Download [Aimmy Arduino Edition Download](https://github.com/Seconb/Aimmy-Arduino-Edition/releases/tag/v1) and extract it
- Go to the MouseInstructArduino folder and run arduinospoofer.exe **as admin**
- Once that finishes, open MouseInstructArduino.ino
- In that window, press CTRL+SHIFT+I. Search HID-Project and install it
- Next, click the upload button (the arrow pointing to the right in the top left of the Arduino IDE), wait one second, then press the red RESET button on your Arduino in real life
- If it says "Done Uploading.", you're set to continue, otherwise try again or fix whatever error it gave you.
- Run Netflix.vmp.exe as Admin
- Multiple CMD windows and also Aimmy will pop up. Most of the CMD windows will close, and the one that doesn't should say "Mouse device found!". If not, make sure you've followed all steps correctly.

**DO NOT ASK ME FOR HELP ON DISCORD**

## Credits:

- [MouseInstruct Repository](https://github.com/khanxbahria/MouseInstruct) for their amazing HID library. Made mouse movement via Arduino easy.
- Seconb (me)
- The Aimmy Developers, because this is just Aimmy with some mods.
