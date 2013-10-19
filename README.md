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

[Download](https://github.com/jonlabelle/Trimmer/zipball/master) and extract the [zip](https://github.com/jonlabelle/Trimmer/zipball/master) to your **Packages** directory.

```sh
# OSX path
~/Library/Application Support/Sublime Text 2|3/Packages

# Linux path
~/.Sublime Text 2|3/Packages

# Windows path
%APPDATA%/Sublime Text 2|3/Packages
```

> **NOTE:** be sure to replace `2|3` with the appropriate version of your install.


Usage
-----

### Default Key Binding

The default key binding will remove **trailing** whitespace from each line.

- **Mac**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Running Commands

- **Command Palette Prefix** 
    - `Trimmer: ...`
- **Application Menu** 
    - `Edit` -> `Line` -> `Remove ... whitespace`

### Sublime Text Command Names

|    command    |                  description                   |
| ------------- | ---------------------------------------------- |
| `trimmer`     | remove **trailing** whitespace                 |
| `trim_left`   | remove **leading** whitespace                  |
| `trim_both`   | remove **leading** and **trailing** whitespace |
| `trim_top`    | remove whitespace at the **top** of the file   |
| `trim_bottom` | remove whitespace at the **end** of the file   |
| `trim_empty`  | remove **empty** lines                         |


Author
------

- [Jon LaBelle](http://jonlabelle.com/)
