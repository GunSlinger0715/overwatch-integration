import sys

sys.path.append("../gatekeeper-api-security-testing")
sys.path.append("../overwatch-ratatoskr")
sys.path.append("../overwatch-heimdal")
sys.path.append("../overwatch-monolith")

from core.validator import validate_target
from messages.messages import create_message
from intelligence.interpreter import interpret_message
from storage.storage_manager import (save_record)


target = "https://example.com"

validated_target = validate_target(target)

message = create_message(
    source="GateKeeper",
    destination="Heimdal",
    message_type="TARGET",
    payload=validated_target,
    
)

analysis = interpret_message(message)

save_record(analysis)

print("\nMESSAGE:")
print(message)

print("\nANALYSIS:")
print(analysis)

print("\nMONOLITH:")
print("Record stored successfully")