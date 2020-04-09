from charms.reactive import Endpoint


class KibanaProvides(Endpoint):

    def configure(self, elasticsearch_creds):
        """
        Configure the elasticsearch relation by providing:
            - elasticsearch_creds
        """

        for relation in self.relations:
            relation.to_publish.update(
                {'elasticsearch_creds': elasticsearch_creds}
            )
