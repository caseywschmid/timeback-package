from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "test-assessment-result-to-delete"  # Replace with actual sourcedId

    # Delete the assessment result (soft delete - sets status to 'tobedeleted')
    result = client.oneroster.gradebook.delete_assessment_result(sourced_id)
    
    if result is None:
        print(f"Assessment result {sourced_id} deleted successfully (204 No Content)")
    else:
        print(f"Assessment result deleted with response: {result}")


if __name__ == "__main__":
    main()

