import os
from unittest import TestCase

from jinja2 import Environment
from parameterized import parameterized_class


@parameterized_class(
    ("env", "expected"),
    [
        ("TEMP", os.environ.get("TEMP")),
        ("PATH", os.environ.get("PATH")),
        ("HOME", os.environ.get("HOME")),
        ("weh893ew82i", None),
    ],
)
class TestMain(TestCase):
    # https://jinja.palletsprojects.com/en/3.0.x/templates/
    environment: Environment
    env: str
    expected: str | None

    def setUp(self):
        self.environment = Environment(extensions=["jinja2_env.EnvExtension"])

    def test_statement(self):
        template = self.environment.from_string("{% env '" + self.env + "' %}")
        self.assertEqual(
            template.render(), self.expected if self.expected is not None else "none"
        )

    def test_statement_no_rstrip(self):
        template = self.environment.from_string("{% env '" + self.env + "', 'akdjw' %}")
        self.assertEqual(
            template.render(), self.expected if self.expected is not None else "akdjw"
        )

    def test_expression(self):
        template = self.environment.from_string(
            "{{ 'adkejf' | env('" + self.env + "') }}"
        )
        print(template.render())
        self.assertEqual(
            template.render(), self.expected if self.expected is not None else "adkejf"
        )
