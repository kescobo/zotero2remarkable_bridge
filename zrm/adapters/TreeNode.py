from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Any, Dict


@dataclass
class TreeNode:
    """Base class for all tree nodes"""

    tags: List[str]
    handle: str
    type: str
    name: str
    path: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_zotero_item(cls, zot_item: Dict[str, Any]):
        data = zot_item.get("data", {})
        path = data.get("path", "")
        name = data.get("filename", "") or Path(path).name
        return TreeNode(
            handle=data["key"],
            name=name,
            type=data.get("itemType", ""),
            tags=data.get("tags", []),
            path=path,
            metadata=data,
        )
