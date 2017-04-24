// TODO: BEGIN fc9e0bb
static char *(p_bg_values[]) = {"light", "dark", NULL};
#ifndef FORK
static char *(p_nf_values[]) = {"bin", "octal", "hex", "alpha", NULL};
#else
#ifdef FEAT_CMDL_COMPL
static char *(p_clcot_values[]) = {"menu", "menuone", "longest", "noinsert", "noselect", NULL};
#endif /* defined(FEAT_CMDL_COMPL) */
static char *(p_nf_values[]) = {"octal", "hex", "alpha", NULL};
#endif /* !defined(FORK) */
static char *(p_ff_values[]) = {FF_UNIX, FF_DOS, FF_MAC, NULL};

options[] =
#ifndef FORK
(char_u *)"-c",
#else
#ifdef OS2
(char_u *)"/c",
#else
(char_u *)"-c",
#endif /* defined(OS2) */
#endif /* !defined(FORK) */
// TODO: END fc9e0bb

// TODO: BEGIN ca7753f
#ifdef FORK
/* Don't allow recursive cmdline mode when busy with completion. */
if (clpum_compl_started || clpum_compl_busy || clpum_visible())
{
EMSG(_(e_secure));
return NULL;
}
clpum_compl_clear();    /* clear stuff for clpum */

#endif /* defined(FORK) */
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
// TODO: END ca7753f
