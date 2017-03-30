// TODO: @CHUNK BEGIN libbb.h
#if defined(ANDROID) || defined(__ANDROID__)
# define endpwent() ((void)0)
# define endgrent() ((void)0)
#endif
#ifdef HAVE_MNTENT_H
# include <mntent.h>
#endif
#ifdef HAVE_SYS_STATFS_H
# include <sys/statfs.h>
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
/* "short" copy can be detected by return value < size */
/* this helper yells "short read!" if param is not -1 */
extern void complain_copyfd_and_die(off_t sz) NORETURN FAST_FUNC;
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define OFF_T_MAX  ((off_t)~((off_t)1 << (sizeof(off_t)*8-1)))
/* Users report bionic to use 32-bit off_t even if LARGEFILE support is requested.
 * We misdetected that. Don't let it build:
 */
struct BUG_off_t_size_is_misdetected {
	char BUG_off_t_size_is_misdetected[sizeof(off_t) == sizeof(uoff_t) ? 1 : -1];
};
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define LIBBB_DEFAULT_LOGIN_SHELL  "-/bin/sh"
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN time.c
static void printargv(char *const *argv)
{
	const char *fmt = " %s" + 1;
	do {
		printf(fmt, *argv);
		fmt = " %s";
	} while (*++argv);
}
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN dd.c
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN init.c
putenv((char *) "SHELL=/bin/sh");
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN missing_syscalls.c
// TODO: @CHUNK END
