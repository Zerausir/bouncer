"""
Datastore models
"""

from google.cloud import ndb


class Redirect(ndb.Model):
    """Redirect model."""
    name = ndb.StringProperty()
    destination_url = ndb.StringProperty()
    created_on = ndb.DateProperty(auto_now_add=True)
    