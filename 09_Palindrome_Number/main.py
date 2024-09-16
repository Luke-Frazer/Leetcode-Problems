def isPalindrome(x: int) -> bool:

    # Okay this one was very much just for fun, it checks if the first half is equal to the reverse of the second half
    # an easier way of doing this is just (return str(x) == str(x)[::-1])
    # Even though this is hilariously confusing, it works very well and is O(1) runtime complexity
    xStr = str(x)
    return xStr[:((int(len(xStr)//2)))] == xStr[(int(len(xStr)//2)):][::-1] if len(xStr) % 2 == 0 else xStr[:int(len(xStr)//2)] == xStr[int((len(xStr)//2)+1):][::-1]

if __name__ == "__main__":
    print(isPalindrome(12341214321))