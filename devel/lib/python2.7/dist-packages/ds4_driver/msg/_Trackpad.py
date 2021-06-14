# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ds4_driver/Trackpad.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Trackpad(genpy.Message):
  _md5sum = "7f8d46ab2334dfb3664bed321f9eaf05"
  _type = "ds4_driver/Trackpad"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Trackpad message for DualShock 4
uint16 id       # Touch ID (increments every touch)
int32 active    # 0: inactive, 1: active
float32 x       # 0.0: left edge, 1.0: right edge
float32 y       # 0.0: left edge, 1.0: right edge
"""
  __slots__ = ['id','active','x','y']
  _slot_types = ['uint16','int32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,active,x,y

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Trackpad, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.active is None:
        self.active = 0
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
    else:
      self.id = 0
      self.active = 0
      self.x = 0.
      self.y = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_Hi2f().pack(_x.id, _x.active, _x.x, _x.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.id, _x.active, _x.x, _x.y,) = _get_struct_Hi2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_Hi2f().pack(_x.id, _x.active, _x.x, _x.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.id, _x.active, _x.x, _x.y,) = _get_struct_Hi2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Hi2f = None
def _get_struct_Hi2f():
    global _struct_Hi2f
    if _struct_Hi2f is None:
        _struct_Hi2f = struct.Struct("<Hi2f")
    return _struct_Hi2f
