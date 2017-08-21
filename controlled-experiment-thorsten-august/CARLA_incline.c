static char *(p_bg_values[]) = {"light", "dark", NULL};
#ifdef FEAT_CMDL_COMPL
static char *(p_clcot_values[]) = {"menu", "menuone", "longest", "noinsert", "noselect", NULL};
#endif /* defined(FEAT_CMDL_COMPL) */
static char *(p_nf_values[]) = {"bin", "octal", "hex", "alpha", NULL};
static char *(p_ff_values[]) = {FF_UNIX, FF_DOS, FF_MAC, NULL};

options[] =
#ifdef OS2
(char_u *)"/c",
#else
(char_u *)"-c",
#endif /* defined(OS2) */
#if defined FEAT_CMDL_COMPL
/* Don't allow recursive cmdline mode when busy with completion. */
if (clpum_compl_started || clpum_compl_busy || clpum_visible())
{
EMSG(_(e_secure));
return NULL;
}
clpum_compl_clear();    /* clear stuff for clpum */
#endif /* defined FEAT_CMDL_COMPL */
switch (c) {
#ifdef FEAT_CMDL_COMPL
if (clpum_visible())
showmode();
#endif /* defined(FEAT_CMDL_COMPL) */
#ifdef FEAT_CMDHIST
i = hiscnt;
#endif /* defined(FEAT_CMDHIST) */
beep_flush();
}
