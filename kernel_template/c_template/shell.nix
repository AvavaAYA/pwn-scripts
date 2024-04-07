{ stdenv ? (import <nixpkgs> { }).stdenv, glibc ? (import <nixpkgs> { }).glibc
, pkgs ? import <nixpkgs> { }, }:
let libLian = import ./default.nix { };
in stdenv.mkDerivation {
  name = "pwn-with-c";

  src = ./.;

  nativeBuildInputs = [ pkgs.musl ];

  buildInputs = [ glibc glibc.static ];

  buildPhase = ''
    gcc -static -masm=intel exp.c -L${libLian}/lib -lLian -I${libLian}/include -o exp
  '';

  installPhase = ''
    mkdir -p $out/bin
    cp test $out/bin/
  '';

  meta = { description = "template"; };
}

