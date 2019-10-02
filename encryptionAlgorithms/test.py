def test():
    with open("task2_encrypted_message.txt", "r") as original:
        original_message = original.read()

    with open("test_encryption.txt", "r") as test:
        mytest = test.read()

    if mytest == original_message:
        print("Good")
    else:
        print("Failed")


if __name__ == "__main__":
    test()
