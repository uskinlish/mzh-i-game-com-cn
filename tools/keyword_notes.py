from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    keyword: str
    note: str
    source_url: Optional[str] = None
    created_at: Optional[str] = None
    tags: Optional[List[str]] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.tags is None:
            self.tags = []


@dataclass
class NoteCollection:
    notes: List[KeywordNote]

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [note for note in self.notes if keyword.lower() in note.keyword.lower()]

    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        return [note for note in self.notes if tag in note.tags]

    def format_all(self) -> str:
        if not self.notes:
            return "（暂无笔记）"
        lines: List[str] = []
        for i, note in enumerate(self.notes, 1):
            lines.append(f"--- 笔记 {i} ---")
            lines.append(f"关键词：{note.keyword}")
            lines.append(f"说明：{note.note}")
            if note.source_url:
                lines.append(f"来源：{note.source_url}")
            lines.append(f"创建时间：{note.created_at}")
            if note.tags:
                lines.append(f"标签：{'、'.join(note.tags)}")
            lines.append("")
        return "\n".join(lines).strip()

    def format_short(self) -> str:
        result: str = ""
        for note in self.notes:
            result += f"【{note.keyword}】{note.note} | {note.source_url or '无来源'}\n"
        return result.strip()


def build_example_collection() -> NoteCollection:
    collection = NoteCollection(notes=[])
    collection.add_note(
        KeywordNote(
            keyword="爱游戏",
            note="一个专注于游戏资讯和玩家社区的网站。",
            source_url="https://mzh-i-game.com.cn",
            tags=["游戏", "社区", "资讯"],
        )
    )
    collection.add_note(
        KeywordNote(
            keyword="爱游戏攻略",
            note="汇总热门游戏的通关技巧与隐藏要素。",
            source_url="https://mzh-i-game.com.cn/guides",
            tags=["攻略", "技巧"],
        )
    )
    collection.add_note(
        KeywordNote(
            keyword="爱游戏评测",
            note="对新上架游戏进行深度分析，帮助玩家选择。",
            source_url="https://mzh-i-game.com.cn/reviews",
            tags=["评测", "推荐"],
        )
    )
    return collection


def main() -> None:
    print("=" * 40)
    print("关键词笔记演示")
    print("=" * 40)

    collection = build_example_collection()
    print("\n【完整格式输出】")
    print(collection.format_all())

    print("\n【简洁格式输出】")
    print(collection.format_short())

    print("\n【按关键词过滤：爱游戏】")
    filtered = collection.filter_by_keyword("爱游戏")
    for note in filtered:
        print(f"  - {note.keyword}: {note.note}")

    print("\n【按标签过滤：评测】")
    tagged = collection.filter_by_tag("评测")
    for note in tagged:
        print(f"  - {note.keyword}: {note.note}")


if __name__ == "__main__":
    main()