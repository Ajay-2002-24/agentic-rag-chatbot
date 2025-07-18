# mcp/context_protocol.py
import uuid
from datetime import datetime

def create_mcp_message(sender, receiver, type_, payload, trace_id=None):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": type_,
        "trace_id": trace_id or str(uuid.uuid4()),
        "timestamp": str(datetime.now()),
        "payload": payload
    }
