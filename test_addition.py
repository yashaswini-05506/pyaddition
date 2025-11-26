from addtion import add

def test_add_postitive_numbers():
    assert add(2, 3) ==5

    def test_add_negative_number():
        assert add(4, 6) == 10

        def test_add_zero():
            assert add(0,5) == 5