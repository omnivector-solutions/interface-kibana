from charms.reactive import when
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class KibanaRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['elasticsearch_creds'] for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        if any(unit.received['elasticsearch_creds'] for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    def list_unit_data(self):
        """
        Get the list of the relation info for each unit.

        Returns a list of dicts, where each dict contains the elasticsearch
        cluster name, the host (address) and the port (as a string).
        For example::
            [
                {
                    'host': '10.1.1.1',
                    'port': '80',
                    'cluster_name': "elasticsearch"
                },
            ]
        """
        units_data = []
        for relation in self.relations:
            for unit in relation.joined_units:
                elasticsearch_creds = unit.received['elasticsearch_creds']
                if not elasticsearch_creds:
                    continue
                ctxt = {'elasticsearch_creds':  elasticsearch_creds}
                units_data.append(ctxt)
        return units_data
