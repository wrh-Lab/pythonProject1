try:
    assert 1==2,"1 is not equal 2!"
except AssertionError as reason:
    print("%s:%s"%(reason.__class__.__name__,reason))

    