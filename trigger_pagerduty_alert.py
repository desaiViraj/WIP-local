import sys
import requests
import json

def trigger_pagerduty_alert(integration_key, description, details):
    url = "https://events.pagerduty.com/v2/enqueue"

    payload = {
        "routing_key": integration_key,
        "event_action": "trigger",
        "payload": {
            "summary": description,
            "source": "Your Application",
            "severity": "error",
            "custom_details": {
                "details": details
            }
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 202:
        print("PagerDuty incident triggered successfully.")
    else:
        print("Failed to trigger PagerDuty incident. Status code: " + str(response.status_code))
        print("Response content: " + response.text)

if __name__ == "__main__":
    integration_key = sys.argv[1]
    description = sys.argv[2]
    details = sys.argv[3]

    trigger_pagerduty_alert(integration_key, description, details)
