class PydubException(Exception):
    pass

class TooManyMissingFrames(PydubException):
    pass

class InvalidDuration(PydubException):
    pass

class InvalidTag(PydubException):
    pass

class InvalidID3TagVersion(PydubException):
    pass

class CouldntDecodeError(PydubException):
    pass

class CouldntEncodeError(PydubException):
    pass

class MissingAudioParameter(PydubException):
    pass
