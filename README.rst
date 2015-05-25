zbmlqosc
========

Pontifications on using blosc with zmq. Warning: executable poetry ahead!

Details
-------

This is a prototype for a large-scale, ultra high-performance, massively
distributed, enterprise grade data center monitoring application. As such it is
similar in architecture to the  graphite-project.  However, it uses zmq as
transport layer and bcolz as time-series database.

Components
----------

The very nature of this software means we have multiple moving parts.

:``listener.py``: Server component that listens for data and stores it in a
                  bcolz ctable.
:``sender.py``: A sample client that sends data.
:``plotter.py``: A simple matplotlib based dashboard.

Running it
----------

In three separate shells (hint: use tmux), run:

::

    $ python server.py

::

    $ python sender.py

::

    $ python plotter.py

You should then see a sine-wave being showen by the ``plotter.py``. This is the
data being sent by ``sender.py`` to the ``listener.py``.

License
-------

Copyright © 2015 Valentin Haenel <valentin@haenel.co>

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
