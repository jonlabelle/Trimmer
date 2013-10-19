import sublime
import sublime_plugin
import re


class TrimLeadingTrailingCommand(sublime_plugin.TextCommand):

    """Trim leading and trailing whitespace."""

    def run(self, edit):
        view = self.view

        trim = view.find_all("^[ \t]+|[ \t]+$")
        trim.reverse()

        for r in trim:
            view.erase(edit, r)

        sublime.status_message(
            'Trimmer: leading and trailing whitespace removed.')


class TrimEofCommand(sublime_plugin.TextCommand):

    """Trim end-of-file whitespace."""

    def run(self, edit):
        view = self.view

        if view.size() > 0:
            eofc = "\n" if view.settings().get(
                "ensure_newline_at_eof_on_save") is True else ""
            region = sublime.Region(0, view.size())

            edited_text = re.sub(
                r"(?m)[\s]*$(?![\w\W])", eofc, view.substr(region))
            view.replace(edit, region, edited_text)

        sublime.status_message('Trimmer: end-of-file whitespace removed.')


class TrimEmptyLinesCommand(sublime_plugin.TextCommand):

    """Remove empty lines."""

    def run(self, edit):
        view = self.view

        if view.size() > 0:
            reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)
            region = sublime.Region(0, view.size())

            edited_text = reobj.sub("", view.substr(region))
            view.replace(edit, region, edited_text)

        sublime.status_message('Trimmer: empty lines removed.')


class TrimLeadingCommand(sublime_plugin.TextCommand):

    """Trim leading whitespace."""

    def run(self, edit):
        view = self.view

        trim = view.find_all("^[ \t]+")
        trim.reverse()

        for r in trim:
            view.erase(edit, r)

        sublime.status_message('Trimmer: leading whitespace removed.')


class TrimmerCommand(sublime_plugin.TextCommand):

    """Trim trailing whitespace."""

    def run(self, edit):
        view = self.view

        trim = view.find_all("[\t ]+$")
        trim.reverse()

        for r in trim:
            view.erase(edit, r)

        sublime.status_message('Trimmer: trailing whitespace removed.')
