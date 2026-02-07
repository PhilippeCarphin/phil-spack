# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Philutils(CMakePackage):
    """Some of my random tools and helper scripts"""
    homepage = "https://github.com/philippecarphin/utils"
    git = "https://github.com/philippecarphin/utils.git"
    url = "philutils"
    maintainers("philippecarphin")
    license("UNKNOWN", checked_by="philippecarphin")
    depends_on("pandoc", type="build")
    version("master", branch="master")
