# -*- coding: utf-8 -*-

import re
import sublime
import sublime_plugin


class TrimmerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        has_matches = False

        matched_regions = view.find_all("[\t ]+$")
        matched_regions.reverse()

        for r in matched_regions:
            view.erase(edit, r)
            has_matches = True

        if has_matches:
            sublime.status_message("Trimmer: trailing whitespace removed.")
        else:
            sublime.status_message("Trimmer: no trailing whitespace found.")


class DeleteEmptyLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("^[ \t]*$\r?\n", re.MULTILINE)

        for region in self.selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub("", str_buffer)
            if str_buffer == trimmed:
                sublime.status_message("Trimmer: no empty lines to delete.")
            else:
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
        reobj = re.compile(r"[ \t\r\n\v\f]")

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
        reobj = re.compile(r"(?:\s{0,})(\r?\n)(?:\s{0,})(?:\r?\n+)")

        for region in self.selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub(r"\1\1", str_buffer)
            if str_buffer == trimmed:
                sublime.status_message("Trimmer: no lines to collapse.")
            else:
                view.replace(edit, region, trimmed)
                sublime.status_message("Trimmer: lines collapsed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class CollapseSpaces(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("([ ]{1})[ ]{1,}")

        for region in self.selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub(r"\1", str_buffer)
            if str_buffer == trimmed:
                sublime.status_message("Trimmer: no spaces to collapse.")
            else:
                view.replace(edit, region, trimmed)
                sublime.status_message("Trimmer: spaces collapsed.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class NormalizeSpaces(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("(^\\s+)|\\s(?=\\s+)|(\\s+$)")

        for region in self.selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub("", view.substr(region))
            if str_buffer == trimmed:
                sublime.status_message("Trimmer: no spaces to normalize.")
            else:
                view.replace(edit, region, trimmed)
                sublime.status_message("Trimmer: spaces normalized.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class TokenizeString(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        reobj = re.compile("^ +|( ){2,}| +$", re.MULTILINE)

        for region in self.selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub("", view.substr(region))
            if str_buffer == trimmed:
                sublime.status_message("Trimmer: nothing to tokenize.")
            else:
                view.replace(edit, region, trimmed)
                sublime.status_message("Trimmer: string tokenized.")

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


class DeleteEmptyTags(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile(r"<([A-Z][A-Z0-9]*)\b[^>]*>\s*</\1>", re.IGNORECASE)

        for region in self.selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub("", str_buffer)
            if str_buffer != trimmed:
                has_matches = True
                view.replace(edit, region, trimmed)

        if has_matches is True:
            sublime.status_message("Trimmer: empty tags deleted.")
        else:
            sublime.status_message("Trimmer: no empty tags to delete.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions


class ReplaceSmartCharactersCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        has_replacements = False

        """ Credit to MagiclessQuotes by Daryl Tucker
        (https://github.com/daryltucker/MagiclessQuotes)"""
        replacements = [
            [u'[’‘‚]', u'\''],
            [u'[“”]', u'"'],
            [u'[„]', u'"'],
            [u'[…]', u'...'],
            [u'[—]', u'---'],
            [u'[–]', u'--'],
            [u'[•]', u'*'],
            [u'[·]', u'-'],
            [u'[ ]', u'   '],
            [u'[ ]', u'  '],
            [u'[   ]', u' '],
            [u'[«]', u'<<'],
            [u'[»]', u'>>']
        ]

        for replacement in replacements:
            for region in self.selections(view):
                source_text = view.substr(region)
                if len(source_text) > 0:
                    replaced_text = re.sub(
                        replacement[0], replacement[1], source_text)
                    if source_text != replaced_text:
                        has_replacements = True
                        view.replace(edit, region, replaced_text)

        if has_replacements is True:
            sublime.status_message("Trimmer: smart characters replaced.")
        else:
            sublime.status_message("Trimmer: no smart characters to replace.")

    def selections(self, view, default_to_all=True):
        regions = [r for r in view.sel() if not r.empty()]
        if not regions and default_to_all:
            regions = [sublime.Region(0, view.size())]
        return regions
