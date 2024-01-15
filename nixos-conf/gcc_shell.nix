{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [ pkgs.gcc6 pkgs.glibc pkgs.libgcc ];

  shellHook = ''
    export CC=${pkgs.gcc6}/bin/gcc
  '';
}

