# mod_speedtest/neubot_module.py

#
# Copyright (c) 2013
#     Nexa Center for Internet & Society, Politecnico di Torino (DAUIN)
#     and Simone Basso <bassosimone@gmail.com>
#
# This file is part of Neubot <http://www.neubot.org/>.
#
# Neubot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Neubot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Neubot.  If not, see <http://www.gnu.org/licenses/>.
#

""" The entry point of the Speedtest module """

import logging
from ..lib_net.poller import POLLER
from .. import mod_speedtest
def _run_test(message):
    """ Run the Speedtest test """
    raise RuntimeError("Not implemented")

def mod_load(context, message):
    """ Invoked when the module loads """
    logging.debug("speedtest: init for context '%s'... in progress", context)

    if context == "server":

        negotiate_server = message["negotiate_server"]
        http_server = message["http_server"]

        logging.debug("speedtest: register negotiate server module... in progress")

        conf = message["configuration"]
        mod_speedtest.wrapper.run(POLLER, conf)

    logging.debug("speedtest: init for context '%s'... complete", context)
