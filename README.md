This is the Russian version. If you want to modify it to your language, just change the function names in the Python script :)

The password in Telegram is 12345, and it is present in the script itself.

You need to insert the Telegram bot token into config.py.

This script uses the following modules:
- **telebot**: For working with the Telegram API and creating bots.
- **io.StringIO**: For working with input-output streams in string format.
- **sys**: For accessing system variables and functions.
- **os**: For working with the operating system, including access to environment variables and the file system.
- **subprocess**: For running and managing child processes, such as executing external commands.
- **config**: Presumably, this is a module with configuration data containing Telegram API keys or other settings. Usually created by the user and not included in the standard Python library.
- **ctypes**: For calling functions from the C library.
- **pyautogui**: For automating interactions with the user interface, such as mouse and keyboard control.
- **datetime**: For working with dates and times.
- **pymsgbox**: For creating dialog boxes in Python.
- **PIL.ImageGrab**: For capturing screen images.

```plaintext
pip install pytelegrambotapi pyautogui pymsgbox pillow
```
![image](https://github.com/Danik105/TelegramRemotePC/assets/41839304/fa5f82b0-4a10-426a-9a5f-43c2bb962f0c)

start.bat - launches the script in hidden mode on Windows.

The Task Manager shown in the screenshot includes the ability to close processes. When this function is selected, the process specified by the user will be terminated, after which information about it will be sent to the bot.
