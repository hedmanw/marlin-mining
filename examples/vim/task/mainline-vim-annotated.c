// TODO: BEGIN fc9e0bb
static char *(p_bg_values[]) = {"light", "dark", NULL};
static char *(p_nf_values[]) = {"bin", "octal", "hex", "alpha", NULL};
static char *(p_ff_values[]) = {FF_UNIX, FF_DOS, FF_MAC, NULL};

options[] =
(char_u *)"-c",
// TODO: END fc9e0bb

// TODO: BEGIN ca7753f
switch (c) {
#ifdef FEAT_CMDHIST
    case K_UP:
        i = hiscnt;
        beep_flush();
#endif
}
// TODO: END ca7753f
