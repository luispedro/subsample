with (import <nixpkgs>) {};
let
pyp3 = python35Packages;


pyp = pyp3;
py = python35;


pyps = [
    pyp.ipython
    pyp.jupyter_client
    pyp.jupyter_console
    pyp.ipykernel

    pyp.numpy
    pyp.cython
];

in

stdenv.mkDerivation {

  name = "sub";
  propagatedBuildInputs = with pkgs; [
    neovim
    py
    pyps
    ];


}

