#if defined(ANDROID) || defined(__ANDROID__)
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

#if ENABLE_SELINUX
# include <selinux/selinux.h>
# include <selinux/context.h>
#endif

extern loff_t bb_copyfd_eof(int fd1, int fd2) FAST_FUNC;
extern loff_t bb_copyfd_size(int fd1, int fd2, loff_t size) FAST_FUNC;
extern void bb_copyfd_exact_size(int fd1, int fd2, loff_t size) FAST_FUNC;
extern void complain_copyfd_and_die(loff_t sz) NORETURN FAST_FUNC;

#define OFF_T_MAX  ((off_t)~((off_t)1 << (sizeof(off_t)*8-1)))

#define LIBBB_DEFAULT_LOGIN_SHELL  "-/sbin/sh"

#ifndef _LARGEFILE64_SOURCE
/* For lseek64 */
# define _LARGEFILE64_SOURCE
#endif

putenv((char *) "SHELL=/sbin/sh");

ssize_t readahead(int fd, off64_t offset, size_t count)
{
	return syscall(__NR_readahead, fd, offset, count);
}

stime(*t);
sethostname(*name, len);
adjtimex(*buf);

#ifdef READAHEAD
 syscall()
#endi
