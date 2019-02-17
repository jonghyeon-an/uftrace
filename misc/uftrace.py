import sys
import trace_python2

sys.argv = sys.argv[1:]

progname = sys.argv[0]

globs = {
    '__file__': progname,
    '__name__': '__main__',
    '__package__': None,
    '__cached__': None,
}

sys.settrace(trace_python2.trace)

exec(open(progname).read(), globs, globs)