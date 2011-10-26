# -*- coding: utf-8 -*-
import json
import urllib2


class RabbitAdminApi(object):

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        auth_handler = urllib2.HTTPBasicAuthHandler()
        auth_handler.add_password(realm='RabbitMQ Management',
                uri='http://%s:%s' % (self.hostname, self.port),
                user=self.username,
                passwd=self.password)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)

    def _request(self, name):
        url = 'http://%s:%s/api/%s' % (self.hostname, self.port, name)
        response = urllib2.urlopen(url)
        return json.loads(response.read())

    @property
    def channels(self):
        return self._request('channels')

    @property
    def queues(self):
        return self._request('queues')
