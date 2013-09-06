Libcloud DNS Zone to BIND zone
==============================

Python module which allows you to export `Libcloud`_ DNS zone from any of the
supported providers to the BIND zone file format.

Note: Generated BIND zone file content doesn't contain ``SOA`` and ``NS``
records. This should work fine if you just want to import this file using
a DNS provider web interface, but if you want to use it with BIND you need
to manually add those records.

Usage
=====

For usage example, see ``example.py`` file.

License
-------

Package is distributed under the `Apache 2.0 license`_.

.. _`Libcloud`: https://libcloud.apache.org/
.. _`Apache 2.0 license`: https://www.apache.org/licenses/LICENSE-2.0.html
