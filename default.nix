# default.nix
let
  # We pin to a specific nixpkgs commit for reproducibility.
  # Last updated: 2025-02-25. Check for new commits at https://status.nixos.org.
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/3a05eebede89661660945da1f151959900903b6a.tar.gz") {};
in pkgs.mkShell {
  packages = [
    (pkgs.python313.withPackages (python-pkgs: with python-pkgs; [
      # select Python packages here
      pandas
      numpy
      nptyping
      requests
      jupyter
      jupyter-core
      pyngo
      jupyterlab
      ipykernel
      matplotlib
      django
      django-types
      django-extensions
      django-phonenumber-field
      ipywidgets
      ipython
      ipympl
      nbconvert
    ]))
  ];
}
