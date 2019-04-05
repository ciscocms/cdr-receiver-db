from collections import OrderedDict


class Cdr(object):
    """Base CDR class"""
    def __init__(self, *cdr):
        for d in cdr:
            for key in d:
                setattr(self, key, d[key])

    def __str__(self):
        return "I am a {} message".format(type(self).__name__)

class callStart(Cdr):
    """CDR call start object"""
    def __init__(self, *cdr):
        super(callStart, self).__init__(*cdr)


class callLegStart(Cdr):
    """CDR call leg start object"""
    def __init__(self, *cdr):
        super(callLegStart, self).__init__(*cdr)


class callLegUpdate(Cdr):
    """CDR call leg update object"""
    def __init__(self, *cdr):
        super(callLegUpdate, self).__init__(*cdr)


class callLegEnd(Cdr):
    """CDR call leg end object"""
    def __init__(self, *cdr):
        super(callLegEnd, self).__init__(*cdr)


class callEnd(Cdr):
    """CDR call end object"""
    def __init__(self, *cdr):
        super(callEnd, self).__init__(*cdr)


class recordingStart(Cdr):
    """CDR recording start object"""
    def __init__(self, *cdr):
        super(recordingStart, self).__init__(*cdr)


class recordingEnd(Cdr):
    """CDR recording end object"""
    def __init__(self, *cdr):
        super(recordingEnd, self).__init__(*cdr)


class streamingStart(Cdr):
    """CDR streaming start object"""
    def __init__(self, *cdr):
        super(streamingStart, self).__init__(*cdr)


class streamingEnd(Cdr):
    """CDR streaming end object"""
    def __init__(self, *cdr):
        super(streamingEnd, self).__init__(*cdr)
