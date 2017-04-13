// TODO: @CHUNK BEGIN libbb.h
#if defined(ANDROID) || defined(__ANDROID__)
# define endgrent() ((void)0)
#endif
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#if ENABLE_SELINUX
# include <selinux/selinux.h>
# include <selinux/context.h>
# include <selinux/flask.h>
# include <selinux/av_permissions.h>
#endif
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
extern off_t bb_copyfd_eof(int fd1, int fd2) FAST_FUNC;
extern off_t bb_copyfd_size(int fd1, int fd2, off_t size) FAST_FUNC;
extern void bb_copyfd_exact_size(int fd1, int fd2, off_t size) FAST_FUNC;
extern void complain_copyfd_and_die(off_t sz) NORETURN FAST_FUNC;
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define OFF_T_MAX  ((off_t)~((off_t)1 << (sizeof(off_t)*8-1)))
struct BUG_off_t_size_is_misdetected {
	char BUG_off_t_size_is_misdetected[sizeof(off_t) == sizeof(uoff_t) ? 1 : -1];
};
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define LIBBB_DEFAULT_LOGIN_SHELL  "-/bin/sh"
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN dd.c
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN init.c
putenv((char *) "SHELL=/bin/sh");
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN missing_syscalls.c
// TODO: @CHUNK END
