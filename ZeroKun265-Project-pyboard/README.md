# ZeroKun265's pyboard

Pyboard requires python 3.x
Pyboard requires the keyboard module, to install it, just run in your terminal:
```pip install keyboard``` or ```python -m pip install keyboard```

```
Usage: pyboard [mode] 

Used to record/replay keyboard inputs
Mode: 
      -r : record keys and play them
      -s=number sets speed factor for playback
      -l : keys are played in loop (only if played, record files are not infinite)
      -R : record keys and store to file
      -p=file : plays keys from file
```

## What does it do?
pyboard is a simple but very useful script that allows to record every action from your keyboard and repeat it, even at a different speed
### Actual uses?
- Did you just copy a big table from the internet but there's whitespaces and weird indentation everywhere? Just start recording, move the cursor with the arrows and deleate all the whitespace from one line, then let pyboard do all of them!
- Do you want to automate the creation of new chrome tabs for some unknown reason? You can do it too
- Do you want to spam messages to your group friends so fast they won't know what hit them? Then pyboard's for you

## Currently unsupported
Sadly the record to file and play file feature don't work right now, but this still hase a lot of uses(and I'll update the repo when i get them working)

## Supported
All platforms, Windows, Mac AND Linux!

## How to use
- Open a terminal and prepare to launch the script with the flags you want (Note: since every key gets recorded you might not want to press alt+tab and instead move around with the mouse cursor)
- Start using your keyboard normally, if you mess up just stop the script and start recording again
- Once you did your thing(Note: make sure that, if you need the cursor in a specific place, it's there)
- Move back to the terminal window(once again you may want to use the mouse instead of alt+tab) and press ESC
- This will give you 5 seconds to go back to your window, make sure everything is ready and then it'll start playing

### Notes:
- If the flag ```-l``` is set, to stop the program you need to quickly switch to the terminal window and interrupt the script(For non coders: Ctrl+C will trigger a KeyboardInterrupt and kill python)
- You may want to give yourself a bit of time before and after the recording, because if the keys are too fast you might not be in time to stop it


