import sublime
import sublime_plugin
import re


class TrimBothCommand(sublime_plugin.TextCommand):

    """Remove leading and trailing whitespace."""

    def run(self, edit):
        view = self.view

        trim = view.find_all("^[ \t]+|[ \t]+$")
        trim.reverse()

        for r in trim:
            view.erase(edit, r)

        sublime.status_message(
            'Trimmer: leading and trailing whitespace removed.')


class TrimBottomCommand(sublime_plugin.TextCommand):

    """Remove whitespace from the end of the file."""

    def run(self, edit):
        view = self.view

        if view.size() > 0:
            eofc = "\n" if view.settings().get(
                "ensure_newline_at_eof_on_save") is True else ""
            region = sublime.Region(0, view.size())

            edited_text = re.sub(
                r"(?m)[\s]*$(?![\w\W])", eofc, view.substr(region))
            view.replace(edit, region, edited_text)

        sublime.status_message('Trimmer: bottom whitespace removed.')


class TrimTopCommand(sublime_plugin.TextCommand):

    """Remove whitespace from the top of the file."""

    def run(self, edit):
        view = self.view

        if view.size() > 0:
            region = sublime.Region(0, view.size())
            edited_text = re.sub(r"\A\s+", "", view.substr(region))
            view.replace(edit, region, edited_text)

        sublime.status_message('Trimmer: top whitespace removed.')


class TrimEmptyCommand(sublime_plugin.TextCommand):

    """Remove empty lines."""

    def run(self, edit):
        reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)

        selections = self.get_selections()

        for sel in selections:
            edited_text = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, edited_text)

        sublime.status_message('Trimmer: empty lines removed.')

    def get_selections(self):
        selections = self.view.sel()

        # check for selections
        has_selections = False
        for region in selections:
            if region.empty() is False:
                has_selections = True

        # if no selections, use the file as selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimLeftCommand(sublime_plugin.TextCommand):

    """Remove leading whitespace."""

    def run(self, edit):
        reobj = re.compile("^[ \t]+", re.MULTILINE)

        selections = self.get_selections()

        for sel in selections:
            edited_text = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, edited_text)

        sublime.status_message('Trimmer: leading whitespace removed.')

    def get_selections(self):
        selections = self.view.sel()

        # check for selections
        has_selections = False
        for region in selections:
            if region.empty() is False:
                has_selections = True

        # if no selections, use the file as selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimmerCommand(sublime_plugin.TextCommand):

    """Remove trailing whitespace."""

    def run(self, edit):
        view = self.view

        trim = view.find_all("[\t ]+$")
        trim.reverse()

        for r in trim:
            view.erase(edit, r)

        sublime.status_message('Trimmer: trailing whitespace removed.')
