# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install git-tools
#
# You can edit this file again by typing:
#
#     spack edit git-tools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GitTools(CMakePackage):
    """Some of my git helper scripts"""
    homepage = "https://gitlab.com/philippecarphin/git-tools"
    git = "https://gitlab.com/philippecarphin/git-tools.git"
    maintainers("philippecarphin")
    license("UNKNOWN", checked_by="philippecarphin")
    depends_on("pandoc", type="build")
    version("main")
