"""csg plan — v0.0.1

读一张尺寸表（CSV），打印出"要建哪些零件"的清单。

这一版【不碰 SolidWorks】，只做三件事：
  1. 读入 CSV
  2. 校验每一行有没有缺列
  3. 打印清单

用法：  python run.py parts.csv
"""
import csv
import sys

COLUMNS = ["零件名", "长", "宽", "高", "孔数", "孔径"]


def load(path):
    """读 CSV，返回每一行（dict）。缺列就报错，不猜。"""
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("表格是空的")
    for i, r in enumerate(rows, 1):
        missing = [c for c in COLUMNS if c not in r or str(r[c]).strip() == ""]
        if missing:
            raise ValueError(f"第 {i} 行缺列：{'、'.join(missing)}")
    return rows


def show(rows):
    print(f"CSG · 读到 {len(rows)} 个零件")
    for i, r in enumerate(rows, 1):
        name = r["零件名"].strip()
        length, width, height = (float(r[k]) for k in ("长", "宽", "高"))
        holes, dia = int(float(r["孔数"])), float(r["孔径"])
        print(f"{i}. {name}  {length:g}×{width:g}×{height:g}  孔 {holes} × Φ{dia:g}")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "parts.csv"
    try:
        rows = load(path)
    except FileNotFoundError:
        print(f"找不到文件：{path}")
        return 1
    except ValueError as exc:
        print(f"表格有问题：{exc}")
        return 1
    show(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
