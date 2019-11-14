from collections import OrderedDict
from typing import (
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)
from xml.etree.ElementTree import Element


class ConjugManager:
    def __init__(self, language: str = ...) -> None: ...
    def __repr__(self) -> str: ...
    def _detect_allowed_endings(self) -> Union[bool, Set[str]]: ...
    def _load_conjugations(self, conjugations_file: str) -> None: ...
    def _load_verbs(self, verbs_file: str) -> None: ...
    def get_conjug_info(self, template: str) -> Optional[OrderedDict]: ...
    def get_verb_info(self, verb: str) -> Optional[VerbInfo]: ...
    def is_valid_verb(self, verb: str) -> bool: ...


class Verb:
    def __init__(
        self,
        verb_info: VerbInfo,
        conjug_info: OrderedDict,
        subject: str = ...,
        predicted: bool = ...
    ) -> None: ...
    def __repr__(self) -> str: ...
    def _load_conjug(self) -> None: ...
    def conjugate_person(self, key: str, persons_dict: OrderedDict, term: str) -> None: ...
    def iterate(self) -> List[Union[Tuple[str, str, str], Tuple[str, str, str, str]]]: ...


class VerbEn:
    def _load_conjug(self) -> None: ...


class VerbEs:
    def _load_conjug(self) -> None: ...


class VerbFr:
    def _load_conjug(self) -> None: ...


class VerbInfo:
    def __eq__(self, other: VerbInfo) -> bool: ...
    def __init__(self, infinitive: str, root: str, template: str) -> None: ...
    def __repr__(self) -> str: ...


class VerbIt:
    def _load_conjug(self) -> None: ...


class VerbPt:
    def _load_conjug(self) -> None: ...


class VerbRo:
    def _load_conjug(self) -> None: ...


class Verbiste:
    def _load_conjugations(self, conjugations_file: str) -> None: ...
    @staticmethod
    def _load_tense(
        tense: Element
    ) -> Optional[Union[List[Union[Tuple[int, str], Tuple[int, None]]], str, List[Tuple[int, None]], List[Tuple[int, str]]]]: ...
    def _load_verbs(self, verbs_file: str) -> None: ...
    def _parse_conjugations(self, file: str) -> Dict[str, OrderedDict]: ...
    @staticmethod
    def _parse_verbs(file: str) -> Dict[str, Dict[str, str]]: ...
