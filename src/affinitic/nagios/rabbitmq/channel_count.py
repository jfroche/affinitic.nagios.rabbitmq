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
        optparser.add_option('-H', '--hostname', metavar='HOSTNAME',
                help='Rabbitmq hostname')
        optparser.add_option('-w', '--warning', default='@2:3', metavar='RANGE',
                help='warning threshold (default: %default%)')
        optparser.add_option('-c', '--critical', default='@0:1', metavar='RANGE',
                help='critical threshold (default: %default%)')
        optparser.add_option('-P', '--port', default='55672', metavar='INT',
                help='RabbitMQ port')
        optparser.add_option('-u', '--user', default='guest', metavar='STRING',
                help='RabbitMQ user')
        optparser.add_option('-p', '--password', default='guest', metavar='STRING',
                help='RabbitMQ password')

    def process_args(self, options, args):
        super(ChannelCountCheck, self).process_args(options, args)
        self.warning = options.warning
        self.critical = options.critical
        self.hostname = options.hostname
        self.port = options.port
        self.username = options.user
        self.password = options.password

    def obtain_data(self):
        api = RabbitAdminApi(self.hostname, self.port, self.username, self.password)
        channelCount = len(api.channels)
        self.measures = [nagiosplugin.Measure('', channelCount, ' channels',
            self.warning, self.critical)]

main = nagiosplugin.Controller(ChannelCountCheck)

if __name__ == '__main__':
    main()
