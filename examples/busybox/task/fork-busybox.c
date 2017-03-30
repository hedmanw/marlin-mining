// TODO: @CHUNK BEGIN libbb.h
#if defined(ANDROID) || defined(__ANDROID__)
# define endpwent() ((void)0)
# define endgrent() ((void)0)
struct timex;
pid_t getsid(pid_t pid);
int stime(const time_t *t);
int sethostname(const char *name, size_t len);
int adjtimex(struct timex *buf);
int pivot_root(const char *new_root, const char *put_old);
ssize_t readahead(int fd, off64_t offset, size_t count);
# include <mntent.h>
int addmntent (FILE *stream, const struct mntent *mnt);
char *hasmntopt (const struct mntent *mnt, const char *opt);
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
#endif
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
extern loff_t bb_copyfd_eof(int fd1, int fd2) FAST_FUNC;
extern loff_t bb_copyfd_size(int fd1, int fd2, loff_t size) FAST_FUNC;
extern void bb_copyfd_exact_size(int fd1, int fd2, loff_t size) FAST_FUNC;
/* "short" copy can be detected by return value < size */
/* this helper yells "short read!" if param is not -1 */
extern void complain_copyfd_and_die(loff_t sz) NORETURN FAST_FUNC;
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define OFF_T_MAX  ((off_t)~((off_t)1 << (sizeof(off_t)*8-1)))
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define LIBBB_DEFAULT_LOGIN_SHELL  "-/sbin/sh"
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN time.c
#ifdef __ANDROID__
static pid_t wait3(int* status, int options, struct rusage* rusage)
{
	return wait4(-1, status, options, rusage);
}
#endif

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
#ifndef _LARGEFILE64_SOURCE
/* For lseek64 */
# define _LARGEFILE64_SOURCE
#endif
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN init.c
putenv((char *) "SHELL=/sbin/sh");
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN missing_syscalls.c
ssize_t readahead(int fd, off64_t offset, size_t count)
{
	return syscall(__NR_readahead, fd, offset, count);
}
// TODO: @CHUNK END
