# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import re


class TrimmerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        matched_regions = view.find_all("[\t ]+$")
        matched_regions.reverse()

        for r in matched_regions:
            view.erase(edit, r)

        sublime.status_message("Trimmer: trailing whitespace removed.")


class DeleteEmptyLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)

        for region in self.selections(view):
            trimmed = reobj.sub("", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message("Trimmer: empty lines deleted.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class RemoveBlankSpaces(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("[ \\t\\r\\n\\v\\f]", re.MULTILINE)

        for region in self.selections(view):
            trimmed = reobj.sub("", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message("Trimmer: blanks spaces removed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class TrimLeadingWhitespaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("^[ \t]+", re.MULTILINE)

        for region in self.selections(view):
            trimmed = reobj.sub("", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message("Trimmer: leading whitespace removed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class TrimLeadingTrailingWhitespace(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("^[ \t]+|[\t ]+$", re.MULTILINE)

        for region in self.selections(view):
            trimmed = reobj.sub("", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message(
            "Trimmer: leading and trailing whitespace removed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class CollapseLines(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        re_trim_whitespace = re.compile("^[ \t]+|[\t ]+$", re.MULTILINE)
        re_extra_lines = re.compile("\\r?\\n{2,}")

        for region in self.selections(view):
            strbuffer = view.substr(region)
            strbuffer = re_trim_whitespace.sub("", strbuffer)
            strbuffer = re_extra_lines.sub("\n\n", strbuffer)
            view.replace(edit, region, strbuffer)

        sublime.status_message("Trimmer: lines collapsed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class CollapseSpaces(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("[ ]{2,}")

        for region in self.selections(view):
            trimmed = reobj.sub(" ", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message("Trimmer: spaces collapsed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class TrimEdges(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile(r"(\A\s+|\s+\Z)")

        if view.size() > 0:
            region = sublime.Region(0, view.size())
            trimmed = reobj.sub("", view.substr(region))
            view.replace(edit, region, trimmed)

        sublime.status_message("Trimmer: file edges trimmed.")


class ReplaceSmartCharactersCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view

        """ credit Daryl Tucker
        https://github.com/daryltucker/MagiclessQuotes"""
        replacements = [
            [u'[’‘]{1}', u'\''],
            [u'[“”]{1}', u'"'],
            [u'[…]{1}', u'...'],
            [u'[—]{1}', u'---'],
            [u'[–]{1}', u'--'],
            [u'[•]{1}', u'*']
        ]

        for replacement in replacements:
            x = view.find_all(replacement[0])
            for position in x:
                view.replace(edit, position, replacement[1])

        sublime.status_message("Trimmer: smart characters replaced.")
