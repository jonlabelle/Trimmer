Trimmer
=======

A [Sublime Text 2](http://www.sublimetext.com) plugin that removes trailing whitespace from the end of each line.

Trimmer can also be used as alternative to the built-in setting, `trim_trailing_white_space_on_save`, for explicitly controlling when trimming is performed. *See the [Usage](#usage) section for more information*.

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

*Trimmer's* default behavior is to remove trailing whitespace from the end of each line. See [Optional Settings](#optional-settings) for additional trimming capabilities.

### Optional Settings

**Trimmer Settings**

- `Preferences` --> `Package Settings` --> `Trimmer` --> `Settings - Default` | `Settings - User`

#### Trim whitespace from end-of-file

Removes all whitespace characters (including newlines), from the end of the document. The default value is `false`.

```javascript
"trim_eof": false // default
```

NOTE: This setting will adhere to the default `ensure_newline_at_eof_on_save` setting, and leave a single end-of-file newline character if specified.

#### Save after Trim

Saves the current document/buffer immediately after trimming is performed. The default value is `false`.

```javascript
"save_after_trim": false // default
```

~~Ensure you're not overriding the *Default* Sublime Text 2 setting, `trim_trailing_white_space_on_save` (which is set to `false`) in your *User* settings. Otherwise, you're just duplicating it's behavior.~~

### Key Bindings

- **Mac**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Sublime Text Command

- `trimmer`

Description: Removes trailing whitespace from the end of each line.

Author
------

[Jon LaBelle](http://jonlabelle.com)
