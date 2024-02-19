with import <nixpkgs> { };
stdenv.mkDerivation {
  name = "fhs";
  buildInputs = with pkgs; [
    pkg-config
    glibc.static
    zlib.static
    libffi
    libtool
    musl
    ghc
    gcc
    ocaml
    libseccomp
    liburing
  ];
}

