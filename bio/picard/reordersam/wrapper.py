"""Snakemake wrapper for picard ReorderSam."""

__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__email__ = "alexhbnr@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard ReorderSam"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input[0]}"
        " --SEQUENCE_DICTIONARY {snakemake.input[1]}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output[0]}"
        " {log}"
    )
