from typing import Any, Callable
from sympy.combinatorics.coset_table import CosetTable
from sympy.combinatorics.free_groups import FreeGroupElement
from sympy.combinatorics.homomorphisms import GroupHomomorphism
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public

@public
def fp_group(fr_grp, relators=...) -> tuple[FpGroup, *tuple[Any, ...]]:
    ...

@public
def xfp_group(fr_grp, relators=...) -> tuple[FpGroup, Callable[[], Any]]:
    ...

@public
def vfp_group(fr_grpm, relators) -> FpGroup:
    ...

class FpGroup(DefaultPrinting):
    is_group = ...
    is_FpGroup = ...
    is_PermutationGroup = ...
    def __init__(self, fr_grp, relators) -> None:
        ...
    
    def make_confluent(self) -> None:
        ...
    
    def reduce(self, word):
        ...
    
    def equals(self, word1, word2) -> bool | None:
        ...
    
    @property
    def identity(self):
        ...
    
    def __contains__(self, g) -> bool:
        ...
    
    def subgroup(self, gens, C=..., homomorphism=...) -> tuple[FpGroup, GroupHomomorphism] | FpGroup:
        ...
    
    def coset_enumeration(self, H, strategy=..., max_cosets=..., draft=..., incomplete=...) -> CosetTable:
        ...
    
    def standardize_coset_table(self) -> None:
        ...
    
    def coset_table(self, H, strategy=..., max_cosets=..., draft=..., incomplete=...) -> list[list[None]]:
        ...
    
    def order(self, strategy=...) -> int | Any:
        ...
    
    def most_frequent_generator(self):
        ...
    
    def random(self):
        ...
    
    def index(self, H, strategy=...) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def derived_series(self) -> list[Any]:
        ...
    
    def lower_central_series(self) -> list[Any]:
        ...
    
    def center(self) -> list[Any]:
        ...
    
    def derived_subgroup(self) -> list[Any]:
        ...
    
    def centralizer(self, other) -> list[Any]:
        ...
    
    def normal_closure(self, other) -> list[Any]:
        ...
    
    @property
    def is_abelian(self) -> Any:
        ...
    
    @property
    def is_nilpotent(self) -> Any:
        ...
    
    @property
    def is_solvable(self) -> Any:
        ...
    
    @property
    def elements(self) -> list[Any] | None:
        ...
    
    @property
    def is_cyclic(self) -> bool:
        ...
    
    def abelian_invariants(self) -> list[Any]:
        ...
    
    def composition_series(self) -> list[Any]:
        ...
    


class FpSubgroup(DefaultPrinting):
    def __init__(self, G, gens, normal=...) -> None:
        ...
    
    def __contains__(self, g) -> bool:
        ...
    
    def order(self):
        ...
    
    def to_FpGroup(self) -> Any:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...


def low_index_subgroups(G, N, Y=...) -> list[Any]:
    ...

def descendant_subgroups(S, C, R1_c_list, x, R2, N, Y) -> None:
    ...

def try_descendant(S, C, R1_c_list, R2, N, alpha, x, beta, Y) -> None:
    ...

def first_in_class(C, Y=...) -> bool:
    ...

def simplify_presentation(*args, change_gens=...) -> FpGroup | tuple[Any, Any] | tuple[Any | list[Any], Any | list[Any]]:
    ...

def elimination_technique_1(gens, rels, identity) -> tuple[list[Any], list[Any]]:
    ...

def define_schreier_generators(C, homomorphism=...) -> None:
    ...

def reidemeister_relators(C) -> None:
    ...

def rewrite(C, alpha, w):
    ...

def elimination_technique_2(C) -> tuple[Any, Any]:
    ...

def reidemeister_presentation(fp_grp, H, C=..., homomorphism=...) -> tuple[tuple[Any, ...], tuple[Any, ...], list[Any]] | tuple[tuple[Any, ...], tuple[Any, ...]]:
    ...

FpGroupElement = FreeGroupElement
