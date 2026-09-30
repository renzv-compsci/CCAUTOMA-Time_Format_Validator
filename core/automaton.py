TRANSITIONS = {
    "S0": {"0": "S1", "1": "S2", "2": "S3"},
    "S1": {"0": "S4", "1": "S5", "2": "S5", "3": "S5", "4": "S5", "5": "S5", "6": "S5", "7": "S5", "8": "S5", "9": "S5"},
    "S2": {"0": "S5", "1": "S5", "2": "S5", "3": "S4", "4": "S4", "5": "S4", "6": "S4", "7": "S4", "8": "S4", "9": "S4"},
    "S3": {"0": "S4", "1": "S4", "2": "S4", "3": "S4"},
    "S4": {":": "S6"},
    "S5": {":": "S7"},
    "S6": {"0": "S8", "1": "S8", "2": "S8", "3": "S8", "4": "S8", "5": "S8"},
    "S7": {"0": "S9", "1": "S9", "2": "S9", "3": "S9", "4": "S9", "5": "S9"},
    "S8": {"0": "S10", "1": "S10", "2": "S10", "3": "S10", "4": "S10", "5": "S10", "6": "S10", "7": "S10", "8": "S10", "9": "S10"},
    "S9": {"0": "S11", "1": "S11", "2": "S11", "3": "S11", "4": "S11", "5": "S11", "6": "S11", "7": "S11", "8": "S11", "9": "S11"},
    "S10": {},
    "S11": {" ": "S12"},
    "S12": {"A": "S13", "P": "S13"},
    "S13": {"M": "S10"},
    "dead": {}
}

ACCEPTING_STATES = {"S10", "S11"}
DEAD_STATE = "dead"
START_STATE = "S0"

def simulate(input_string: str) -> dict: 
    current_state = START_STATE
    trace = []

    for index, char in enumerate(input_string): 
        if current_state == DEAD_STATE: 
            next_state = DEAD_STATE
        else: 
            next_state = TRANSITIONS.get(current_state, {}).get(char, DEAD_STATE)

        trace.append({
            "step": index, 
            "char": char if char != " " else "' '",
            "from_state": current_state, 
            "to_state": next_state
        })
        current_state = next_state

    is_accepted = current_state in ACCEPTING_STATES
    return {
        "accepted": is_accepted, 
        "final_state": current_state, 
        "trace": trace 
    }