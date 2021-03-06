.. _installation:

Installation
============

PynPoint is compatible with Python 3.6 and 3.7. Earlier versions (up to v0.7.0) are also compatible with Python 2.7. We highly recommend using Python 3 since several key Python projects have already |python| Python 2.

Virtual Environment
-------------------

<<<<<<< HEAD
PynPoint is available in the |pypi| and on |github|. We recommend using a Python virtual environment to install and run PynPoint such that the correct versions of the dependencies can be installed without affecting other installed Python packages. First install `virtualenv`, for example with the |pip|::

    $ pip install virtualenv

Then create a virtual environment for Python 3::

    $ virtualenv -p python3 folder_name

And activate the environment with::

    $ source folder_name/bin/activate

A virtual environment can be deactivated with::
=======
PynPoint is available in the |pypi| and on |github|. We recommend using a Python virtual environment to install and run PynPoint such that the correct versions of the dependencies can be installed without affecting other installed Python packages. First install `virtualenv`, for example with the |pip|:

.. code-block:: console

    $ pip install virtualenv

Then create a virtual environment for Python 3:

.. code-block:: console

    $ virtualenv -p python3 folder_name

And activate the environment with:

.. code-block:: console

    $ source folder_name/bin/activate

A virtual environment can be deactivated with:

.. code-block:: console
>>>>>>> upstream/master

    $ deactivate

.. important::
   Make sure to adjust the path where the virtual environment is installed and activated.

Installation from PyPI
----------------------

<<<<<<< HEAD
PynPoint can now be installed with pip::

    $ pip install pynpoint

If you do not use a virtual environment then you may have to add the ``-- user`` argument::

    $ pip install --user pynpoint

PynPoint is actively being developed. To update the installation to the latest version::
=======
PynPoint can now be installed with pip:

.. code-block:: console

    $ pip install pynpoint

If you do not use a virtual environment then you may have to add the ``--user`` argument:

.. code-block:: console

    $ pip install --user pynpoint

PynPoint is actively being developed. To update the installation to the latest version:

.. code-block:: console
>>>>>>> upstream/master

   $ pip install --upgrade PynPoint

.. _installation_github:

Installation from Github
------------------------

<<<<<<< HEAD
The repository can also be cloned from Github, which contains the most recent implementations::

    $ git clone git@github.com:PynPoint/PynPoint.git

In that case, the dependencies can be installed from the PynPoint folder::

    $ pip install -r requirements.txt

By adding the path of the repository to the ``PYTHONPATH`` environment variable enables PynPoint to be imported from any location::
=======
The repository can also be cloned from Github, which contains the most recent implementations:

.. code-block:: console

    $ git clone git@github.com:PynPoint/PynPoint.git

In that case, the dependencies can be installed from the PynPoint folder:

.. code-block:: console

    $ pip install -r requirements.txt

And to update the dependencies to the latest versions with which PynPoint is compatible:

.. code-block:: console

    $ pip install --upgrade -r requirements.txt 

By adding the path of the repository to the ``PYTHONPATH`` environment variable enables PynPoint to be imported from any location:

.. code-block:: console
>>>>>>> upstream/master

    $ echo "export PYTHONPATH='$PYTHONPATH:/path/to/pynpoint'" >> folder_name/bin/activate

.. important::
   Make sure to adjust local path in which PynPoint will be cloned from the Github repository.

Do you want to makes changes to the code? Then please fork the PynPoint repository on the Github page and clone your own fork instead of the main repository. We very much welcome active contributions and pull requests (see :ref:`contributing` section).

Testing Pynpoint
----------------

<<<<<<< HEAD
The installation can be tested by starting Python in interactive mode and printing the PynPoint version::
=======
The installation can be tested by starting Python in interactive mode and printing the PynPoint version:

.. code-block:: python
>>>>>>> upstream/master

    >>> import pynpoint
    >>> pynpoint.__version__

.. tip::
<<<<<<< HEAD
   If the PynPoint package is not find by Python then possibly the path was not set correctly. The list of folders that are searched by Python for modules can be printed in interactive mode as::

      >>> import sys
      >>> sys.path
=======
   If the PynPoint package is not find by Python then possibly the path was not set correctly. The list of folders that are searched by Python for modules can be printed in interactive mode as:

      .. code-block:: python

         >>> import sys
         >>> sys.path
>>>>>>> upstream/master

   The result should contain the folder in which the Github repository was cloned or the folder in which Python modules are installed with pip.

.. |python| raw:: html

   <a href="https://python3statement.org/" target="_blank">stopped supporting</a>

.. |pypi| raw:: html

   <a href="https://pypi.org/project/pynpoint/" target="_blank">PyPI repository</a>

.. |github| raw:: html

   <a href="https://github.com/PynPoint/PynPoint" target="_blank">Github</a>

.. |pip| raw:: html

   <a href="https://packaging.python.org/tutorials/installing-packages/" target="_blank">pip package manager</a>
