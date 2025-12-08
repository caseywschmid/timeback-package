from timeback import Timeback
from timeback.models.request import TimebackAddAgentRequest


def main():
    client = Timeback()

    user_id = "975f0849-8f4e-423f-9560-1b94af66b59e"
    agent_sourced_id = "9069005b-a061-466a-bd02-5018ac4ffd7b"

    request = TimebackAddAgentRequest(user_id=user_id, agent_sourced_id=agent_sourced_id)
    resp = client.oneroster.rostering.add_agent(request)
    if not resp:
        print("No result")
        return

    print(f"Response: {resp.get('message', 'Agent added successfully')}")


if __name__ == "__main__":
    main()

