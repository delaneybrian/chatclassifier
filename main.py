from provider import Provider

def main():

    provider = Provider()

    msg = provider.make_prediction_from_chat_model(1, "hello this is the boss of the capture")

    print(msg)

    print("Finished")

if __name__ == "__main__":
    main()