class Handler(object):
    """
    Abstract class for handling external bibliographic databases.

    Must implement `fetch` method. Takes ID in the format expected by database,
    and returns a `dict` containing the bibliographic metadata.
    """
    requires_auth = False

    def authenticate(self, auth_key):
        raise NotImplementedError
    def fetch(self, id):
        raise NotImplementedError
