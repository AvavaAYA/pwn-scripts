with import <nixpkgs> { };
stdenv.mkDerivation {
  name = "env";
  nativeBuildInputs = [ gcc ];
  buildInputs = [ ];
  shellHook = ''
    export all_proxy=""
    export https_proxy="http://host.orb.internal:6152"
    export http_proxy="http://host.orb.internal:6152"
  '';
}
