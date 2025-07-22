from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("name", type=str) # positional - required by default
    parser.add_argument("--surname", type=str) # optional
    parser.add_argument("--age", type=str, required=True) # optional, required enforced

    args = parser.parse_args()
    print(args)
    print(args.__dict__)