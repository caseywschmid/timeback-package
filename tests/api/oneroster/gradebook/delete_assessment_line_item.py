from timeback import Timeback


def main():
    client = Timeback()
    sourced_id = "<assessment-line-item-id>"  # Replace with actual ID

    result = client.oneroster.gradebook.delete_assessment_line_item(sourced_id)
    
    if result is None:
        print(f"Assessment line item {sourced_id} deleted (204 No Content)")
    else:
        print(f"Deleted with response: {result}")


if __name__ == "__main__":
    main()

