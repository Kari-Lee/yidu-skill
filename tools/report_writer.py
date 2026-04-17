#!/usr/bin/env python3
"""已读 · 报告文件管理工具"""

import os
import json
import argparse
from datetime import datetime


def write_report(slug: str, content: str, base_dir: str = "./reports"):
    """写入确诊报告"""
    report_dir = os.path.join(base_dir, slug)
    os.makedirs(report_dir, exist_ok=True)

    report_path = os.path.join(report_dir, "report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)

    meta = {
        "slug": slug,
        "created_at": datetime.now().isoformat(),
        "version": 1
    }
    meta_path = os.path.join(report_dir, "meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"✅ 确诊报告已写入: {report_path}")
    return report_path


def list_reports(base_dir: str = "./reports"):
    """列出所有确诊报告"""
    if not os.path.exists(base_dir):
        print("还没有任何确诊报告。")
        return []

    reports = []
    for slug in sorted(os.listdir(base_dir)):
        meta_path = os.path.join(base_dir, slug, "meta.json")
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            reports.append(meta)
            print(f"  [{slug}] 创建于 {meta.get('created_at', '未知')}")

    if not reports:
        print("还没有任何确诊报告。")
    return reports


def delete_report(slug: str, base_dir: str = "./reports"):
    """删除确诊报告"""
    import shutil
    report_dir = os.path.join(base_dir, slug)
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
        print(f"🗑️ 已删除报告: {slug}")
    else:
        print(f"找不到报告: {slug}")


def main():
    parser = argparse.ArgumentParser(description="已读 · 报告管理")
    parser.add_argument("--action", choices=["write", "list", "delete"], required=True)
    parser.add_argument("--slug", type=str, help="报告标识符")
    parser.add_argument("--content", type=str, help="报告内容（write 时使用）")
    parser.add_argument("--content-file", type=str, help="从文件读取报告内容")
    parser.add_argument("--base-dir", type=str, default="./reports", help="报告存放目录")

    args = parser.parse_args()

    if args.action == "write":
        if not args.slug:
            parser.error("--slug is required for write action")
        content = args.content or ""
        if args.content_file and os.path.exists(args.content_file):
            with open(args.content_file, "r", encoding="utf-8") as f:
                content = f.read()
        write_report(args.slug, content, args.base_dir)

    elif args.action == "list":
        list_reports(args.base_dir)

    elif args.action == "delete":
        if not args.slug:
            parser.error("--slug is required for delete action")
        delete_report(args.slug, args.base_dir)


if __name__ == "__main__":
    main()
