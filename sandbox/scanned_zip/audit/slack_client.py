def send_slack_alert():
    import os
    return f'Slack Bot Token: {os.getenv("SLACK_BOT_TOKEN")}'