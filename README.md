Trimmer
=======

Trimmer is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.

- Trim whitespace at the end of each line.
- Trim whitespace at the start of each line.
- Delete empty, whitespace only lines.

Compatibility
-------------

Trimmer is compatible with both Sublime Text 2 and Sublime Text 3, on all OS platforms.


Installing
----------

### Sublime Package Control

If you have [Sublime Package Control](http://wbond.net/sublime_packages/package_control) installed, simply navigate to:

- `Tools` -> `Command Palette...` -> `Package Control: Install Package`, and type **`Trimmer`**.

### Git Install

Change to your Sublime Text ***Packages*** directory, and clone the [Trimmer repository](https://github.com/jonlabelle/Trimmer).

```sh
# Sublime Text 3 OSX git install
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ &&
    git clone https://github.com/jonlabelle/Trimmer
```

### Manual Install

[Download](https://github.com/jonlabelle/Trimmer/zipball/master) and extract the [zip](https://github.com/jonlabelle/Trimmer/zipball/master) to your ***Packages*** directory.

```sh
# OSX Sublime Text Pacakges Path
~/Library/Application Support/Sublime Text [2|3]/Packages

# Linux Sublime Text Pacakges Path
~/.Sublime Text [2|3]/Packages

# Windows Sublime Text Pacakges Path
%APPDATA%/Sublime Text [2|3]/Packages
```

> **NOTE:** replace the `[2|3]` part above with the appropriate *major* version of your install.


Usage
-----

### Default Key Binding

The *default* key binding will trim trailing whitespace from the end of each of line, in current view.

- **Mac**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Running Commands

All commands are accessible from the **Command Palette**, prefix `Trimmer: ...`.

### Sublime Text Commands

|          command          |                description                |             scope              |
| ------------------------- | ----------------------------------------- | ------------------------------ |
| `trimmer`                 | trim whitespace at the end of each line   | entire file                    |
| `trim_leading_whitespace` | trim whitespace at the start of each line | line selection, or entire file |
| `delete_empty_lines`      | deletes empty, whitespace only lines      | line selection, or entire file |


Author
------

- [Jon LaBelle](http://jonlabelle.com/)
