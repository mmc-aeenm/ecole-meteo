#!/usr/bin/python3
# coding: utf-8


class Controller:
    def __init__(self):
        self.session = []


    def _view(self, file, **kwargs):
        with open('view/' + file + '.html', 'r') as f:
            content = f.read()
        return content.format(**kwargs)


    def _error(self, number, **kwargs):
        file = 'error/' + str(number)
        return self._view(file, **kwargs)


    def index(self):
        return self._view("index")

    def campus(self):
        return self._view("campus/site")

    def vie_associative(self):
        return self._view("vie-associative/annee")

