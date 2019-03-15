from SmartAPI.common.PROPERTY import PROPERTY
from SmartAPI.common.RESOURCE import RESOURCE
from SmartAPI.common.Tools import Tools
from SmartAPI.rdf.Resource import Resource
from SmartAPI.model.Message import Message

from SmartAPI.smartapiexceptions.NonePointerException import NonePointerException

import traceback

class Notification(Message):

	def __init__(self, uri = None):
		Message.__init__(self, uri)
		self.setType(RESOURCE.NOTIFICATION)
			
	@classmethod
	def fromString(cls, data, serialization):
		try:
			return cls.parse(Tools().getResourceByType(RESOURCE.NOTIFICATION, Tools().fromString(data, serialization)))
		except:
			print "Unable to parse Notification from the given string."
			traceback.print_exc()
			return None
