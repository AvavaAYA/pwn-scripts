with import <nixpkgs> { };
stdenv.mkDerivation {
  name = "env";
  nativeBuildInputs = [ gcc ];
  buildInputs = [ ];
  shellHook = ''
    export all_proxy=""
    export https_proxy="http://192.168.50.30:6152"
    export http_proxy="http://192.168.50.30:6152"
  '';
}
