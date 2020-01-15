'''
Redfish API client used to query Dell PowerEdge server BIOS attributes
'''
import json
import requests
from requests.auth import HTTPBasicAuth
from poweredge_bios_cli.errors import BiosAttributeNotExistError


class Client:  # pylint: disable=too-few-public-methods
    '''
    The Redfish client class that interacts with the Redfish API on the server.
    '''

    def __init__(self, username, password, host, ssl_verify=True):
        self.username = username
        self.password = password
        self.host = host
        self.ssl_verify = ssl_verify
        self.uri = f'https://{host}/redfish/v1/Systems/System.Embedded.1/Bios'

    def get_bios_attributes(self, attributes=('all')):
        '''
        Get the specified BIOS attribute(s). If one or more attributes are specified,
        only return those attributes. If 'all' is specified, return all attributes.

        '''
        request = requests.get(self.uri, auth=HTTPBasicAuth(self.username, self.password),
                               verify=self.ssl_verify)
        data = json.loads(request.text)
        data = data['Attributes']

        if 'all' in attributes:
            attributes = data
            return attributes

        attributes_dict = {}
        for attribute in attributes:
            try:
                if attribute in data:
                    attributes_dict.update({attribute: data[attribute]})
                else:
                    raise BiosAttributeNotExistError
            except BiosAttributeNotExistError:
                print(f'The BIOS attribute "{attribute}" does not exist.')

        attributes = attributes_dict

        return attributes
