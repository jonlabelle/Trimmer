Trimmer
=======

[Trimmer](http://jonlabelle.github.io/Trimmer/) is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.

**Features**
 
- Trim whitespace at the end of each line.
- Trim whitespace at the start of each line.
- Trim whitespace at the start and end of each line.
- Delete empty, whitespace only lines.
- Collapse multiple consecutive empty lines into one empty line.
- Trim empty, whitespace only lines at the beginning and end of the file.
- Remove blank space characters.

**Extra**

- Replace *smart* characters command that peforms the following actions:
	* **Smart single quotes:** `’‘` to `''`
	* **Smart double quotes:** `“”` to `""`
	* **Ellipses:** `…` to `...`
	* **Em dash:** `—` to `---`
	* **En dash:** `–` to `--`
	* **Middot:** `•` to `*`

Watch a [**Quick Demo**](https://raw.githubusercontent.com/jonlabelle/Trimmer/gh-pages/images/trimmer_demo.gif)
 
![ScreenShot](https://raw.githubusercontent.com/jonlabelle/Trimmer/gh-pages/images/trimmer_ss_cmd_palette.png)
  
## Compatibility

Trimmer is compatible with Sublime Text 2 and 3, on *all* OS platforms (OS X, Windows and Linux).

## Install

### Package Control

The easiest, and recommended way to install Trimmer is using [Package Control](https://sublime.wbond.net).

From the main application menu, navigate to:

- `Tools` -> `Command Palette...` -> `Package Control: Install Package`, type the word **`Trimmer`**, then select it to complete install.

### Git

To install Trimmer using Git, change to your Sublime Text ***Packages*** directory, and clone the [Trimmer repository](https://github.com/jonlabelle/Trimmer).

	# on OS X... cd to your Packages directory and clone the Git repository
	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ &&
	    git clone https://github.com/jonlabelle/Trimmer

### Manually

**Download** and **extract** the [zip file](https://github.com/jonlabelle/Trimmer/zipball/master) or [tarball](https://github.com/jonlabelle/Trimmer/tarball/master) to your Sublime Text ***Packages*** directory. Listed below are the *default* locations for Sublime Text Packages.

**OS X**

	~/Library/Application Support/Sublime Text [2|3]/Packages

**Linux**

	~/.Sublime Text [2|3]/Packages

**Windows**

	%APPDATA%/Sublime Text [2|3]/Packages

> Don't forget to replace the `[2|3]` part with the appropriate Sublime Text version for your installation.

## Usage

### Key Bindings

The *default* key binding will trim trailing whitespace at the end of each of line (entire file).

- **OS X**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

## Command Accessibility

All commands are accessible from the **Command Palette** using prefix `Trimmer`, and in the **Main Menu** under `Edit` -> `Line` -> *Trimmer* command.

**Screenshots**

- from the [Command Palette](https://raw.githubusercontent.com/jonlabelle/Trimmer/gh-pages/images/trimmer_ss_cmd_palette.png)
- from the [Main Menu](https://raw.githubusercontent.com/jonlabelle/Trimmer/gh-pages/images/trimmer_ss_main_menu.png)

## Trimmer Command API

|              Command               |                              Description                               |          Context          |
|------------------------------------|------------------------------------------------------------------------|---------------------------|
| `trimmer`                          | trim whitespace at the end of each line                                | entire file               |
| `trim_leading_whitespace`          | trim whitespace at the start of each line                              | selection, or entire file |
| `trim_leading_trailing_whitespace` | trim whitespace at the start and end of each line                      | selection, or entire file |
| `delete_empty_lines`               | delete empty, whitespace only lines                                    | selection, or entire file |
| `collapse_empty_lines`             | collapse multiple consecutive empty lines into one empty line          | selection, or entire file |
| `trim_edges`                       | trim empty, whitespace only lines at the beginning and end of the file | entire file               |
| `remove_blank_spaces`              | remove all blank space characters (tab, cr, ff, vt, space)             | selection, or entire file |

## Author

[Jon LaBelle](http://jonlabelle.com)

## License

Trimmer is licensed under the [MIT license](http://opensource.org/licenses/MIT).
