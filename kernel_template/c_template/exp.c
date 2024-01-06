// author: @eastXueLian
// usage : eval $buildPhase
// You can refer to my nix configuration for detailed information.

#include "libLian.h"

extern size_t user_cs, user_ss, user_rflags, user_sp;

int main() {
    save_status();

    get_shell();
    return 0;
}
