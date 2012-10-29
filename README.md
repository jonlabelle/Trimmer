Trimmer
=======

A [Sublime Text 2](http://www.sublimetext.com) plugin that removes trailing
whitespace from lines and saves the document.

Installation
------------

As always, the recommended method for installation is via [Sublime Package Control](http://wbond.net/sublime_packages/package_control).

Open the `Command Palette...` --> `Package Control: Install Package` and search for `Trimmer`.

#### Alternative installation methods

##### Install using Git

1. Locate your Sublime Text 2 `Packages` directory by using the menu item `Preferences -> Browse Packages...`.
2. Run the following command from your `Packages` directory:
  - `git clone https://github.com/jonlabelle/Trimmer "Trimmer"`

##### Manually install

1. [Download](https://github.com/jonlabelle/Trimmer/zipball/master) the the zip.
2. Copy the *Trimmer* folder to your Sublime Text 2 *Packages* directory.
  - **Mac**: `~/Library/Application Support/Sublime Text 2/Packages`
  - **Linux**: `~/.Sublime Text 2/Packages`
  - **Windows**: `%APPDATA%/Sublime Text 2/Packages`

Usage
-----

Ensure you're not overriding the *Default* Sublime Text 2 setting, `trim_trailing_white_space_on_save` (which is set to `false`) in your *User* settings. Otherwise, you're just duplicating it's behavior.

#### Keymap

There is currently only one default keymap defined by *Trimmer*, and that is for the **Mac**. For *Linux* and *Windows*, you will need to manually add a *Key Binding* for the command named `trimmer`.

- **Mac**: `Ctrl + S`
- **Linux**: `not mapped`
- **Windows**: `not mapped`

#### Command

- `trimmer`

Remove trailing whitespace from lines and save.

Author
------

[Jon LaBelle](http://jonlabelle.com)