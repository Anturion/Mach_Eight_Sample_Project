## Mach Eight Sample Project

This project is built on python 3.9.6 version

### Creation of `.venv`

Virtual environments are just as easy to create as when using Conda, there are
only some slightly differences. We will asume the usage of Python 3, as the
library is intended to work on this version. Most Python installation use
`python3` as the command to execute processes within Python 3, but there are
some Linux distribution that prefer the usage of `python`, such as:
* Arch Linux
* Manjaro
* Gentoo

If you are not using any of the previously mentioned distros, then do as follows
(Otherwise change `python3` -> `python`):

```shell
python3 -m venv env
```
This creates a virtual environment on the folder we mentioned previously, after
that we need to activate it so that the prompt has access to it whenever needed.
This gets done by executing:

```shell
src .venv/bin/activate
```

on Linux/Mac, or

```shell
.venv\Scripts\activate.bat
```

on Windows.

---

### Installation of required libraries

Now, in order to use the app, we need to install all of the required
for this purpose just type:

```shell
pip install -r requirements.txt
```

### Run the app:

Now we are ready to run our application, for this we simply write

```shell
python manage.py
```

### Run the test:

The tests of the application were made with the help of pytest, 
therefore to run them you just have to type

```shell
pytest
```
