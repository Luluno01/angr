
from .base_ptr_save_simplifier import BasePointerSaveSimplifier
from .dead_assignment_elimination import DeadAssignmentRemoval
from .stack_canary_simplifier import StackCanarySimplifier

_all_optimization_passes = [
    StackCanarySimplifier,
    BasePointerSaveSimplifier,
    DeadAssignmentRemoval,
]


def get_optimization_passes(arch, platform):

    import archinfo

    if isinstance(arch, archinfo.Arch):
        arch = arch.name

    platform = platform.lower()

    passes = [ ]
    for pass_ in _all_optimization_passes:
        if arch in pass_.ARCHES and platform in pass_.PLATFORMS:
            passes.append(pass_)

    return passes
