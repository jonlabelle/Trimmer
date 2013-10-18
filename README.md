Trimmer
=======

Trimmer is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.

- Remove **trailing** whitespace
- Remove **leading** whitespace
- Remove **leading** and **trailing** whitespace
- Remove **end-of-file** whitespace

  
Compatibility
-------------

Trimmer is compatible with both Sublime Text 2 and Sublime Text 3.


Installing
----------

### Package Install

If you're using [Sublime Package Control](http://wbond.net/sublime_packages/package_control)...

- From `Tools` -> `Command Palette...` -> `Package Control: Install Package`, enter search term ***Trimmer***.

### Git Install

`cd` to your **Packages** directory, and clone the git repository.

```sh
# OSX
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

The default key binding will only remove ***trailing whitespace***.

- **Mac**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

Additional trimming commands can be accessed from...

- `Command Palette...`, prefix `Trimmer: ...`
- or `Edit` -> `Line` -> `Remove ... whitespace`

#### Sublime Text Command Names

- `trimmer`: remove **trailing** whitespace
- `trim_leading`: remove **leading** whitespace
- `trim_leading_trailing`: remove **leading** and **trailing** whitespace
- `trim_eof`: remove **end-of-file** whitespace


Author
------

- [Jon LaBelle](http://jonlabelle.com/)
