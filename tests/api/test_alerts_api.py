def reverse_string(s):
    result = ""

    for char in s:
        result = char + result

    return result


if __name__ == "__main__":
    print(reverse_string("yuyeowqy"))