from timeback import Timeback


def main():
    client = Timeback()
    result = client.oneroster.resources.delete_resource("<resource-id>")
    
    if result is None:
        print("Deleted successfully")
    else:
        print(f"Deleted with response: {result}")


if __name__ == "__main__":
    main()

