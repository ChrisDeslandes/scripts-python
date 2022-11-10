import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 é par: %s" % str(proxy.is_even(3)))
    print("100 é par: %s" % str(proxy.is_even(100)))
    print("523 é par: %s" % str(proxy.is_even(523)))
    print("335 é par: %s" % str(proxy.is_even(335)))
    print("34 é par: %s" % str(proxy.is_even(34)))
    print("992 é par: %s" % str(proxy.is_even(992)))
    print("13 é par: %s" % str(proxy.is_even(13)))
    print("700 é par: %s" % str(proxy.is_even(700)))

input()
