Trimmer
=======

[Trimmer](http://jonlabelle.github.io/Trimmer/) is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.

- Trim whitespace at the end of each line.
- Trim whitespace at the start of each line.
- Trim whitespace at the start and end of each line.
- Delete empty, whitespace only lines.

## Compatibility

Trimmer is compatible with both Sublime Text 2 and Sublime Text 3, on all OS platforms (OS X, Windows and Linux).

## Installing

### Package Control

If you have [Package Control](https://sublime.wbond.net) installed, simply navigate to:

- **Tools**
    - **Command Palette...**
    - **Package Control:** ***Install Package***
        - type the word `Trimmer`

### Git

To install Trimmer using Git, change to your Sublime Text ***Packages*** directory, and clone the [Trimmer repository](https://github.com/jonlabelle/Trimmer).

```sh
# on OS X... cd to your Packages directory and clone the Git repository
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ &&
    git clone https://github.com/jonlabelle/Trimmer
```

### Manually

You can also manually install Trimmer.

Download and extract the [zip file](https://github.com/jonlabelle/Trimmer/zipball/master) to your ***Packages*** directory. Listed below are the default Sublime Text ***Packages*** directories by platform.

```sh
# OS X
~/Library/Application Support/Sublime Text [2|3]/Packages

# Linux
~/.Sublime Text [2|3]/Packages

# Windows
%APPDATA%/Sublime Text [2|3]/Packages
```

> **NOTE:** replace the `[2|3]` part above with the appropriate Sublime Text *major* version of your install.

## Usage

### Key Bindings

The *default* key binding will trim trailing whitespace at the end of each of line (entire file).

- **OS X**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Commands

All commands are accessible from the **Command Palette** and prefixed with `Trimmer:`.

### Trimmer Sublime Text Command Reference

|              command               |                    description                    |            context             |
| ---------------------------------- | ------------------------------------------------- | ------------------------------ |
| `trimmer`                          | trim whitespace at the end of each line           | entire file                    |
| `trim_leading_whitespace`          | trim whitespace at the start of each line         | selected lines, or entire file |
| `trim_leading_trailing_whitespace` | trim whitespace at the start and end of each line | selected lines, or entire file |
| `delete_empty_lines`               | delete empty, whitespace only lines               | selected lines, or entire file |


### Config file

```sh
{
    // Select which command you want to run on file save
    // "trimmer", "trim_leading_whitespace", 
    // "trim_leading_trailing_whitespace", "delete_empty_lines", 
    // or "none" to not run any of these commands when a file is saved.
    "run_on_save": "none"
}
```

## Author

- [Jon LaBelle](http://jonlabelle.com/)
