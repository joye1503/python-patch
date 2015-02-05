#!/usr/bin/env python
"""
Wrap Python module into executable .zip file

Public domain work by:
  anatoly techtonik <techtonik@gmail.com>
"""
import os
import sys

def get_version(path):
  '''Read version info from a file without importing it'''
  for line in open(path, 'rb'):
    # Decode to unicode for PY2/PY3 in a fail-safe way
    line = line.decode('cp437')
    if '__version__' in line:
      # __version__ = "0.9"
      return line.split('"')[1]

def zipadd(archive, filename, newname):
  '''Add filename to archive. `newname` is required. Otherwise
     zipfile may create unsafe entries, such as "../patch.py" '''
  import zipfile
  zf = zipfile.ZipFile(archive, 'a', zipfile.ZIP_DEFLATED)
  zf.write(filename, newname)

if not sys.argv[1:]:
  sys.exit("usage: pack.py <module.py>")

modpath = sys.argv[1]
modname = os.path.basename(modpath)[:-3] # also strip extension
version  = get_version(modpath)
packname = modname + "-" + version + ".zip"
print("[*] Packing %s into %s" % (modpath, packname))
if os.path.exists(packname):
  os.remove(packname)
zipadd(packname, modpath, os.path.basename(modpath))

