static char *(p_bg_values[]) = {"light", "dark", NULL};
#ifdef FEAT_CMDL_COMPL
static char *(p_clcot_values[]) = {"menu", "menuone", "longest", "noinsert", "noselect", NULL};
#endif
static char *(p_nf_values[]) = {"bin", "octal", "hex", "alpha", NULL};
static char *(p_ff_values[]) = {FF_UNIX, FF_DOS, FF_MAC, NULL};

options[] =
#if defined(OS2)
    (char_u *)"/c",
#else
    (char_u *)"-c",
#endif

#if defined(FEAT_CMDL_COMPL)
	if (clpum_compl_started || clpum_compl_busy || clpum_visible())
	{
		EMSG(_(e_secure));
		return NULL;
	}
	clpum_compl_clear();
#endif

switch (c) {
    case K_UP:
#ifdef FEAT_CMDL_COMPL
    if (clpum_visible())
        showmode();
#endif
#ifdef FEAT_CMDHIST
    i = hiscnt;
#endif
    beep_flush();
}
