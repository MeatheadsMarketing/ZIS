def format_review_report(agent_name, review_results):
    lines = [f"Review for {agent_name}:"]
    for item, status in review_results:
        lines.append(f"- {item}: {status}")
    return "\n".join(lines)