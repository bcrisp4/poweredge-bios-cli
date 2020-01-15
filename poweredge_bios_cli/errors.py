'''
PowerEdge BIOS CLI exceptions
'''


class Error(Exception):
    '''
    Base error
    '''


class BiosAttributeNotExistError(Error):
    '''
    Raised when requested BIOS attribute does not exist in the collection of
    attributes returned by the Redfish API.
    '''
