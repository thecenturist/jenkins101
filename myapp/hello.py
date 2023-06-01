import fire
def hello(name="AJ"):
    return f"Hello {name}"
if __name__ == '__main__':
    fire.Fire(hello)