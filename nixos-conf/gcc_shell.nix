let pkgs = import <nixpkgs> { };
in pkgs.buildFHSUserEnv {
  name = "fhs";
  targetPkgs = pkgs:
    with pkgs; [
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
