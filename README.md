# screen-reader-dh7445
screen-reader-dh7445 created by GitHub Classroom

## How to
1. Install NVDA
2. Enable NVDA development
	1. Open NVDA
	2. Go to Settings > Advanced
	3. Check "I Understand that changing..." checkbox
	4. Check "Enable loading custom code from Developer Scratchpad directory"
3. Open developer scratch directory
	1. Can be opened from NVDA from Settings > Advanced > Open Developer Scratchpad Directory" or
	2. (Windows) Through windows explorer, usually under C:\Users\[USER]\AppData\Roaming\nvda\scratchpad
4. Download "running processes.py"
5. Copy file into 'globalPlugins' directory under Scratchpad directory
6. Open or Restart NVDA | Reload Plugins through Tools > Reload Plugins


## Commands to trigger add-on

"Control+NVDA+1"  --> Reads top 5 processes based on memory usage

"Control+NVDA+2"  --> Reads all processes

"Control+NVDA+3"  --> Reads programs
