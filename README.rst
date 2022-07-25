.. |pic1| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue
.. |pic2| image:: https://img.shields.io/github/license/mashape/apistatus.svg
.. |pic3| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. |pic4| image:: https://img.shields.io/badge/%20type_checker-mypy-%231674b1?style=flat
.. |pic5| image:: https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey
.. |pic6| image:: https://github.com/AndresAlgaba/pytemppack/actions/workflows/testing.yml/badge.svg
.. |pic7| image:: https://img.shields.io/readthedocs/pytemppack
.. |pic8| image:: https://img.shields.io/pypi/v/pytemppack

.. _pytemppack: https://github.com/AndresAlgaba/pytemppack/tree/main/pytemppack
.. _examples: https://github.com/AndresAlgaba/pytemppack/tree/main/examples
.. _contribute: https://github.com/AndresAlgaba/pytemppack/blob/main/CONTRIBUTING.rst

.. _poetry: https://python-poetry.org/docs/
.. _pip: https://mypy.readthedocs.io/en/stable/config_file.html#the-mypy-configuration-file

.. _bandit: https://bandit.readthedocs.io/en/latest/
.. _black: https://black.readthedocs.io/en/stable/index.html
.. _pytest: https://docs.pytest.org/en/stable/index.html
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/stable/index.html
.. _mypy: https://mypy.readthedocs.io/en/stable/index.html
.. _shields: https://shields.io/
.. _README: https://www.makeareadme.com/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _Read the Docs: https://readthedocs.org/
.. _isort: https://pycqa.github.io/isort/index.html
.. _templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates

.. _changelog: https://keepachangelog.com/en/1.0.0/
.. _code of conduct: https://www.contributor-covenant.org/version/1/4/code-of-conduct/

.. _Twitter: https://twitter.com/DataLabBE
.. _website: https://data.research.vub.be/
.. _papers: https://researchportal.vub.be/en/organisations/data-analytics-laboratory/publications/

.. _repo: https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion

.. _Dynamic versioning: https://pypi.org/project/poetry-dynamic-versioning/


pytemppack
==========

|pic2| |pic5| |pic1| |pic8|

|pic6| |pic7| |pic3| |pic4|

This is a template for Python packages with `poetry`_ with additional tools for development, such as autoformatting, type checking, and more.

The `pytemppack`_ folder contains the python module, and we have some `examples`_.

As best practices are always changing, and people have different experiences, we encourage you to `contribute`_ to this project!


Features
--------

* Arranging imports with `isort`_.
* Autoformatting with `black`_.
* Boilerplate `README`_ with `shields`_.
* Documentation with `Sphinx`_ and `Read the Docs`_.
* Issue and pull request `templates`_.
* Templates for `changelog`_, `code of conduct`_ and `contribute`_.
* Testing with `pytest`_ and coverage with `pytest-cov`_.
* Security scanning with `Bandit`_.
* Static type-checking with `mypy`_.


TODO
----

* `Dynamic versioning`_.


Installation
------------

Use the package manager `pip`_ to install ``pytemppack`` from PyPi.

.. code-block:: bash

    pip install pytemppack

For development install, see `contribute`_.


Usage
-----

Transform a ``np.ndarray`` into a ``pd.DataFrame``.

.. code-block:: python

    from pytemppack import PyPack
    from pytemppack.utils import generate_random_array

    data = generate_random_array((5, 5))
    columns = ['a', 'b', 'c', 'd', 'e']

    pypack = PyPack(data)
    pypack.transform_results(columns)

    pypack.results.head()

            a	            b	            c	            d	            e
    0	0.976700	0.118091	0.441006	0.659874	0.060139
    1	0.380196	0.241766	0.609871	0.735758	0.683689
    2	0.923246	0.318534	0.863621	0.222754	0.671238
    3	0.261692	0.964079	0.863758	0.172066	0.611018
    4	0.319097	0.263650	0.674881	0.870415	0.060137


Community
---------

If you are interested in cross-disciplinary research related to machine learning, you can:

* Follow DataLab on `Twitter`_.
* Check the `website`_.
* Read our `papers`_.


Disclaimer
----------

The package and the code is provided "as-is" and there is NO WARRANTY of any kind. 
Use it only if the content and output files make sense to you.


Acknowledgements
----------------

This `repo`_ was a great help for autosummary recurssion to document the API.
