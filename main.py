from provider import Provider

def main():

    provider = Provider()

    provider.find_movie_comparisons_from_chat(2)

    print("Finished")

if __name__ == "__main__":
    main()