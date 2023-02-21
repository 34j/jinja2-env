from __future__ import annotations

import os

from jinja2 import Environment, nodes
from jinja2.ext import Extension
from jinja2.parser import Parser


def _get_env_default(default: str | None, key: str) -> str | None:
    return os.environ.get(key, default)


class EnvExtension(Extension):
    # a set of names that trigger the extension.
    tags = {"env"}

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)
        environment.filters["env"] = _get_env_default

    def parse(self, parser: Parser) -> nodes.Output:
        lineno = next(parser.stream).lineno

        command = parser.parse_expression()

        if parser.stream.skip_if("comma"):
            rstrip = parser.parse_expression()
        else:
            rstrip = nodes.Const("none")

        return nodes.Output(
            [self.call_method("_run_shell", [command, rstrip])], lineno=lineno
        )

    def _run_shell(self, key: str, default: str | None) -> str | None:
        return os.environ.get(key, default)
