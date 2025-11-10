from timeback import Timeback
from timeback.models.request import TimebackDeleteAgentRequest


def main():
	client = Timeback()
	user_id = "02d5c525-1755-4572-aae6-a30b8e89af79"
	agent_sourced_id = "test.account8@alpha.school"

	request = TimebackDeleteAgentRequest(user_id=user_id, agent_sourced_id=agent_sourced_id)
	result = client.oneroster.rostering.delete_agent(request)
	if result is None:
		print("Deleted (no content)")
		return
	print(f"Deleted Agent Result: {result}")


if __name__ == "__main__":
	main()
