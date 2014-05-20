Trimmer
=======

[Trimmer](http://jonlabelle.github.io/Trimmer/) is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.
 
- Trim whitespace at the end of each line.
- Trim whitespace at the start of each line.
- Trim whitespace at the start and end of each line.
- Delete empty, whitespace only lines.
- Collapse multiple consecutive empty lines into one empty line.
- Trim empty, whitespace only lines at the beginning and end of the file.

Watch a [**Quick Demo**](https://raw.githubusercontent.com/jonlabelle/Trimmer/gh-pages/images/trimmer_demo.gif)
 
![ScreenShot](https://raw.githubusercontent.com/jonlabelle/Trimmer/gh-pages/images/trimmer_ss_cmd_palette.png)
  
## Compatibility

Trimmer is compatible with Sublime Text 2 and 3, on all OS platforms (OS X, Windows and Linux).

## Installing

### Package Control

The easiest (and recommended) way to install Trimmer is using [Package Control](https://sublime.wbond.net).

- `Tools` -> `Command Palette...` -> `Package Control: Install Package`  
  
  Type the word `Trimmer`, and select it to install.

### Git

To install Trimmer using Git, change to your Sublime Text ***Packages*** directory, and clone the [Trimmer repository](https://github.com/jonlabelle/Trimmer).

	# on OS X... cd to your Packages directory and clone the Git repository
	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ &&
	    git clone https://github.com/jonlabelle/Trimmer

### Manually

You can also manually install Trimmer.

Download and extract the [zip file](https://github.com/jonlabelle/Trimmer/zipball/master) to your ***Packages*** directory. Listed below are the default Sublime Text ***Packages*** directories by platform.

	# OS X
	~/Library/Application Support/Sublime Text [2|3]/Packages

	# Linux
	~/.Sublime Text [2|3]/Packages

	# Windows
	%APPDATA%/Sublime Text [2|3]/Packages

> **NOTE:** replace the `[2|3]` part above with the appropriate Sublime Text *major* version of your install.

## Usage

### Key Bindings

The *default* key binding will trim trailing whitespace at the end of each of line (entire file).

- **OS X**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Commands

All commands are accessible from the ***Command Palette*** using prefix `Trimmer:`, and in the Main Menu under `Edit` -> `Line`.

#### Trimmer Sublime Text Command Reference

|              Command               |                              Description                               |            Context             |
|------------------------------------|------------------------------------------------------------------------|--------------------------------|
| `trimmer`                          | trim whitespace at the end of each line                                | entire file                    |
| `trim_leading_whitespace`          | trim whitespace at the start of each line                              | selected lines, or entire file |
| `trim_leading_trailing_whitespace` | trim whitespace at the start and end of each line                      | selected lines, or entire file |
| `delete_empty_lines`               | delete empty, whitespace only lines                                    | selected lines, or entire file |
| `collapse_empty_lines`             | collapse multiple consecutive empty lines into one empty line          | selected lines, or entire file |
| `trim_edges`                       | trim empty, whitespace only lines at the beginning and end of the file | entire file                    |

## Author

- [Jon LaBelle](http://jonlabelle.com/)
