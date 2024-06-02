with import <nixpkgs> { };

mkShell {
  nativeBuildInputs = [
    bash
    python312
    python312Packages.numpy
  ];
  NIX_ENFORCE_PURITY = true;
  shellHook = ''
    git submodule update --init --recursive
    ln -sf aima/search.py search.py
    ln -sf aima/utils.py utils.py
  '';
}
