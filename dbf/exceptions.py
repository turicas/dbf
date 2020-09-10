# warnings and errors

class DbfError(Exception):
    """
    Fatal errors elicit this response.
    """
    def __init__(self, message, *args):
        Exception.__init__(self, message, *args)
        self.message = message


class DataOverflowError(DbfError):
    """
    Data too large for field
    """
    def __init__(self, message, data=None):
        DbfError.__init__(self, message)
        self.data = data


class BadDataError(DbfError):
    """
    bad data in table
    """
    def __init__(self, message, data=None):
        DbfError.__init__(self, message)
        self.data = data


class FieldMissingError(KeyError, DbfError):
    """
    Field does not exist in table
    """
    def __init__(self, fieldname):
        KeyError.__init__(self, '%s:  no such field in table' % fieldname)
        DbfError.__init__(self, '%s:  no such field in table' % fieldname)
        self.data = fieldname


class FieldSpecError(DbfError, ValueError):
    """
    invalid field specification
    """
    def __init__(self, message):
        ValueError.__init__(self, message)
        DbfError.__init__(self, message)


class NonUnicodeError(DbfError):
    """
    Data for table not in unicode
    """
    def __init__(self, message=None):
        DbfError.__init__(self, message)


class NotFoundError(DbfError, ValueError, KeyError, IndexError):
    """
    record criteria not met
    """
    def __init__(self, message=None, data=None):
        ValueError.__init__(self, message)
        KeyError.__init__(self, message)
        IndexError.__init__(self, message)
        DbfError.__init__(self, message)
        self.data = data


class DbfWarning(Exception):
    """
    Normal operations elicit this response
    """


class Eof(DbfWarning, StopIteration):
    """
    End of file reached
    """
    message = 'End of file reached'

    def __init__(self):
        StopIteration.__init__(self, self.message)
        DbfWarning.__init__(self, self.message)


class Bof(DbfWarning, StopIteration):
    """
    Beginning of file reached
    """
    message = 'Beginning of file reached'

    def __init__(self):
        StopIteration.__init__(self, self.message)
        DbfWarning.__init__(self, self.message)


class DoNotIndex(DbfWarning):
    """
    Returned by indexing functions to suppress a record from becoming part of the index
    """
    message = 'Not indexing record'

    def __init__(self):
        DbfWarning.__init__(self, self.message)


class FieldNameWarning(UserWarning):
    message = 'non-standard characters in field name'


