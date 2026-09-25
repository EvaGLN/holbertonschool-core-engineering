<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Environment & First Programs

## Table of Contents :

  - [0. Interpreter Reasoning](#subparagraph0)
  - [1. Deterministic Script Output](#subparagraph1)
  - [2. Installing and Using `pycodestyle` with `pip`](#subparagraph2)
  - [3. Virtual Environment Isolation](#subparagraph3)
## Introduction & Context

Python can execute code in two primary ways:

* Interactively, using the interpreter (REPL).
* By executing a script file.

Professional software development requires understanding both execution modes, how tools are installed, and how environments influence behavior.

This project builds a structured mental model:

1. How the interpreter evaluates expressions and statements.
2. How a script differs from interactive execution.
3. How development tools are installed using `pip`.
4. Why global installations can create conflicts.
5. How virtual environments isolate dependencies.

---

## Learning Objectives

By the end of this project, you should be able to:

* Distinguish between expressions and statements in the interpreter.
* Predict when output will appear automatically in interactive mode.
* Create a portable, executable Python script.
* Install and use a development tool via `pip`.
* Explain the difference between global installations and isolated environments.
* Demonstrate dependency isolation using `venv`.

---

## Resources

* Python Tutorial — Using the Interpreter
  [https://docs.python.org/3/tutorial/interpreter.html](/rltoken/KTFsM4xolpaUmXJDFTkPUA)

* Python Standard Library — `venv`
  [https://docs.python.org/3/library/venv.html](/rltoken/nCiGtqk6wQ0qKMdzbv4CgQ)

* pip User Guide (overview)
  [https://pip.pypa.io/en/stable/user_guide/](/rltoken/1beB_SU5x7OaJiDBFqj3zA)

* pycodestyle documentation
  [https://pycodestyle.pycqa.org/](/rltoken/U3ryRAQIOJTwZ24yc0wTSQ)

---

## General Requirements

* Corrections will run on **Ubuntu 20.04 LTS**.
* Python version used for correction: **Python 3.8.x**.
* Every Python file must start exactly with:

  ```
  #!/usr/bin/env python3
  ```
* Every Python file must:
	* Be executable.
	* End with a newline.
	* Be PEP8 compliant (pycodestyle 2.7.x).
* Output must match expected formatting exactly.
* No external libraries are allowed unless explicitly requested.


## Task
### 0. Interpreter Reasoning <a name='subparagraph0'></a>

Start the Python interpreter:

```bash
python3
```

Inside the interpreter:

* Evaluate a mathematical expression.
* Assign a value to a variable.
* Enter the variable name alone.
* Use `print()` with that variable.
* Evaluate a comparison expression.

Observe carefully:

* When Python displays output automatically.
* When it does not.
* What role `print()` plays.

Reflect on why the behavior differs between expressions and statements.

You will validate your understanding through a quiz.

---

### 1. Deterministic Script Output <a name='subparagraph1'></a>

Create an executable file named `structured_output.py` that prints exactly:

```text
Language: Python
Version: 3
Pi approx: 3.14
Computation valid: True
```

Constraints:

* The float must be derived from a numeric value and formatted to two decimals.
* The boolean must result from evaluating a comparison expression.
* At least one line must use formatted string interpolation.
* No input is allowed.

Execution example:

```bash
./structured_output.py
```

The output must match exactly.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/hello_world`
* File: `structured_output.py`

---

### 2. Installing and Using `pycodestyle` with `pip` <a name='subparagraph2'></a>

`pip` is the standard tool used to install Python packages and development tools.

When you run:

```bash
pip install <package_name>
```

The package is typically installed globally for that Python installation unless a virtual environment is active.

Install `pycodestyle` using `pip`.

After installation, run:

```bash
pycodestyle structured_output.py
```

If formatting errors are reported, correct your script until no errors remain.

When installing in the sandbox, you may see a warning such as:

```vbnet
> WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead.
```

This warning appears because installing packages globally (especially as root) can affect the system Python environment.

On a personal machine, installing tools globally can:

* Create version conflicts.
* Affect other projects unexpectedly.
* Require elevated permissions.

**This motivates the use of virtual environments.**

Your understanding will be validated through a quiz.

---

### 3. Virtual Environment Isolation <a name='subparagraph3'></a>

A virtual environment is an isolated Python setup with its own interpreter and installed packages. The goal is to see, concretely, that installing a tool in one environment does not make it available in another.

The instructions below use Linux commands. On Windows, the process is similar, but activation commands differ.

### Create two environments

From the folder where you want to work, create two virtual environments:

```bash
python3 -m venv alpha_env
python3 -m venv beta_env
```

### Confirm activation changes “which Python”

Activate the first environment:

```bash
source alpha_env/bin/activate
```

Confirm the Python interpreter being used:

```bash
which python3
python3 --version
```

Expected behavior:

* `which python3` points inside `alpha_env/` (a path containing `alpha_env/bin/python3`).
* The Python version prints normally (for example, `Python 3.8.x`).

### Install a tool in only one environment

While `alpha_env` is active, install `pycodestyle`:

```bash
pip install pycodestyle
```

You may see a warning like:

> WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

What matters here:

* Packages installed with `pip` are global to the *current Python environment*.
* If a virtual environment is active, the installation is isolated to that environment.

Confirm `pycodestyle` is available:

```bash
pycodestyle --version
```

Expected behavior:

* A version number is printed (for example, `2.7.x`).

### Deactivate and switch environments

Deactivate the current environment:

```bash
deactivate
```

Confirm you are no longer using the environment interpreter:

```bash
which python3
```

Expected behavior:

* The path no longer contains `alpha_env/`.

Now activate the second environment:

```bash
source beta_env/bin/activate
```

Confirm interpreter location again:

```bash
which python3
```

Expected behavior:

* `which python3` points inside `beta_env/`.

### Verify isolation

Check whether `pycodestyle` exists in `beta_env`:

```bash
pycodestyle --version
```

Expected behavior:

* The command should fail (for example: `command not found`) **or** indicate it is not available.

This difference is the point: `pycodestyle` was installed only in `alpha_env`, so it should not appear in `beta_env`.

### Return to the first environment (switch back)

Deactivate `beta_env`:

```bash
deactivate
```

Activate `alpha_env` again:

```bash
source alpha_env/bin/activate
```

Confirm `pycodestyle` is available again:

```bash
pycodestyle --version
```

Expected behavior:

* A version number is printed again.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
