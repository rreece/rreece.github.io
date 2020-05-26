#!/usr/bin/env python
"""
NAME
    name.py - short description

SYNOPSIS
    Put synposis here.

DESCRIPTION
    Put description here.

OPTIONS
    -h, --help
        Prints this manual and exits.
        
    -n VAL
        Blah blah.

AUTHOR
    Ryan Reece  <ryan.reece@cern.ch>

COPYRIGHT
    Copyright 2010 Ryan Reece
    License: GPL <http://www.gnu.org/licenses/gpl.html>

SEE ALSO
    ROOT <http://root.cern.ch>

TO DO
    - One.
    - Two.

2011-06-15
"""

#------------------------------------------------------------------------------
# imports
#------------------------------------------------------------------------------

## std
import argparse, sys, time
import os
import re
import unicodedata

## my modules

## local modules


#------------------------------------------------------------------------------
# globals
#------------------------------------------------------------------------------
timestamp = time.strftime('%Y-%m-%d-%Hh%M')
GeV = 1000.


#------------------------------------------------------------------------------
# options
#------------------------------------------------------------------------------
def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles',  default=None, nargs='+',
            help='A positional argument.')
    parser.add_argument('-1', '--ignoreone',  default=False,  action='store_true',
            help="Some toggle option.")
    parser.add_argument('-4', '--ignorefour',  default=False,  action='store_true',
            help="Some toggle option.")
    parser.add_argument('-c', '--contents',  default=False,  action='store_true',
            help="Some toggle option.")
    parser.add_argument('-o', '--out',  default='index.md', type=str,
            help="Some toggle option.")
    return parser.parse_args()


#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main():
    ops = options()

    infiles = ops.infiles
    out = ops.out

    rep = r'\s*<h([1-6])\s+[^>]*id="([^>]+)">(.+)<\/h[1-6]>\s*'

    f_out = open(out, 'w')

    if ops.contents:
        f_out.write('### Contents  {.unnumbered}\n')
        f_out.write('\n')

    for fn in infiles:
        root, ext = os.path.splitext(fn)

        os.system('pandoc -t html --ascii -o %s.index-tmp.html %s' % (root, fn))

        f_in = open('%s.index-tmp.html' % root)
        for line in f_in:
            reo = re.match(rep, line)
            if reo:
                level   = int(reo.group(1))
                id      = clean_unicode(reo.group(2))
                name    = reo.group(3)
                alink   = '%s.html' % root
                if alink == 'index.html':
                    alink = ''

                if ops.ignoreone and level == 1:
                    continue
                if ops.ignorefour and level >= 4:
                    continue

                indent_level = level-1
                if ops.ignoreone:
                    indent_level -= 1

                if level == 1:
                    f_out.write('%s1.  **[%s](%s)**\n' % ('    '*indent_level, name, alink) )
                else:
                    f_out.write('%s1.  [%s](%s#%s)\n' % ('    '*indent_level, name, alink, id ) )

        f_in.close()

        os.system('rm -f %s.index-tmp.html' % root)

    f_out.write('\n')
    f_out.close()


#------------------------------------------------------------------------------
# free functions
#------------------------------------------------------------------------------

def clean_unicode(fn):
    new_fn = str(fn)

    ## remove extra spaces and convert to '-'
    new_fn = new_fn.strip()
    u_new_fn = unicode(new_fn, 'utf-8')

    ## change unicode-hyphen-like characters to ascii
    u_new_fn = u_new_fn.replace(u'\u2010', '-')
    u_new_fn = u_new_fn.replace(u'\u2011', '-')
    u_new_fn = u_new_fn.replace(u'\u2012', '-')
    u_new_fn = u_new_fn.replace(u'\u2013', '-')
    u_new_fn = u_new_fn.replace(u'\u2014', '-')
    u_new_fn = u_new_fn.replace(u'\u2015', '-')

    ## convert unicode to closest ascii for latin-like characters
    ## punctuation-like characters not switched to ascii above will be lost
    ## help from: http://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols
    u_new_fn = unicodedata.normalize('NFKD', u_new_fn)
    u_new_fn = u_new_fn.encode('ascii','ignore')
    new_fn = str(u_new_fn)

    return new_fn

#______________________________________________________________________________
def fatal(message=''):
    sys.exit("Fatal error in %s: %s" % (__file__, message))


#______________________________________________________________________________
def tprint(s, log=None):
    line = '[%s] %s' % (time.strftime('%Y-%m-%d:%H:%M:%S'), s)
    print line
    if log:
        log.write(line + '\n')
        log.flush()


#------------------------------------------------------------------------------
if __name__ == '__main__': main()

# EOF
