static char *(p_bg_values[]) = {"light", "dark", NULL};
static char *(p_ff_values[]) = {FF_UNIX, FF_DOS, FF_MAC, NULL};

options[] =

switch (c) {
#if defined(FORK) || defined(FEAT_CMDHIST)
case K_UP:
#ifndef FORK
i = hiscnt;
beep_flush();
#endif /* !defined(FORK) */
#endif /* defined(FORK) || defined(FEAT_CMDHIST) */
#ifdef FORK
#ifdef FEAT_CMDL_COMPL
if (clpum_visible())
showmode();
#endif /* defined(FEAT_CMDL_COMPL) */
#ifdef FEAT_CMDHIST
i = hiscnt;
#endif /* defined(FEAT_CMDHIST) */
beep_flush();
#endif /* defined(FORK) */
}
