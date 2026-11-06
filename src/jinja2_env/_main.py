from __future__ import annotations

import os
from typing import TYPE_CHECKING

from jinja2 import Environment, nodes
from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2.parser import Parser


def _get_env_default(default: str | None, key: str) -> str | None:
    return os.environ.get(key, default)


class EnvExtension(Extension):
    # a set of names that trigger the extension.
    tags: set[str] = {"env"}  # noqa: RUF012

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

        return nodes.Output([self.call_method("_run_shell", [command, rstrip])], lineno=lineno)

    def _run_shell(  # noqa: PLR6301
        self, key: str, default: str | None
    ) -> str | None:
        return os.environ.get(key, default)
