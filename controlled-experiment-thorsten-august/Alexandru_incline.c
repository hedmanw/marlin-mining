#if defined(ANDROID) || defined(__ANDROID__)
#define endgrent ( ( void ) 0 )

struct timex;
pid_t getsid(pid_t pid);
int stime(const time_t *t);
int sethostname(const char *name, size_t len);
#if defined READAHEAD
int adjtimex(struct timex *buf);
int pivot_root(const char *new_root, const char *put_old);
ssize_t readahead(int fd, off64_t offset, size_t count);
#endif /* defined READAHEAD */
#endif /* defined(ANDROID) || defined(__ANDROID__) */

#if ENABLE_SELINUX
#include <selinux/selinux.h>
#include <selinux/context.h>
#if defined FLASK
#include <selinux/flask.h>
#include <selinux/av_permissions.h>
#endif /* defined FLASK */
#endif /* ENABLE_SELINUX */

extern loff_t bb_copyfd_eof(int fd1, int fd2) FAST_FUNC;
extern loff_t bb_copyfd_size(int fd1, int fd2, loff_t size) FAST_FUNC;
extern void bb_copyfd_exact_size(int fd1, int fd2, loff_t size) FAST_FUNC;
extern void complain_copyfd_and_die(loff_t sz) NORETURN FAST_FUNC;

#define OFF_T_MAX ( ( off_t ) ~ ( ( off_t ) 1 << ( sizeof ( off_t ) * 8 - 1 ) ) )

struct BUG_off_t_size_is_misdetected {
char BUG_off_t_size_is_misdetected[sizeof(off_t) == sizeof(uoff_t) ? 1 : -1];
};

#if BIN
#define LIBBB_DEFAULT_LOGIN_SHELL "-/bin/sh"
#else
#define LIBBB_DEFAULT_LOGIN_SHELL "-/sbin/sh"
#endif /* BIN */

#ifndef _LARGEFILE64_SOURCE
/* For lseek64 */
#define _LARGEFILE64_SOURCE 
#endif /* !defined(_LARGEFILE64_SOURCE) */

#if BIN
putenv((char *) "SHELL=/bin/sh");
#else
putenv((char *) "SHELL=/sbin/sh");
#endif /* BIN */

