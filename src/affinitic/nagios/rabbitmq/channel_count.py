# -*- coding: utf-8 -*-
"""
affinitic.nagios.rabbitmq

Licensed under the GPL license, see LICENCE.txt for more details.
"""
import nagiosplugin
from affinitic.nagios.rabbitmq.api import RabbitAdminApi

class ChannelCountCheck(nagiosplugin.Check):

    def __init__(self, optparser, logger):
        super(ChannelCountCheck, self).__init__(optparser, logger)
        optparser.add_option('-h', '--hostname', metavar='HOSTNAME',
                help='Rabbitmq hostname')

    def process_args(self, options, args):
        super(ChannelCountCheck, self).process_args(options, args)
        self.hostname = options.hostname

    def obtain_data(self):
        api = RabbitAdminApi(self.hostname, 55672, 'jfroche', 'xMLMY4MG')
        return len(api.channels)

main = nagiosplugin.Controller(ChannelCountCheck)

if __name__ == '__main__':
    main()
