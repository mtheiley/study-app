{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      # Put python depency here
      sanic
      aiosqlite
      setuptools
    ]))
  ];
}