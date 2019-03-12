# -*- coding: utf-8 -*-

import re
import sublime
import sublime_plugin


def selections(view, default_to_all=True):
    regions = [r for r in view.sel() if not r.empty()]
    if not regions and default_to_all:
        regions = [sublime.Region(0, view.size())]
    return regions


class TrimmerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False

        regions = view.find_all('[\t ]+$')
        regions.reverse()
        for region in regions:
            view.erase(edit, region)
            has_matches = True

        if has_matches:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: trailing whitespace removed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no trailing whitespace found.'), 0)


class DeleteEmptyLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile('^[ \t]*$\r?\n', re.MULTILINE)

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: empty lines deleted.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no empty lines to delete.'), 0)


class RemoveBlankSpaces(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile(r'[ \t\r\n\v\f]')

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: blanks spaces removed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no blank spaces to remove.'), 0)


class TrimLeadingWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile('^[ \t]+', re.MULTILINE)

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: leading whitespace removed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no leading whitespace to remove.'), 0)


class TrimLeadingTrailingWhitespace(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile('^[ \t]+|[\t ]+$', re.MULTILINE)

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: leading and trailing whitespace removed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no leading or trailing whitespace to remove.'), 0)


class CollapseLines(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile(r'(?:\s*)(\r?\n)(?:\s*)(?:\r?\n+)')

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub(r'\1\1', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: lines collapsed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no lines to collapse.'), 0)


class CollapseSpaces(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile('([ ])[ ]+')

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub(r'\1', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: spaces collapsed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no spaces to collapse.'), 0)


class NormalizeSpaces(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile('(^\\s+)|\\s(?=\\s+)|(\\s+$)')

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: spaces normalized.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no spaces to normalize.'), 0)


class TokenizeString(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile('^ |\t+|( ){2,}|\t| |\t+$', re.MULTILINE)

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: string tokenized.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: nothing to tokenize.'), 0)


class TrimEdges(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile(r'(\A\s+|\s+\Z)')

        if view.size() > 0:
            region = sublime.Region(0, view.size())
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            return sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: file edges trimmed.'), 0)
        else:
            return sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no file edges to trim.'), 0)


class DeleteEmptyTags(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False
        reobj = re.compile(r'<([A-Z][A-Z0-9]*)\b[^>]*>\s*</\1>', re.IGNORECASE)

        for region in selections(view):
            str_buffer = view.substr(region)
            trimmed = reobj.sub('', str_buffer)
            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: empty tags deleted.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no empty tags to delete.'), 0)


class TrimSelections(sublime_plugin.TextCommand):
    def run(self, edit):
        """
        Trim leading and trailing whitespace from selections.

        Originally from the 'Multi​Edit​Utils' Plug-in
        https://github.com/philippotto/Sublime-MultiEditUtils
        """
        view = self.view
        selection = view.sel()
        new_regions = []

        for current_region in selection:
            text = view.substr(current_region)

            l_stripped_text = text.lstrip()
            r_stripped_text = l_stripped_text.rstrip()

            l_stripped_count = len(text) - len(l_stripped_text)
            r_stripped_count = len(l_stripped_text) - len(r_stripped_text)

            a = current_region.begin() + l_stripped_count
            b = current_region.end() - r_stripped_count

            if a == b:
                # the region only contained whitespace
                # use the old selection end to avoid jumping of cursor
                a = b = current_region.b

            new_regions.append(sublime.Region(a, b))

        selection.clear()
        for region in new_regions:
            selection.add(region)

        sublime.set_timeout(lambda: sublime.status_message(
            'Trimmer: selections trimmed.'), 0)


class RemoveComments(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False

        re_single_line_comment = re.compile(r"//.*$", re.MULTILINE)
        re_hash_comment = re.compile("#[^!].*$", re.MULTILINE)
        re_html_comment = re.compile("<!--.*?-->", re.DOTALL)
        re_block_comment = re.compile(r"/\*.*?\*/", re.DOTALL)
        re_ini_comment = re.compile(r"^(?:\s+)?;.*$", re.MULTILINE)

        for region in selections(view):
            str_buffer = view.substr(region)

            #
            # TODO: re-work this brute force approach and filter by syntax/scope
            trimmed = re_single_line_comment.sub('', str_buffer)
            trimmed = re_hash_comment.sub('', trimmed)
            trimmed = re_html_comment.sub('', trimmed)
            trimmed = re_block_comment.sub('', trimmed)
            trimmed = re_ini_comment.sub('', trimmed)

            if str_buffer != trimmed:
                view.replace(edit, region, trimmed)
                has_matches = True

        if has_matches is True:
            view.run_command('collapse_lines')
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: comments removed.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no comments to remove.'), 0)


class ReplaceSmartCharactersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        has_matches = False

        smart_replacements = [
            [u'[’‘′‚]', u'\''],
            [u'[“”″]', u'"'],
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
            [u'[»]', u'>>'],
            [u'[©]', u'(C)'],
            [u'[®]', u'(R)'],
            [u'[™]', u'(TM)']
        ]

        for replacement in smart_replacements:
            for region in selections(view):
                source_text = view.substr(region)
                if len(source_text) > 0:
                    replaced_text = re.sub(
                        replacement[0], replacement[1], source_text)
                    if source_text != replaced_text:
                        view.replace(edit, region, replaced_text)
                        has_matches = True

        if has_matches is True:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: smart characters replaced.'), 0)
        else:
            sublime.set_timeout(lambda: sublime.status_message(
                'Trimmer: no smart characters to replace.'), 0)
