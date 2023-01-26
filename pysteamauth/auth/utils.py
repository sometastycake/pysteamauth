import base64

from google.protobuf.message import Message


def pbmessage_to_request(msg: Message) -> str:
    return str(base64.b64encode(msg.SerializeToString()), 'utf8')
