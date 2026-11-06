# jinja2-env

<p align="center">
  <a href="https://github.com/34j/jinja2-env/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/34j/jinja2-env/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://jinja2-env.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/jinja2-env.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
</p>
<p align="center">
  <a href="https://codecov.io/gh/34j/jinja2-env">
    <img src="https://img.shields.io/codecov/c/github/34j/jinja2-env.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/j178/prek">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json" alt="prek">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/jinja2-env/">
    <img src="https://img.shields.io/pypi/v/jinja2-env.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/jinja2-env.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/jinja2-env.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://jinja2-env.readthedocs.io" target="_blank">https://jinja2-env.readthedocs.io </a>

**Source Code**: <a href="https://github.com/34j/jinja2-env" target="_blank">https://github.com/34j/jinja2-env </a>

---

Jinja2 Extension for getting eval() result.

## Installation

Install this via pip (or your favourite package manager):

```shell
pip install jinja2-env
```

## Usage

The extension class is `jinja2_env.EnvExtension`.

As a statement:

```text
{% env "HOME" %}
{% env "HOME", default %}
```

As a expression:

```text
{{ "default" | env("HOME") }}
```
