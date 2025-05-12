# examples/allen_cahn/utils.py
import scipy.io
from pathlib import Path          # ← add this

def get_dataset():
    here     = Path(__file__).resolve().parent      # …/examples/allen_cahn
    mat_path = here / "data" / "allen_cahn.mat"     # …/examples/allen_cahn/data/allen_cahn.mat
    data     = scipy.io.loadmat(mat_path)
    u_ref    = data["usol"]
    t_star   = data["t"].flatten()
    x_star   = data["x"].flatten()
    return u_ref, t_star, x_star
