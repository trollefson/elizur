import logging
import os

import numba


logger = logging.getLogger(__name__)

VERSION = "v0.2.2"

numba.config.DISABLE_JIT = os.environ.get("ELIZUR_NUMBA_DISABLE_JIT", "1").lower() in (
    "1",
    "t",
    "yes",
    "true",
)
logger.info("numba.config.DISABLE_JIT=%s", numba.config.DISABLE_JIT)
