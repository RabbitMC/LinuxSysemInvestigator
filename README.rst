LinuxSystemInvestigator
========================

*Generic* Linux System Investigator Kit written in Python.

It will produce following information in JSON file:

Computer

- Name

- OS
  - Version
  - Bit Version

- Logged In User
  - Name

- CPU
  - Name
  - Vendor
  - Speed
  - #Core (logical)
  - #Core
- Memory

  - logical
  - virtual
- Disks

  - Name
  - Path (/dev/fd0)
  - Size
  - Partitions
- Network Card Adapters

  - IP
  - Mac

### extern / submodules

- psutil_

.. _psutil: http://www.python.org/

#### src:

- RST-Quickref_

.. _RST-Quickref: http://docutils.sourceforge.net/docs/user/rst/quickref.html
