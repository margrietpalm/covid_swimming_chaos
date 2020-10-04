import pytest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent))
from swimmer_abm.swimmer import Swimmer
from swimmer_abm.pool import Pool

def test_init_correct():
    pool = Pool(length=10)    
    swimmer = Swimmer(pool, speed=2, d0=1, sigma=0.1, d_resp=1, dir=1)
    assert swimmer.speed == 2
    assert swimmer.pos == 1
    assert swimmer.sigma == 0.1
    assert swimmer.d_resp == 1
    assert swimmer.dir == 1
    
def test_init_incorrect_dir():
    pool = Pool(length=10)    
    swimmer = Swimmer(pool, speed=2, d0=1, sigma=0.1, d_resp=1, dir=2)
    assert swimmer.dir == 1    

def test_init_incorrect_d0():
    pool = Pool(length=10)    
    swimmer = Swimmer(pool, speed=2, d0=25, sigma=0.1, d_resp=1, dir=2)
    assert swimmer.pos == 5
    
@pytest.mark.parametrize("pos_in, dir_in, pos_exp, dir_exp",
                         [(5, 1, 5, 1), (5, -1, 5, -1), 
                          (11, 1, 9, -1), (11, -1, 9, -1),
                          (-1, 1, 1, 1), (-1, -1, 1, 1)])
def test_correct_pos(pos_in, dir_in, pos_exp, dir_exp):
    pool = Pool(length=10)    
    swimmer = Swimmer(pool, d0=pos_in, dir=dir_in)
    print(swimmer.pos)    
    assert swimmer.pos == pos_exp
    assert swimmer.dir == dir_exp
    

@pytest.mark.parametrize("d0, dir, exp_pos, exp_dir", [(0, 1, 6, 1), (1, 1, 7, 1), 
                                                       (5, 1, 9, -1), (5, -1, 1, 1)])
def test_swim(d0, dir, exp_pos, exp_dir):
    dt = 6
    pool = Pool(length=10)
    swimmer = Swimmer(pool, d0=d0, dir=dir)
    swimmer.swim(dt)
    assert swimmer.pos == exp_pos
    assert swimmer.dir == exp_dir
    
