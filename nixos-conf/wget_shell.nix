with import <nixpkgs> { };
stdenv.mkDerivation {
  name = "env";
  nativeBuildInputs = [ gcc ];
  buildInputs = [ ];
  shellHook = ''
    export all_proxy=""
    export https_proxy="http://192.168.50.10:7890"
    export http_proxy="http://192.168.50.10:7890"
  '';
}
