Trimmer
=======

Trimmer is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.

- Remove **trailing** whitespace.
- Remove **leading** whitespace.
- Remove **leading** and **trailing** whitespace.
- Remove whitespace at the **top** of the file.
- Remove whitespace at the **end** of the file.
- Remove **empty** lines.


Compatibility
-------------

Trimmer is compatible with both Sublime Text 2 and Sublime Text 3.


Installing
----------

### Sublime Package Control Install

If you're using [Sublime Package Control](http://wbond.net/sublime_packages/package_control)...

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

The *default* key binding will remove **trailing whitespace** from each line.

- **Mac**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Running Commands

All commands can be run directly from the **Command Palette** or by navigating the **Application Menu**.

- **Command Palette**: prefix, `Trimmer: ...`
- **Application Menu**: `Edit` -> `Line` -> `Remove ... whitespace`

### Sublime Text Commands

|    command    |                  description                   |        context         |
| ------------- | ---------------------------------------------- | ---------------------- |
| `trimmer`     | remove **trailing** whitespace                 | file/buffer            |
| `trim_left`   | remove **leading** whitespace                  | file/buffer, selection |
| `trim_both`   | remove **leading** and **trailing** whitespace | file/buffer            |
| `trim_top`    | remove whitespace at the **top** of the file   | file/buffer            |
| `trim_bottom` | remove whitespace at the **end** of the file   | file/buffer            |
| `trim_empty`  | remove **empty** lines                         | file/buffer, selection |


Author
------

- [Jon LaBelle](http://jonlabelle.com/)
