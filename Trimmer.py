import sublime
import sublime_plugin
import re


class DeleteEmptyLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message("Trimmer: empty lines deleted.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimLeadingWhitespaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]+", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message("Trimmer: leading whitespace removed.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimLeadingTrailingWhitespace(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("^[ \t]+|[\t ]+$", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub("", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message(
            "Trimmer: leading and trailing whitespace removed.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class CollapseEmptyLines(sublime_plugin.TextCommand):

    def run(self, edit):
        reobj = re.compile("(\r?\n){3,}", re.MULTILINE)
        selections = self.get_selections()

        for sel in selections:
            trimmed = reobj.sub(r"\1\1", self.view.substr(sel))
            self.view.replace(edit, sel, trimmed)

        sublime.status_message(
            "Trimmer: empty lines collapsed.")

    def get_selections(self):
        selections = self.view.sel()

        has_selections = False
        for sel in selections:
            if sel.empty() is False:
                has_selections = True

        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections


class TrimEdges(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        if view.size() > 0:
            region = sublime.Region(0, view.size())
            trimmed = re.sub("(\\A\\s+|\\s+\\Z)", "", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message('Trimmer: file edges trimmed.')


class TrimmerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        matched_regions = view.find_all("[\t ]+$")
        matched_regions.reverse()

        for r in matched_regions:
            view.erase(edit, r)

        sublime.status_message("Trimmer: trailing whitespace removed.")
