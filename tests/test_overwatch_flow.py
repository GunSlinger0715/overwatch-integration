print("=== OVERWATCH INTEGRATION TEST ===")

finding = {
    "finding": "Missing CSP Header",
    "risk": "MEDIUM"
}

print("\n[GateKeeper]")
print(finding)

message = {
    "message_id": "MSG-000001",
    "source": "GateKeeper",
    "destination": "Heimdal",
    "payload": finding
}

print("\n[Ratatoskr]")
print(message)

analysis = {
    "classification": "MISCONFIGURATION",
    "confidence": "HIGH"
}

print("\n[Heimdal]")
print(analysis)

record = {
    "finding": finding,
    "analysis": analysis
}

print("\n[Monolith]")
print("Stored")

decision = {
    "decision": "CORRECTABLE",
    "recommended_action": "ROUTE_TO_FORGE"
}

print("\n[Odin]")
print(decision)

print("\n=== FLOW COMPLETE ===")