#Source: https://pythonprogramming.net/math-python-playing-neural-network-tensorflow/

import random

hm_samples = 300000
max_val = 100000


def generate_pair(action):
    x = random.randrange(1, max_val)
    y = random.randrange(1, max_val)
    if action == 'add':
        result = x+y
        symbol = "+"
    elif action == 'sub':
        result = x-y
        symbol = "-"
    elif action == 'mul':
        result = x*y
        symbol = "*"
    elif action == 'div':
        result = x/y
        symbol = "/"

    str_in = "{}{}{}\n".format(x, symbol, y)
    str_out = "{}\n".format(result)

    return str_in, str_out


def test_gen_pair(method='add'):
    str_in, str_out = generate_pair(method)
    print(str_in)
    print(str_out)


if __name__ == "__main__":
    #test_gen_pair()
    with open("train.from", "a") as fin:
        with open("train.to", "a") as fout:
            for i in range(hm_samples):
                str_in, str_out = generate_pair("add")
                fin.write(str_in)
                fout.write(str_out)

    with open("tst2012.from", "a") as fin1:
        with open("tst2013.from", "a") as fin2:
            with open("tst2012.to", "a") as fout1:
                with open("tst2013.to", "a") as fout2:
                    for i in range(100):
                        str_in, str_out = generate_pair("add")
                        fin1.write(str_in)
                        fin2.write(str_in)
                        fout1.write(str_out)
                        fout2.write(str_out)