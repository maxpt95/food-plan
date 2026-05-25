import time


def menu():
    while True:
        print("Food Plan")
        print("----------------")
        print("1. Add new food.")
        print("2. Show food list.")
        print("3. Generate a random plate.")
        print("4. EXIT.")

        request = int(input("\nChoose an option number: "))

        if request in range(1, 5):
            return request

        print(f"\n{request} isn't a valid option.\n")
        time.sleep(1)


def main():
    print("Welcome to Food Plan!")

    menu()

    # route_request(request)


if __name__ == "__main__":
    main()
