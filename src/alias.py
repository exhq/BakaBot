import json
import pathlib
import typing

aliases = {}

alias_file = pathlib.Path('aliases.json').absolute()


def load():
    global aliases
    if not alias_file.exists():
        return
    with alias_file.open() as fp:
        aliases = json.load(fp)


def save():
    with alias_file.open('w') as fp:
        json.dump(aliases, fp)


def set_alias(short_name: str, long_name: str):
    aliases[short_name] = long_name


def get_alias(short_name: str) -> typing.Optional[str]:
    return aliases.get(short_name)
