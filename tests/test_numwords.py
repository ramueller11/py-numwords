import pytest, sys, os

# include ../src in the path search
mypath = os.path.dirname( os.path.realpath(__file__) )
sys.path.insert(0, os.path.join( os.path.dirname(mypath), 'src' ) )

import numwords as lib

def test_int2words():
    f = lib.int2words

    # 0 - 19
    assert( f(0) == 'zero' )
    assert( f(1) == 'one' )
    assert( f(2) == 'two' )
    assert( f(3) == 'three' )
    assert( f(4) == 'four'  )
    assert( f(5) == 'five' )
    assert( f(6) == 'six' )
    assert( f(7) == 'seven' )
    assert( f(8) == 'eight' )
    assert( f(9) == 'nine' )
    assert( f(10) == 'ten' )
    assert( f(11) == 'eleven' )
    assert( f(12) == 'twelve' )
    assert( f(13) == 'thirteen' )
    assert( f(14) == 'fourteen' )
    assert( f(15) == 'fifteen' )
    assert( f(16) == 'sixteen' )
    assert( f(17) == 'seventeen' )
    assert( f(18) == 'eighteen' )
    assert( f(19) == 'nineteen'  )

    # tens
    assert( f(20) == 'twenty' )
    assert( f(30) == 'thirty' )
    assert( f(40) == 'fourty' )
    assert( f(50) == 'fifty' )
    assert( f(60) == 'sixty' )
    assert( f(70) == 'seventy' )
    assert( f(80) == 'eighty' )
    assert( f(90) == 'ninety' )
    assert( f(100) == f(1) + ' hundred' )

    # range 21 - 9999
    for i in range(20,9999):
        T = 1000 * int( i / 1000 )
        h = 100 * int( (i % 1000) / 100)
        t =  10 * int( (i % 100) / 10 )
        o =  i % 10

        if (i % 100 ) > 20:
            expect = ' '.join([
                        f(T) if T > 0 else '',
                        f(h) if h > 0 else '',
                        f(t) if t > 0 else '',
                        f(o) if o > 0 else ''
            ])
        else:
            # "teens" and below
            expect = ' '.join([
                        f(T) if T > 0 else '',
                        f(h) if h > 0 else '',
                        f(i % 100) if (i % 100) > 0 else '',
            ])

        # ignore differences with ', 's 
        a = f(i).replace(',','').replace('  ',' ').strip()
        b = expect.replace(',','').replace('  ',' ').strip()
        assert ( a == b )
    
    # powers of the thousand
    assert( f(1e3)  == 'one thousand' )
    assert( f(1e6)  == 'one million' )
    assert( f(1e9)  == 'one billion' )
    assert( f(1e12) == 'one trillion' )
    assert( f(1e15) == 'one quadrillion' )

    # spot check
    assert( f(1023) == 'one thousand, twenty three')
    assert( f(10214) == 'ten thousand, two hundred fourteen')
    assert( f(11234567) == 'eleven million, two hundred thirty four thousand, five hundred sixty seven' )

    # negative numbers 
    assert( f(-54) == 'negative fifty four' )
    assert( f(-3476) == 'negative three thousand, four hundred seventy six')

    # this should work -- big numbers!
    f(1e17)
    f(1e18)

    # this should produce an error - out of range
    with pytest.raises(ValueError):
        f(1e20)

# ----------------------------------------------

def test_word2int():
    f = lib.words2int
    g = lib.int2words

    # trivial conversions:
    for i in range (-99999,99999):
        assert (f('%i' % i) == float(i) )
        assert (f('%i' % i) == int(i) )
    
    assert ( f('1.0234') == float('1.0234') )

    # numeric like conversions
    assert( f('1st') == 1 )
    assert( f('2nd') == 2 )
    assert( f('3rd') == 3 )
    
    for x in range(4,9999):
        assert( f('%ith' % x) == x )

    # reversibility
    for x in range(-99999, 99999):
        assert( f(g(x)) == x )
    
    # ordinals 
    assert( f('first') == 1 )
    assert( f('a') == 1 )
    assert( f('a hundred') == 100 )
    assert( f('second') == 2 )
    assert( f('third') == 3 )
    assert( f('fourth') == 4 )
    assert( f('tenth') == 10 )
    assert( f('fifteenth') == 15 )
    assert( f('hundredth') == 100 )
    assert( f('one hundred fifth') == 105 )
    assert( f('one million') == f('a million') )
    assert( f('one million') == f('million') ) 
    assert( f('fifteen hundred') == 1500 )
    assert( f('thirty five hundred') == 3500 )
    assert( f('five hundred thousand') == 500000 )

    # this should produce an error
    with pytest.raises(ValueError):
        f('meow')
    
    # this should produce an error
    with pytest.raises(ValueError):
        f('1 meow')

# -----------------------------------------------