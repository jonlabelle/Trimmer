# Trimmer

[![ci](https://github.com/jonlabelle/Trimmer/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/jonlabelle/Trimmer/actions/workflows/ci.yml)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/fdcdvfsip9d9efg3?svg=true)](https://ci.appveyor.com/project/jonlabelle/trimmer)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/jonlabelle/Trimmer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/jonlabelle/Trimmer/context:python)
[![Package Control Installs](https://img.shields.io/packagecontrol/dt/Trimmer.svg?label=installs)](https://packagecontrol.io/packages/Trimmer)
[![Latest Release](https://img.shields.io/github/tag/jonlabelle/Trimmer.svg?label=version)](https://github.com/jonlabelle/Trimmer/releases)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/jonlabelle/Trimmer/blob/master/LICENSE.md)

> [Trimmer](https://github.com/jonlabelle/Trimmer) is a [Sublime Text](http://www.sublimetext.com) plug-in for cleaning up whitespace.

## Features

- Trim whitespace at the end of each line.
- Trim whitespace at the start of each line.
- Trim whitespace at the start and end of each line.
- Trim whitespace from selection(s).
- Delete empty, whitespace only lines.
- Collapse multiple consecutive empty lines into one empty line.
- Collapse multiple consecutive spaces into one space.
- Trim empty, whitespace only lines at the beginning and end of file.
- Remove blank space characters.
- Normalize spaces (consecutive spaces reduced, empty lines removed and lines trimmed).
- Tokenize a string by collapsing consecutive spaces, and trimming leading and trailing spaces.
- Delete empty, whitespace only HTML and XML tags.
- Remove code comments and collapse lines.

## Additional Features

A **Replace Smart Characters** command that performs the following actions:

- **Smart single quotes:** `’` *to* `'`
- **Smart double quotes:** `“` *to* `"`
- **Prime:** `′` *to* `'`
- **Double Prime:** `″` *to* `"`
- **German quotes:** `„` *to* `"` and `‚` *to* `'`
- **Ellipsis:** `…` *to* `...`
- **Em dash:** `—` *to* `---`
- **En dash:** `–` *to* `--`
- **Bullet:** `•` *to* `*`
- **Middle dot:** `·` *to* `-`
- **Em space** *to* three spaces
- **En space** *to* two spaces
- **Non-breaking space** *to* one space
- **Thin space** *to* one space
- **Hair space** *to* one space
- **Left angle quote:** `«` *to* `<<`
- **Right angle quote:** `»` *to* `>>`
- **Copyright symbol:** `©` *to* `(C)`
- **Trademark symbol:** `™` *to* `(T)`
- **Registered trademark symbol:** `®` *to* `(R)`

![ScreenShot](https://raw.githubusercontent.com/jonlabelle/Trimmer/master/screenshots/command_palette.png)

Watch a [**Quick Demo**](https://raw.githubusercontent.com/jonlabelle/Trimmer/master/screenshots/demo.gif)

## Install

Trimmer is compatible with both Sublime Text 2 and 3 and all supported Operating Systems.

### Package Control

The easiest, and recommended way to install Trimmer is using [Package Control](https://packagecontrol.io).

From the main application menu, navigate to:

- `Tools` -> `Command Palette...` -> `Package Control: Install Package`, type
  the word ***Trimmer***, then select it to complete installation.

### Git

To install Trimmer using Git, change to your **Sublime Text Packages** directory
and clone the [Trimmer repository](https://github.com/jonlabelle/Trimmer).

For example, on **OS X**... start a new **Terminal** session and enter the following
commands:

```shell
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ git clone https://github.com/jonlabelle/Trimmer
```

### Manually

**Download** and **extract** the [zip](https://github.com/jonlabelle/Trimmer/zipball/master)
or [tarball](https://github.com/jonlabelle/Trimmer/tarball/master) to your
Sublime Text packages directory.

**Default Sublime Text Packages Paths:**

* **OS X:** `~/Library/Application Support/Sublime Text [2|3]/Packages`
* **Linux:** `~/.Sublime Text [2|3]/Packages`
* **Windows:** `%APPDATA%/Sublime Text [2|3]/Packages`

> **NOTE** Replace the `[2|3]` part with the appropriate Sublime Text
> version for your installation.

## Usage

All commands are accessible from the **Command Palette** using prefix
***Trimmer***, and in the **Main Menu** under `Edit` -> `Line` -> *Trimmer* command.

- [Command Palette screenshot](https://raw.githubusercontent.com/jonlabelle/Trimmer/master/screenshots/command_palette.png)
- [Main Menu screenshot](https://raw.githubusercontent.com/jonlabelle/Trimmer/master/screenshots/main_menu.png)

### Key Bindings

The *default* key binding will trim trailing whitespace at the end of each of
line (entire file).

- **OS X**: `Ctrl + S`
- **Linux**: `Ctrl + Alt + S`
- **Windows**: `Ctrl + Alt + S`

### Trimmer Command API

|              Command               |                                              Description                                               |          Context          |
|------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------|
| `trimmer`                          | trim whitespace at the end of each line                                                                | entire file               |
| `trim_leading_whitespace`          | trim whitespace at the start of each line                                                              | selection, or entire file |
| `trim_leading_trailing_whitespace` | trim whitespace at the start and end of each line                                                      | selection, or entire file |
| `trim_selections`                  | trim whitespace from selection(s)                                                                      | selection                 |
| `delete_empty_lines`               | delete empty, whitespace only lines                                                                    | selection, or entire file |
| `collapse_lines`                   | collapse multiple consecutive empty lines into one empty line                                          | selection, or entire file |
| `collapse_spaces`                  | collapse multiple consecutive spaces into one space                                                    | selection, or entire file |
| `trim_edges`                       | trim empty, whitespace only lines at the beginning and end of the file                                 | entire file               |
| `remove_blank_spaces`              | remove all blank space characters (tab, cr, ff, vt, space)                                             | selection, or entire file |
| `normalize_spaces`                 | consecutive spaces reduced, empty lines removed and lines trimmed                                      | selection, or entire file |
| `replace_smart_characters`         | replace smart characters (smart quotes, em/en dash, ellipsis, nbsp)                                    | selection, or entire file |
| `tokenize_string`                  | convert a string to a token by collapsing consecutive spaces, and trimming leading and trailing spaces | selection, or entire file |
| `delete_empty_tags`                | delete empty, whitespace only html and xml tags                                                        | selection, or entire file |
| `remove_comments`                  | remove code comments and collapse lines                                                                | selection, or entire file |

## Author

[Jon LaBelle](https://jonlabelle.com)

## License

Trimmer is licensed under the [MIT license](http://opensource.org/licenses/MIT).
