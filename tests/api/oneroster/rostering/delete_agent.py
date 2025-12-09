from timeback import Timeback
from timeback.models.request import TimebackDeleteAgentRequest


def main():
    client = Timeback()
    user_id = "44c08081-dddd-455b-89ef-88f66e5dec02"  # OLD Siyon (tobedeleted)
    agent_sourced_id = "9069005b-a061-466a-bd02-5018ac4ffd7b"  # Mom

    request = TimebackDeleteAgentRequest(
        user_id=user_id, agent_sourced_id=agent_sourced_id
    )
    result = client.oneroster.rostering.delete_agent(request)
    if result is None:
        print("Deleted (no content)")
        return
    print(f"Deleted Agent Result: {result}")


if __name__ == "__main__":
    main()
