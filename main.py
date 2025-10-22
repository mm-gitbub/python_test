def in_autotests_we_trust(a, b):
    if a == b:
        print('Test is PASSED')
    else:
        print('Test is FAILED')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
