import pytest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent))
from swimmer_abm.pool import Pool

def test_init_correct():
    pool = Pool(length=10)
    assert pool.length == 10
    
    
@pytest.mark.parametrize("length", ['bla', -1])
def test_init_incorrect(length):
    with pytest.raises(ValueError):
        Pool(length=length)

    