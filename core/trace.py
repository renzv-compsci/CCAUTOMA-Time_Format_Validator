def format_trace_table(trace_data: list) -> list[dict]: 
    formatted = []
    for step in trace_data: 
        formatted.append({
            "Step": step["step"], 
            "Read Symbol": step["char"], 
            "Current State": step["from_state"], 
            "Next State": step["to_state"]
        })
    return formatted

def get_trace_summary(final_state: str, is_accepted: bool) -> str: 
    if is_accepted:
        return f"The automaton successfully reached accepting state {final_state}. The string is in L_TIME."
    else:
        if final_state == "dead":
            return "The automaton transitioned to the dead state. The string violates the structural rules of L_TIME."
        else:
            return f"The automaton halted in non-accepting state {final_state}. The input was incomplete."