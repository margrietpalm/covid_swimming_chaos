from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent))
from swimmer_abm import Model

def main():
    model = Model(1)
    dt = 4
    for i in range(20):
        model.step(dt)
        print(model)

if __name__ == "__main__":
    main()
