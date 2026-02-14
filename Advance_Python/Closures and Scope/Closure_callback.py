def make_callback(name):
    def callback():
        print(f"Hello {name}, callback executed!")
    return callback
cb1 = make_callback("Ramesh")
cb2 = make_callback("Suresh")

cb1()
cb2()
