from timeback import Timeback
from timeback.models.request import TimebackAddAgentRequest


def main():
    client = Timeback()

    user_id = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"
    agent_sourced_id = "agent-123-456-789"

    request = TimebackAddAgentRequest(user_id=user_id, agent_sourced_id=agent_sourced_id)
    resp = client.oneroster.rostering.add_agent(request)
    if not resp:
        print("No result")
        return

    print(f"Response: {resp.get('message', 'Agent added successfully')}")


if __name__ == "__main__":
    main()

