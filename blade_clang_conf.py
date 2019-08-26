import os
import platform
import glob
DIR_OF_THIS_SCRIPT = os.path.abspath( os.path.dirname( __file__ ) )

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
# '-Wall',
'-Wextra',
# '-Werror',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
# You 100% do NOT need -DUSE_CLANG_COMPLETER and/or -DYCM_EXPORT in your flags;
# only the YCM source code needs it.
# '-DUSE_CLANG_COMPLETER',
# '-DYCM_EXPORT=',
# THIS IS IMPORTANT! Without the '-x' flag, Clang won't know which language to
# use when compiling headers. So it will guess. Badly. So C++ headers will be
# compiled as C headers. You don't want that so ALWAYS specify the '-x' flag.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
# '-isystem',
# 'cpp/pybind11',
# '-isystem',
# 'cpp/BoostParts',
# '-isystem',
# get_python_inc(),
# '-isystem',
# 'cpp/llvm/include',
# '-isystem',
# 'cpp/llvm/tools/clang/include',
# '-I',
# 'cpp/ycm',
# '-I',
# 'cpp/ycm/ClangCompleter',
'-I',
'build64_release',
'-I',
'.',
'-I',
'~/install/include/*/',
'-isystem',
'streamlog4cxx-lib/include',
'-isystem',
'cpp3rdlib/*/include',
'-isystem',
'rpc/fbthrift/include',
'-isystem',
'rpc/thrift/include',
'-isystem',
'/usr/include',
'-isystem',
'/usr/include/x86_64-linux-gnu'
# '-isystem',
# '~/toolchains/include/c++/5.1.0',
# '-isystem',
# 'cpp/ycm/tests/gmock/gtest',
# '-isystem',
# 'cpp/ycm/tests/gmock/gtest/include',
# '-isystem',
# 'cpp/ycm/tests/gmock',
# '-isystem',
# 'cpp/ycm/tests/gmock/include',
# '-isystem',
# 'cpp/ycm/benchmarks/benchmark/include',
]

# Clang automatically sets the '-std=' flag to 'c++14' for MSVC 2015 or later,
# which is required for compiling the standard library, and to 'c++11' for older
# versions.
# if platform.system() != 'Windows':
#   flags.append( '-std=c++11' )


def expandGlob( flags ):
    i = 0
    while i < len(flags):
        flag = flags[i]
        if flag == '-I' or flag == '-isystem':
            path = flags[i + 1]
            if not path.startswith('/') and not path.startswith('~'):
                path = os.path.join(DIR_OF_THIS_SCRIPT, path)
            paths = glob.glob(os.path.expanduser(path))
            del flags[i + 1]
            del flags[i]
            j = i
            for p in paths:
                flags.insert(j, flag)
                flags.insert(j + 1, p)
                j += 2
            i += len(paths) * 2 - 1
        i += 1
    return flags
