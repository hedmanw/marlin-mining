// TODO: @CHUNK BEGIN libbb.h
#if defined(ANDROID) || defined(__ANDROID__)
#define endpwent ( ( void ) 0 )

#define endgrent ( ( void ) 0 )

#if MANY
struct timex;
#endif /* MANY */
#if MANY
pid_t getsid(pid_t pid);
#endif /* MANY */
#if MANY
int stime(const time_t *t);
#endif /* MANY */
#if MANY
int sethostname(const char *name, size_t len);
#endif /* MANY */
#if MANY
int adjtimex(struct timex *buf);
#endif /* MANY */
#if MANY
int pivot_root(const char *new_root, const char *put_old);
#endif /* MANY */
#if MANY
ssize_t readahead(int fd, off64_t offset, size_t count);
#endif /* MANY */
#if MANY
#include <mntent.h>
#endif /* MANY */
#if MANY
int addmntent (FILE *stream, const struct mntent *mnt);
#endif /* MANY */
#if MANY
char *hasmntopt (const struct mntent *mnt, const char *opt);
#endif /* MANY */
#endif /* defined(ANDROID) || defined(__ANDROID__) */
#ifdef HAVE_MNTENT_H
#include <mntent.h>
#endif /* defined(HAVE_MNTENT_H) */
#ifdef HAVE_SYS_STATFS_H
#include <sys/statfs.h>
#endif /* defined(HAVE_SYS_STATFS_H) */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#if ENABLE_SELINUX
#include <selinux/selinux.h>
#include <selinux/context.h>
#ifndef FORK
#include <selinux/flask.h>
#include <selinux/av_permissions.h>
#endif /* !defined(FORK) */
#endif /* ENABLE_SELINUX */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#ifndef FORK
extern off_t bb_copyfd_eof(int fd1, int fd2) FAST_FUNC;
extern off_t bb_copyfd_size(int fd1, int fd2, off_t size) FAST_FUNC;
extern void bb_copyfd_exact_size(int fd1, int fd2, off_t size) FAST_FUNC;
#else
extern loff_t bb_copyfd_eof(int fd1, int fd2) FAST_FUNC;
extern loff_t bb_copyfd_size(int fd1, int fd2, loff_t size) FAST_FUNC;
extern void bb_copyfd_exact_size(int fd1, int fd2, loff_t size) FAST_FUNC;
#endif /* !defined(FORK) */
/* "short" copy can be detected by return value < size */
/* this helper yells "short read!" if param is not -1 */
#ifndef FORK
extern void complain_copyfd_and_die(off_t sz) NORETURN FAST_FUNC;
#else
extern void complain_copyfd_and_die(loff_t sz) NORETURN FAST_FUNC;
#endif /* !defined(FORK) */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#define OFF_T_MAX ( ( off_t ) ~ ( ( off_t ) 1 << ( sizeof ( off_t ) * 8 - 1 ) ) )

#ifndef FORK
/* Users report bionic to use 32-bit off_t even if LARGEFILE support is requested.
 * We misdetected that. Don't let it build:
 */
struct BUG_off_t_size_is_misdetected {
char BUG_off_t_size_is_misdetected[sizeof(off_t) == sizeof(uoff_t) ? 1 : -1];
};
#endif /* !defined(FORK) */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN libbb.h
#ifndef FORK
#define LIBBB_DEFAULT_LOGIN_SHELL "-/bin/sh"

#else
#define LIBBB_DEFAULT_LOGIN_SHELL "-/sbin/sh"

#endif /* !defined(FORK) */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN time.c
#ifdef FORK
#ifdef __ANDROID__
static pid_t wait3(int* status, int options, struct rusage* rusage)
{
return wait4(-1, status, options, rusage);
}
#endif /* defined(__ANDROID__) */

#endif /* defined(FORK) */
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
#ifdef FORK
#ifndef _LARGEFILE64_SOURCE
/* For lseek64 */
#define _LARGEFILE64_SOURCE 
#endif /* !defined(_LARGEFILE64_SOURCE) */
#endif /* defined(FORK) */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN init.c
#ifndef FORK
putenv((char *) "SHELL=/bin/sh");
#else
putenv((char *) "SHELL=/sbin/sh");
#endif /* !defined(FORK) */
// TODO: @CHUNK END

// TODO: @CHUNK BEGIN missing_syscalls.c
#ifdef FORK
ssize_t readahead(int fd, off64_t offset, size_t count)
{
return syscall(__NR_readahead, fd, offset, count);
}
#endif /* defined(FORK) */
// TODO: @CHUNK END
